####### text watermark 
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

def add_watermark(input_image_path, watermark_text):
    # Open the original image
    original_image = Image.open(input_image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(original_image)

    # Choose a font and size for the watermark
    font = ImageFont.load_default()

    # Specify the position and color of the watermark
    watermark_position = (100, 100)
    watermark_color = (255, 255, 255)  # white color

    # Add the watermark text to the image
    draw.text(watermark_position, watermark_text, font=font, fill=watermark_color)

    # Convert the PIL image to a NumPy array
    img_array = np.array(original_image)

    # Display the image using matplotlib
    plt.imshow(img_array)
    plt.axis('off')  # Turn off axis labels
    plt.show()

if __name__ == "__main__":
    input_image_path = "/sample.jpg"
    watermark_text = "Soal 2 Tamrin 2 Dars Amniat Shabake hay Computeri"
    add_watermark(input_image_path, watermark_text)







########## picture watermatk 
# import all the libraries
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# to open the image
image = Image.open("/sample.jpg")
# this open the photo viewer
image.show()
plt.imshow(image)



# image watermark
size = (500, 100)
crop_image = image.copy()
# to keep the aspect ration in intact
crop_image.thumbnail(size)

# add watermark
copied_image = image.copy()
# base image
copied_image.paste(crop_image, (500, 200))
# pasted the crop image onto the base image
plt.imshow(copied_image)
# copied_image.save("./output/")
