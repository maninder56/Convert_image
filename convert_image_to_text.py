from PIL import Image
import os

path = 'C:/Users/User/PycharmProjects/Convert_image_to_text/'
photo_path = 'Images/flower_small.jpg'


# photo size = 25x25 = 625

def get_photo_rgb(image_path):
    rgb_list = []  # store all rbg data
    photo = Image.open(path + image_path)
    for row in range(photo.size[0]):  # get the rgb data of every pixel
        for col in range(photo.size[1]):
            pixel_data = photo.getpixel((row, col))
            rgb_list.append(pixel_data)

    print("\nrgb_list length = ", len(rgb_list))
    photo.close()

    return rgb_list

def brightness_level(photo_data):
    brightness_list = []
    rgb_list = get_photo_rgb(photo_data)
    for rgb in rgb_list:
        average_value = (rgb[0] + rgb[1] + rgb[2]) / 3
        brightness_list.append(round(average_value))
    return brightness_list


def scale_down(photo_data):#to scale down picture quality
    new_photo_list = []
    old_data = brightness_level(photo_data)
    photo = Image.open(path + photo_path)
    photo_size = [photo.size[0], photo.size[1]]
    for i in range(0, len(old_data), photo.size[0]):  # convert rgb list in sub list
        chunk = old_data[i: i + photo.size[0]]
        new_photo_list.append(chunk)
    photo.close()

    scale_down_list =[]
    scale_down_value = 5

    for i in new_photo_list:
        print(i)









def assing_character(brightness_data):
    assined_character = []
    brightness_list = brightness_level(brightness_data)
    for item in brightness_list:
        if 255 >= item > 234: #255 to 233
            assined_character.append('.')

        elif 234 >= item > 212: #234 to 211
            assined_character.append(',')

        elif 212 >= item > 191: #212 to 190
            assined_character.append('-')

        elif 191 >= item > 170:
            assined_character.append('~')

        elif 170 >= item > 150:
            assined_character.append(':')

        elif 150 >= item > 129:
            assined_character.append(';')

        elif 129 >= item > 108:
            assined_character.append('=')

        elif 108 >= item > 87:
            assined_character.append('!')

        elif 87 >= item > 66:
            assined_character.append('*')

        elif 66 >= item > 45:
            assined_character.append('#')

        elif 44 >= item > 25:
            assined_character.append('$')

        else:
            assined_character.append('@')

    return assined_character



'''
def save_file(file):
    save_file = character_table(file)
    for i in save_file:
        print(i)'''


#print(save_file(photo_path))
#print(brightness_level(photo_path))

print(scale_down(photo_path))

































def read_open_text_file():
    text = open(path + 'Convert_image/Text/wolf.txt', 'r')
    print('\n', text.read())
    text.close()
    # os.startfile(path + 'Convert_image/Text/wolf.txt')

# read_open_text_file()



























