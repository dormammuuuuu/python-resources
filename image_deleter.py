import os
import random

def group_and_delete_random_images(folder_path, remain=10, group_size=30):
    # Get the list of all files in the folder
    files = os.listdir(folder_path)
    # Filter out the files that are not images
    images = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
    # Divide the images into groups of group_size
    groups = [images[i:i+group_size] for i in range(0, len(images), group_size)]
    # For each group, delete (group_size - remain) random images and remain remain images
    for group in groups:
        images_to_delete = random.sample(group, group_size - remain)
        for image in images_to_delete:
            os.remove(os.path.join(folder_path, image))

# Example usage
folder_path = 'C:/Users/jeric/Desktop/Extracted Pistol/capstone nila'
group_and_delete_random_images(folder_path, remain=5, group_size=50)


