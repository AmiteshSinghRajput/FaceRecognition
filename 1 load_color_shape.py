# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:06:58 2021

@author: admin
"""

# Amitesh 
# program to load a color picture and find shape
import face_recognition
photo_amit= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\ajitmts.jpg","RGB")
photo_amit1= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\Screenshots\\jyanshu.png","RGB")
photo_amit2= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\Screenshots\\amitesh.png")

print("the shape of the color photos file are...")
print("photo =",photo_amit.shape)
print("photo1 =",photo_amit1.shape)
print("photo2 =",photo_amit2.shape)
