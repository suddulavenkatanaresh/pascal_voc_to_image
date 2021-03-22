import numpy as np 
import os 
from xml.etree import ElementTree as et
import cv2
import matplotlib.pyplot as plt 
#from PIL import Image 
from PIL import Image, ImageOps 


files_dir="/home/vihal_venkat/Desktop/numberplate/indian /images"
  




files = [files for files in sorted(os.listdir(files_dir)) if files[-4:]=='.xml']
               
print(files)
        
for i, xml in enumerate(files):
    xml_path=os.path.join(files_dir,xml)
    tree = et.parse(xml_path)
    root = tree.getroot()
    for member in root.findall('object'):
            #labels.append(self.classes.index(member.find('name').text))
            
            # bounding box
            path=tree.find('path').text
            
            
            
            xmin = int(member.find('bndbox').find('xmin').text)
            xmax = int(member.find('bndbox').find('xmax').text)
            
            ymin = int(member.find('bndbox').find('ymin').text)
            ymax = int(member.find('bndbox').find('ymax').text)
            image_name=member.find('name').text
            
            
        
            im=Image.open(path)
            #plt.imshow(im)
            im = im.crop((xmin,ymin,xmax,ymax))
            im2 = ImageOps.grayscale(im) 

            #plt.imshow(im2)
            
            im_name="/home/vihal_venkat/indian_licence_pales/"+image_name+'.jpg'
            print(im_name)
            im2.save(im_name) 
            
            
            
            
            
            
        


    
