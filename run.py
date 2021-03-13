#! /usr/bin/env python3
import os
import requests

image_file=[]
image_path = os.path.expanduser('~')+'/supplier-data/images/'
for image in os.listdir(image_path):
  if '.jpeg' in image:
    image_file.append(image)
desc_file=[]
desc_path = os.path.expanduser('~')+'/supplier-data/descriptions/'
for desc in os.listdir(desc_path):
  if '.txt' in desc:
    desc_file.append(desc)

list=[]
category={}
for desc in desc_file:
  with open(os.path.join(desc_path,desc)) as file:
    line = file.readlines()
    category['name']=line[0].strip()
    category['weight']=int(line[1].strip().split(' ')[0])
    category['description']=line[2].strip()

    for image in image_file:
      if desc.split('.')[0] in image.split('.')[0]:
        category ['image_name']=image

    resp = requests.post('http://35.238.175.250/fruits/', json=category)
