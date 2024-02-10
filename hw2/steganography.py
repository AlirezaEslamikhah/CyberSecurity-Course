import shutil
import string
import matplotlib.pyplot as plt
import random
import numpy as np
import cv2
import os
from PIL import Image
from skimage.measure import shannon_entropy
want_random_character = True
count_of_random_characters = 0
count_of_site_messy_image = 5
count_of_my_messy_image = 20
count_of_all_image =30
index_of_messy_image = sorted(random.sample(range(count_of_all_image), count_of_my_messy_image))
name_of_my_messy_image=[]
entropy_dict ={}
# print(index_of_messy_image)
# input("wait")
def entropy(image_path):
    global entropy_dict
    gray_image = Image.open(image_path)#.convert('L')
    # gray_image = gray_image.flatten()
    # Calculate entropy
    entropy_value = shannon_entropy(gray_image)
    entropy_dict[image_path] = entropy_value

    # image_path = 'download.png'#messy
    # gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # image_path2 = 'Training_1206.jpg'
    # gray_image2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
    # # Calculate entropy
    # entropy_value1 = shannon_entropy(gray_image)
    # entropy_value2 = shannon_entropy(gray_image2)

    # print(f"Entropy of the image1: {entropy_value1} , Entropy of the image2: {entropy_value2}")
    
def histogram():

    # Read the image
    image_path = 'download (3).jfif'#messy

    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Calculate entropy
    entropy_value = shannon_entropy(gray_image)
    print(f"Entropy of the image: {entropy_value}")
    image = cv2.imread('download (3).jfif', cv2.IMREAD_GRAYSCALE)

    # image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    for i in image:
        print(f"({i})")
    count = {}
    flat = image.flatten()
    for i in flat:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    ##for key in count:
    ##   print(f"{count[key]} , {vlaue}")
    count = sorted(count.items(), key=lambda x:x[0])

    print(count)
# def hide():
def steganography(img):
    global want_random_character
    # img = cv2.imread("download (3).jfif",  cv2.IMREAD_GRAYSCALE)
    # print(int(img.shape[0]*img.shape[1]/8))

#   W,H,rgb#= img.shape
#   if len(img.shape) == 3:
#     W,H,rgb= img.shape
#   elif len(img.shape) == 2:
    W,H = img.shape
#   else:
#     print("unkhown shape")
#     return

    # want_random_character ='y'
    if want_random_character =='n':
        img = hide(img , False)
    else:
        img = hide(img , True)

#   if len(img.shape) == 3:
#     img = img.reshape((W,H,rgb))
#   elif len(img.shape) == 2:
    img = img.reshape((W,H))
    # print(f"shape:{img.shape}")
    # print(f"len:{len(img)}")
    # input("wait")
    img = Image.fromarray(img)
    return img

def hide(img, flag):#true means i want maximmum message size
    if flag == False:
        # def generate_random_string(count):
        # Define the set of characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random string of the specified count
        random_string = ''.join(random.choice(characters) for _ in range(count_of_random_characters))

        # return random_string
        message = random_string
        message += '[END]'

        message = message.encode('ascii')
        message_bits = ''.join([format(i,'08b') for i in message])
        # print(f"message_bits:{message_bits} , len:{len(message_bits)}")
        img = img.flatten()

        for idx, bit in enumerate(message_bits):# enumerate -> get index and value
            val = img[idx]
            val = bin(val)
            val = val[:-1] + bit
            img[idx] = int(val,2)
        return img
    else:
        count = int(img.shape[0]*img.shape[1]/8)-1
        img = img.flatten()
        for idx in range(count):# enumerate -> get index and value
            bit =random.randint(0,1)
            # print(f"bit:{bit} , bin(bit):{bin(bit)} , bit(bit)[0]:{bin(bit)[0]}")
            # input("wait")
            val = img[idx]
            val = bin(val)
            # print(f"val:{val} , bit:{bit}")
            val = val[:-1] + str(bit)
            # print(f"val:{val} , bit:{bit}")
            # input("wait")

            img[idx] = int(val,2)
        return img
def enheraf(image_path):
# Read the image
    # gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    gray_image = Image.open(image_path)#.convert('L')

    # Calculate the standard deviation
    std_deviation = np.std(gray_image)
    image_path= image_path.split('\\')
    entropy_dict[image_path[-1]] = std_deviation

    # print(f"Standard Deviation of the image: {std_deviation}")
def steganalysis(image_path):
    # entropy(image_path)
    enheraf(image_path)
    # enheraf()
    # ...

def main():
    global count_of_all_image , want_random_character ,  count_of_random_characters , entropy_dict , name_of_my_messy_image
    want_random_character = input("do you want random maximmum message?(y/n)")
    if want_random_character == 'n':
        count_of_random_characters = input("get count of characters(your count must not greater than 60,000): ")

    counter = 0
    # steganography(2)
    # input("wait")
    directory_path = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\/resize_set'
    output_directory = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\/unkhown_set'
    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        if count_of_all_image == 0:
            break
        count_of_all_image-=1#fix it

        image_name = filename
        image_path = os.path.join(directory_path, filename)
                # image_name = image_name.replace('.' , str(count_of_all_image)+'.')
        output_path = os.path.join(output_directory, image_name)
        # Check if the file is an image (you might want to add more file type checks)
        # if filename.endswith(('.jpg', '.jpeg', '.png')):
        if filename.endswith('jpg'):
            # Construct the full path to the image
            if counter in index_of_messy_image:
                name_of_my_messy_image.append(filename)

                image = cv2.imread(image_path,  cv2.IMREAD_GRAYSCALE)
                # cv2.imshow('Image', image)
                # cv2.waitKey(0)
                img =steganography(image)
                
                img.save(output_path)
            else:
                shutil.copy(image_path, output_directory)
            counter +=1
    site_messy_image_path = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\site_messy_image'
    # output_directory = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\/unkhown_set'
    #copy messy site
    for filename in os.listdir(site_messy_image_path):
        image_path = os.path.join(site_messy_image_path, filename)
        shutil.copy(image_path, output_directory)
        name_of_my_messy_image.append(filename)
    #steganalysis
    for filename in os.listdir(output_directory):
        image_path = os.path.join(output_directory, filename)

        steganalysis(image_path)


    entropy_dict = sorted(entropy_dict.items(), key=lambda x:x[1] , reverse=True)
    
    count = 0
    number_of_mistakes =count_of_site_messy_image+count_of_my_messy_image
    for key , value in entropy_dict:
        if key in name_of_my_messy_image:
            number_of_mistakes-=1
        print(f"key {key} , value {value}:")
        count+=1
        if count ==20:
            break
    print(f"realy messy images\n{name_of_my_messy_image}")
    print(f"error percentage:{number_of_mistakes/(count_of_site_messy_image+count_of_my_messy_image)}")
if __name__ == '__main__':
    main()