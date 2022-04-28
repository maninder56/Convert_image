from PIL import Image

photo = Image.open('Images/wolf_icon.jpg')

# Image size is 256x256
size = photo.size

rgb_list = []
# Get rgb values for each pixel, the result is a list that has 256*256 = 65536 values
for row in range(photo.size[1]):
    for col in range(photo.size[0]):
        #get brightness data
        pixel = [photo.getpixel((col,row))]
        rgb_list.append(pixel)
        #print('height:',row,'| width:',col,'| rgb values:',pixel)


print(rgb_list)
print(len(rgb_list))

#Get brightness from rgb values