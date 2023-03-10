import os
import shutil

def split_images(source_dir, destination_dir, num_splits):
    # Get a list of all the image files in the source directory
    image_files = [f for f in os.listdir(source_dir) if f.endswith('.txt') or f.endswith('.xml')]

    # Determine the number of images per split
    images_per_split = len(image_files) // num_splits

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.mkdir(destination_dir)

    # Iterate over each split
    for i in range(num_splits):
        # Create a subdirectory for this split
        split_dir = os.path.join(destination_dir, f'split_{i+1}')
        os.mkdir(split_dir)

        # Determine the start and end indices of the images for this split
        start_index = i * images_per_split
        end_index = (i+1) * images_per_split

        # Copy the images for this split to the split directory
        for image_file in image_files[start_index:end_index]:
            source_path = os.path.join(source_dir, image_file)
            destination_path = os.path.join(split_dir, image_file)
            shutil.copyfile(source_path, destination_path)

if __name__ == '__main__':
    source_dir = 'C:/Users/jeric/Downloads/Compressed/WiderPerson/Yolo Annotations'
    destination_dir = 'C:/Users/jeric/Downloads/Compressed/WiderPerson/Split_Annotations'
    num_splits = 3

    split_images(source_dir, destination_dir, num_splits)
