# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:36:53 2021

@author: admin
"""

#face locations
import face_recognition
family_photo =face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\family pic.jpg")
face_loc =face_recognition.face_locations(family_photo)
print(face_loc)
print("Number of faces located...",len(face_loc))