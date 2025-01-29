from PIL import Image,ImageEnhance,ImageFilter
import os

# img1 =Image.open("dog image 1.jpg")
# img1.save('dog1.png')
# img1.show()

# MAX_SIZE =(250,250)
# img1.thumbnail(MAX_SIZE) 
# img1.save('dog1small.jpg')   

# for item in os.listdir():
#     if item.endswith('jpg'):
#        img1 = Image.open(item)
#        filename,extension=os.path.splitext(item)
#        img1.save(f'{filename}.png')

# ----Sharpness ----
img1 =Image.open("dog image 1.jpg")
enhancer =ImageEnhance.Sharpness(img1)
enhancer.enhance(6).save('dog1edited.jpg')

# -----color----
img2 =Image.open("dog image 2.jpg")
enhancer =ImageEnhance.Color(img2)
enhancer.enhance(0).save('dog2edited.jpg')

# -----Brightness----
img3 =Image.open("dog image 3.jpg")
enhancer =ImageEnhance.Brightness(img3)
enhancer.enhance(2.5).save('dog3edited.jpg')

#  -----Contrast----
img4 =Image.open("Nature image4.jpg")
enhancer =ImageEnhance.Contrast(img4)
enhancer.enhance(1.5).save('Natureimage4.jpg')

#  ----blur----
img5 =Image.open("Nature image 5.jpg")
img5.filter(ImageFilter.GaussianBlur).save("BlurImage.png")


       
