# import json
# import os

# # Function to check if image paths are readable
# def check_image_paths(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             data = json.loads(line)
#             if 'image' in data:
#                 image_path = data['image']
#                 if not os.path.isfile(image_path):
#                     print(f"Image not found or unreadable: {image_path}")
#                 else:
#                     print(f"Image is readable: {image_path}")

# # Usage example
# check_image_paths('./data/val.jsonl')


import os

# # Check if the paths are correct
# print(os.path.isfile('./data/train.jsonl'))
# print(os.path.isfile('./data/val.jsonl'))
# print(os.path.isfile('./data/test.jsonl'))
# print(os.path.isdir('./data/imgs'))
# print(os.path.isfile('./data/imgs/281.png'))

import json
import os
from PIL import Image

# Function to check if image paths are readable and display the images
import json
import os
from PIL import Image
import time
# Function to check if image paths are readable and display the images
def check_and_display_images_from_json(json_data):
    messages = json_data.get("messages", [])
    
    for message in messages:
        image_path = message.get("image")
        if image_path:
            if not os.path.isfile(image_path):
                print(f"Image not found or unreadable: {image_path}")
            else:
                print(f"Displaying image: {image_path}")
                try:
                    img = Image.open(image_path)
                    img.show()
                    time.sleep(10)
                except Exception as e:
                    print(f"Error loading image {image_path}: {e}")

# Usage example
check_and_display_images_from_json('./data/test.json')
