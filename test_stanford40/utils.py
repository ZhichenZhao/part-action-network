'''
project: Part Action Network(PAN)
name: config.py
author: Zhichen Zhao
data: 2017.09

This file describes some tools
'''

from config import *
import numpy as np
def get_pred_by_batch(net, imgs_in_batch, keys, coefs):
    prediction = [0]*cls_len
    sum_coefs = sum(coefs)
    sum_batch = len(imgs_in_batch)
    for imgs in imgs_in_batch:
        net.blobs['data'].data[...] = imgs
        out = net.forward()
        for idx, key in enumerate(keys):
            prediction_tmp = out[key][0]
            prediction = [x+coefs[idx]*y/sum_coefs/sum_batch for x,y in zip(prediction,prediction_tmp)]
    return prediction

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

