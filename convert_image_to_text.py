from PIL import Image
import os

path = 'C:/Users/User/PycharmProjects/Convert_image_to_text/'
photo_path = 'Images/wolf_icon.jpg'



# photo size = 25x25 = 625

def get_photo_rgb(image_path):
    rgb_list = []  # store all rbg data
    photo = Image.open(path + image_path)
    for row in range(photo.size[1]):  # get the rgb data of every pixel
        for col in range(photo.size[0]):
            pixel_data = photo.getpixel((col,row))
            rgb_list.append(pixel_data)

    print("\nrgb_list length = ", len(rgb_list))
    print('Photo sizes', photo.size)
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
    assigned_character = []
    brightness_list = brightness_level(brightness_data)
    for item in brightness_list:
        if 255 >= item > 234:  # 255 to 233
            assigned_character.append(' ..')
        elif 234 >= item > 212:  # 234 to 211
            assigned_character.append(' ,,')
        elif 212 >= item > 191:  # 212 to 190
            assigned_character.append(' --')
        elif 191 >= item > 170:
            assigned_character.append(' ~~')
        elif 170 >= item > 150:
            assigned_character.append(' ::')
        elif 150 >= item > 129:
            assigned_character.append(' ;;')
        elif 129 >= item > 108:
            assigned_character.append(' ==')
        elif 108 >= item > 87:
            assigned_character.append(' !!')
        elif 87 >= item > 66:
            assigned_character.append(' **')
        elif 66 >= item > 45:
            assigned_character.append(' ##')
        elif 44 >= item > 25:
            assigned_character.append(' $$')
        else:
            assigned_character.append(' @@')
    return assigned_character


def save_file(file):
    photo = Image.open(path + photo_path)
    save_file = assing_character(file)
    text = open(path + 'Convert_image/Text/save.txt', 'w')
    for i in range(0, len(save_file), photo.size[0]):
        for x in save_file[i: i + photo.size[0]]:
            text.write(x)
        text.write('\n')
    photo.close()
    text.close()


save_file(photo_path)


def read_open_text_file():
    # text = open(path + 'Convert_image/Text/wolf.txt', 'r')
    # print('\n', text.read())
    # text.close()
    os.startfile(path + 'Convert_image/Text/save.txt')


read_open_text_file()
