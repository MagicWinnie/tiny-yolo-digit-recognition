import os

dataset_folder = 'C:/Users/magic/Documents/Projects/SVHN'
darknet_folder = 'C:/Users/magic/Documents/Projects/darknet/custom_data'

for folder in ['train', 'test']:
    with open(os.path.join(darknet_folder, folder + '.txt'), 'w') as f:
        for fi in os.listdir(os.path.join(dataset_folder, folder)):
            if fi.split('.')[1] == 'png':
                f.write(os.path.join(dataset_folder, folder, fi).replace('\\', '/') + '\n')