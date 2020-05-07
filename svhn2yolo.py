import os
import json
import cv2 as cv
from pymatreader import read_mat

def mat2dict(filename):
    print('[DEBUG] Started loading')
    data = read_mat(filename)
    print('[DEBUG] Finished loading')
    return data

def dict2json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    print('[DEBUG] Successful')

def json2dict(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
data = json2dict('C:/Users/magic/Documents/Projects/SVHN/train/digitStruct.json')
dataset_folder = 'C:/Users/magic/Documents/Projects/SVHN'

'''
{'width': 15.0, 'label': 8.0, 'top': 18.0, 'left': 65.0, 'height': 47.0}
{'width': 28.0, 'label': 8.0, 'top': 18.0, 'left': 81.0, 'height': 53.0}
{'width': [25.0, 27.0], 'label': [9.0, 5.0], 'top': [3.0, 3.0], 'left': [36.0, 57.0], 'height': [45.0, 45.0]}
{'width': [25.0, 25.0], 'label': [2.0, 2.0], 'top': [6.0, 4.0], 'left': [34.0, 61.0], 'height': [40.0, 40.0]}
{'width': [7.0, 15.0, 17.0], 'label': [1.0, 6.0, 9.0], 'top': [10.0, 8.0, 9.0], 'left': [35.0, 44.0, 62.0], 'height': [25.0, 25.0, 25.0]}
'''

for folder in ['train', 'test']:
    data = mat2dict(os.path.join('C:/Users/magic/Documents/Projects/SVHN', folder, 'digitStruct.mat'))
    bbox = data['digitStruct']['bbox']
    name = data['digitStruct']['name']
    for i in range(len(bbox)):
        print(folder, i)
        if type(bbox[i]['label']) == float:
            img = cv.imread(os.path.join(dataset_folder, folder, name[i]))
            width = img.shape[1]
            height = img.shape[0]
            with open(os.path.join(dataset_folder, folder, name[i].split('.')[0]+'.txt'), 'w') as txt_file:
                x_centre = (bbox[i]['left'] + bbox[i]['width']/2)/width
                y_centre = (bbox[i]['top'] + bbox[i]['height']/2)/height
                if bbox[i]['label'] == 10.0:
                    label_fix = 0
                else:
                    label_fix = bbox[i]['label']
                txt_file.write(' '.join([str(int(label_fix)), str(x_centre), str(y_centre), str(bbox[i]['width']/width), str(bbox[i]['height']/height)]))
        else:
            img = cv.imread(os.path.join(dataset_folder, folder, name[i]))
            width = img.shape[1]
            height = img.shape[0]
            with open(os.path.join(dataset_folder, folder, name[i].split('.')[0]+'.txt'), 'w') as txt_file:
                for k in range(len(bbox[i]['width'])):
                    x_centre = (bbox[i]['left'][k] + bbox[i]['width'][k]/2)/width
                    y_centre = (bbox[i]['top'][k] + bbox[i]['height'][k]/2)/height
                    if bbox[i]['label'][k] == 10.0:
                        label_fix = 0
                    else:
                        label_fix = bbox[i]['label'][k]
                    txt_file.write(' '.join([str(int(label_fix)), str(x_centre), str(y_centre), str(bbox[i]['width'][k]/width), str(bbox[i]['height'][k]/height), '\n']))