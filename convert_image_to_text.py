from PIL import Image
import os

path = 'C:/Users/User/PycharmProjects/Convert_image_to_text/'

#photo size = 25x25 = 625

def get_photo_rgb(image_path):
    rgb_list = []# store all rbg data
    rgb_table = [] # rgb data in sub list
    photo = Image.open(path + image_path)
    for row in range(photo.size[0]):#get the rgb data of every pixel
        for col in range(photo.size[1]):
            pixel_data = photo.getpixel((row,col))
            rgb_list.append(pixel_data)

    for i in range(0 , len(rgb_list), photo.size[0]):#convert rgb list in sub list
        chunk = rgb_list[i : i + photo.size[0]]
        rgb_table.append(chunk)

    print("\nrgb_list length = ", len(rgb_list))
    print("\nrgb_list length = ", len(rgb_table))
    photo.close()

    return rgb_table

get_photo_rgb('Images/flower_small.jpg')


#def brightness_nevel(rgb_list)










def read_open_text_file():
    text = open(path + 'Convert_image/Text/wolf.txt', 'r')
    print('\n',text.read())
    text.close()
    # os.startfile(path + 'Convert_image/Text/wolf.txt')

#read_open_text_file()
