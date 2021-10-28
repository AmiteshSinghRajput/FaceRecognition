from PIL import Image
import face_recognition
photo_amit= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\ajitmts.jpg","RGB")
photo_amit1= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\Screenshots\\jyanshu.png","RGB")
photo_amit2= face_recognition.load_image_file("C:\\Users\\admin\\Pictures\\Screenshots\\amitesh.png")

print("the shape of the photos are")
print("photo =",photo_amit.shape)
print("photo1 =",photo_amit1.shape)
print("photo2 =",photo_amit2.shape)


pil_photo_amit=Image.fromarray(photo_amit)
pil_photo_amit.show()
pil_photo_amit1=Image.fromarray(photo_amit1)
pil_photo_amit1.show()
pil_photo_amit2=Image.fromarray(photo_amit2)
pil_photo_amit2.show()

