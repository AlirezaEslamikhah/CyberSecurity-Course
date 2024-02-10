from PIL import Image
import os

# Input and output directories
input_directory = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\/train2\happy'
output_directory = 'F:\classes\/amniat\hw\/2-steganography\image_dataset\/new_set'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Desired size for the resized images
new_size = (600,800)  # Specify your desired width and height

# Loop through each file in the input directory
count = 1000
for filename in os.listdir(input_directory):
    if count ==0:
        break
    # Check if the file is an image (you might want to add more file type checks)
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Construct the full path to the input image
        input_path = os.path.join(input_directory, filename)

        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            count -=1
            resized_img = img.resize(new_size)

            # Construct the full path to the output image
            output_path = os.path.join(output_directory, filename)

            # Save the resized image
            resized_img.save(output_path)

print("Resizing and saving complete.")
