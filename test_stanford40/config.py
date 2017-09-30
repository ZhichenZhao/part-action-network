'''
project: Part Action Network(PAN)
name: config.py
author: Zhichen Zhao
data: 2017.09

This file describes some basic configure of PAN,
include models, paths
'''
import sys
# change your pycaffe path here
sys.path.append('yourcaffe/python')
import caffe


cls_len = 40

'''
In the test phase, do once resize and crop a region at center,
see README for details
'''
scales = [256, 240] 
cropped_size = 224

model_path = '../models/'
net = caffe.Net(model_path + 'part_action_with_ctx_deploy.prototxt',model_path + 'tmp/part_action_with_ctx.caffemodel', caffe.TEST)

caffe.set_mode_gpu()

data_dir = '../data/stanford40/'
bbox_dir = 'BBOXImages/'
ctx_dir = 'JPEGImages/'
part_dir = 'PARTImages/'

test_list_file = open(data_dir + 'test.txt','r')
categories_stanford40 = [\
'applauding',\
'blowing_bubbles',\
'brushing_teeth',\
'cleaning_the_floor',\
'climbing',\
'cooking',\
'cutting_trees',\
'cutting_vegetables',\
'drinking',\
'feeding_a_horse',\
'fishing',\
'fixing_a_bike',\
'fixing_a_car',\
'gardening',\
'holding_an_umbrella',\
'jumping',\
'looking_through_a_microscope',\
'looking_through_a_telescope',\
'playing_guitar',\
'playing_violin',\
'pouring_liquid',\
'pushing_a_cart',\
'reading',\
'phoning',\
'riding_a_bike',\
'riding_a_horse',\
'rowing_a_boat',\
'running',\
'shooting_an_arrow',\
'smoking',\
'taking_photos',\
'texting_message',\
'throwing_frisby',\
'using_a_computer',\
'walking_the_dog',\
'washing_dishes',\
'watching_TV',\
'waving_hands',\
'writing_on_a_board',\
'writing_on_a_book']










