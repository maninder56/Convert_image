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
    '''
    for i in range(0, len(rgb_list), photo.size[0]):  # convert rgb list in sub list
        chunk = rgb_list[i: i + photo.size[0]]
        rgb_table.append(chunk)'''

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

def rgb_table(character_table):






print(assing_character(photo_path))
print(brightness_level(photo_path))

def read_open_text_file():
    text = open(path + 'Convert_image/Text/wolf.txt', 'r')
    print('\n', text.read())
    text.close()
    # os.startfile(path + 'Convert_image/Text/wolf.txt')

# read_open_text_file()


number = 2

if 1 < number <= 5 : # 1 to 5
    print ("You entered a number in the range of 1 to 5")
elif int(number) in range(6, 11):# 6 to 10
    print ("You entered a number in the range of 6 to 10")
else:
    print ("Your number wasn't in the correct range")


























