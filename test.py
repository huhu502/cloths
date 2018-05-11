import os
import shutil
import cv2
import random
import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


df_train = pd.read_csv('../data/labels_train.csv', header=None)
df_train.columns = ['id','imageId', 'url', 'labelId']
df_train.head()
df_train.reset_index(inplace=True)
del df_train['index']
df_train.reset_index(inplace=True)
print('{0}: {1}'.format('labels_train', len(df_train)))
df_train.head()
label_length = 10
base_dir = './data/'
train_dir = os.path.join(base_dir, 'train')
valid_dir = os.path.join(base_dir, 'valid')
data_sets = ['train','valid']

for data_set in data_sets:
    set_dir = os.path.join(base_dir, data_set)
    if not os.path.exists(set_dir):
        os.makedirs(set_dir)
    for i in range(label_length):
        label_dir = os.path.join(set_dir, str(i))
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
data_length = len(set_dir)

for i in range(data_length):
    if i != 0 :
        tmp_label = df_train['labelId'][i]
        image_id = df_train['imageId'][i]
        tmp_label = tmp_label.replace('[','')
        tmp_label = tmp_label.replace(']','')
        tmp_label = tmp_label.replace('\'','')
        tmp_label = tmp_label.split(",")
        tmp_label = map(int,tmp_label)
        tmp_label = list(tmp_label)
        label = tmp_label.index(max(tmp_label))