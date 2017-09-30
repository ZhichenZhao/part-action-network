'''
project: Part Action Network(PAN)
name: config.py
author: Zhichen Zhao
date: 2017.09

This file describes the main process of test PAN on Stanford40
'''
import sys
import os
import numpy as np
import cv2
import warnings
from config import *
import augmentor as aug
import utils as utl
sys.path.append('yourcaffe/python')
from sklearn.metrics import average_precision_score
import caffe

# read image file
test_image = []
test_label = []

for line in test_list_file:
    line=line.strip('\n').split(' ')
    test_image.append(line[0])
    test_label.append(int(line[1]))
test_list_file.close()

# prepare transformers for multiscale test
transformers = []
def get_transformer(inp_shape):
    origin_shape = (9,3) + (inp_shape,inp_shape)
    transformer = caffe.io.Transformer({"data": origin_shape})
    transformer.set_transpose("data", (2,0,1))
    transformer.set_mean("data", np.array([128,128,128]))
    transformer.set_raw_scale("data", 255)
    transformer.set_channel_swap("data",(2,1,0))
    return transformer

test_app = []
right = 0
wrong = 0
predictions = []
for s in scales:
    transformers.append(get_transformer(s))
pred_multiscale = []
tested_imgs = []

# pre-process images by transformers but not resize or crop
for s_idx,s in enumerate(scales):
    for idx, im in enumerate(test_image):
        tested_imgs.append([])
        im_bbox = caffe.io.load_image(data_dir + bbox_dir + im)
        im_ctx = caffe.io.load_image(data_dir + ctx_dir + im)
        pics = []
        pics.append(transformers[s_idx].preprocess('data', im_bbox))
        pics.append(transformers[s_idx].preprocess('data', im_ctx))
        for part in ['head','torso','legs','larm','rarm','lhand','rhand']:
            im_name = data_dir + part_dir + im[:-4] + '_' + part + im[-4:]
            if os.path.exists(im_name):
                im_part = caffe.io.load_image(im_name)
            else:
                #warnings.warn(im_name + ' ' + part + ' lost!' + ', use mean image as filler')
                im_part = 0.5 * np.ones((256,256,3),dtype=float)
            pics.append(transformers[s_idx].preprocess('data', im_part)) 
        tested_imgs[s_idx].append(pics)
        print('loading image: ' + im)

# one-pass resize with crop and forward the Part Action Network
for i in range(len(test_image)):
    score = np.zeros(cls_len)
    for s_idx, s in enumerate(scales):
        print('processing image: ' + test_image[i] + ' at scale: ' + str(s))
        pics = tested_imgs[s_idx][i]
        pics = aug.crop_imgs_at_center(pics, s, cropped_size)
        pics_f1 = aug.aug_flip(pics)

        prediction = utl.get_pred_by_batch(net, [pics,pics_f1], ['fc_stanford2','fc_part_act'], [1,0.2])
        score += prediction
    assert score.shape[0]==cls_len
    score /= len(scales)
    predictions.append(list(utl.softmax(score)))

# calculate the mean accuracy and mean average precision
mA = []
preds = [pre.index(max(pre)) for pre in predictions]
for cls in range(len(predictions[0])):
    label = [1 if y == cls else 0 for y in test_label]
    amt = sum(label)
    pr = [1 if pre == cls else 0 for pre in preds]
    tp = sum([1 if p==1 and l==1 else 0 for p,l in zip(pr,label)])
    acc = tp/(amt+0.0000001)
    print(categories_stanford40[cls] + ' accuracy: '+ str(acc))
    mA.append(acc)
print('mA:')
print sum(mA)/len(mA)
mAP = 0
for cls in range(len(predictions[0])):
    samples = [pred[cls] for pred in predictions]
    labels = [1 if y == cls else 0 for y in test_label]
    ap = average_precision_score(labels, samples)
    mAP += ap
    print(categories_stanford40[cls] + ' AP: ' + str(ap))

print 'mAP:'
print mAP/cls_len
    
