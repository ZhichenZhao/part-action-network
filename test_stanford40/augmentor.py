'''
project: Part Action Network(PAN)
name: config.py
author: Zhichen Zhao
date: 2017.09

This file describes test augmentations
'''

import numpy as np
import random

def aug_flip(imgs):
    '''bbox->flipped bbox, parts->flipped parts'''
    res = []
    for img in imgs:
        res.append(img[:,:,::-1])
    return res 

def aug_part_flip(imgs):
    '''bbox->bbox, parts->flipped parts'''
    res = []
    for i, img in enumerate(imgs):
        if i<2:
            res.append(img)
        else:
            res.append(img[:,:,::-1])
    return res

def aug_rand_flip(imgs):
    '''random flip each part and img, bbox->flipped bbox, parts->flipped parts'''
    res = []
    for img in imgs:
        choose = random.randint(0,1)
        if choose == 0:
            res.append(img)
        else:
            res.append(img[:,:,::-1])
    return res


def crop_imgs_at_center(imgs, inp_shape, tar_shape):
    '''crop a region at the center with target size'''
    res = []
    for img in imgs:
        res.append(img[:,(inp_shape-tar_shape)/2:(inp_shape-tar_shape)/2+tar_shape,(inp_shape-tar_shape)/2:(inp_shape-tar_shape)/2+tar_shape])
    return res

