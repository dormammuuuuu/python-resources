import os
import imgaug as ia
from imgaug import augmenters as iaa
import cv2

def augment_images(folder_path):
    # Get the list of all files in the folder
    images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Define the augmentations to be applied
    sometimes = lambda aug: iaa.Sometimes(0.5, aug)
    augmentations = iaa.Sequential([
        sometimes(iaa.Fliplr(0.5)),
        # sometimes(iaa.Add((-10, 10), per_channel=0.5)),
        # sometimes(iaa.Grayscale(alpha=(0.0, 1.0)))
    ])

    for image in images:
        # Load the image
        img = cv2.imread(os.path.join(folder_path, image))

        # Apply the augmentations
        augmented_img = augmentations.augment_image(img)

        # Save the augmented image
        cv2.imwrite(os.path.join(folder_path, image), augmented_img)

        # Remove the original image
        # os.remove(os.path.join(folder_path, image))

        print ("Augmented image: " + image)

augment_images("videos/scissors 3-moviepy")
