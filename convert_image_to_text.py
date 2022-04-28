from PIL import Image

path = 'C:/Users/User/PycharmProjects/Convert_image_to_text/Images/'

photo = Image.open(path + 'flower.jpg')

print(photo.format,photo.size, photo.mode)






photo.close()