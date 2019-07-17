import os
import shutil
import random
import argparse
import sys

def scanAllImages(folder_path):
        images = []

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('jpg'):
                    relativePath = os.path.join(root, file)
                    path = os.path.abspath(relativePath)
                    images.append(path)
        images.sort(key=lambda x: x.lower())
        return images

parser = argparse.ArgumentParser()
parser.add_argument('--in_dir', default='', help="Path to the annotation directory")
parser.add_argument('--out_dir', default='', help="Path to keypoints xml directory")
parser.add_argument('--number_of_file', default='0', help="Path to keypoints xml directory")
agrs = parser.parse_args()

in_dir = agrs.in_dir
output_dir = agrs.out_dir
num = int(agrs.number_of_file)

if num == 0: sys.exit()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = scanAllImages(in_dir) #[f for f in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, f))]

random_files = random.sample(files, len(files))

for idx, val in enumerate(random_files): 
    if idx == num:
        sys.exit()
    file_name = os.path.basename(val)
    shutil.copy(val, os.path.join(output_dir, file_name))
