#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
image_path = os.path.expanduser('~')+"/supplier-data/images/"
image_file=[]
for image in os.listdir(image_path):
  if ".jpeg" in image:
    image_file.append(image)

for idv_image in image_file:
  with open(os.path.join(image_path,idv_image),'rb') as img:
   r = requests.post(url, files={'file':img})
