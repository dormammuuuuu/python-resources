import os

# Set the folder path containing the YOLOv5 .txt annotation files
folder_path = "C:/Users/Joshua/Documents/vig-proj/SADI-Yolov5-Lite/datasets/test/labels"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a YOLOv5 .txt annotation file
    if filename.endswith(".txt"):
        # Read the contents of the file
        with open(os.path.join(folder_path, filename), "r") as file:
            contents = file.read().replace("/n", "\r\n")

        # Write the modified contents back to the file
        with open(os.path.join(folder_path, filename), "w") as file:
            file.write(contents)
