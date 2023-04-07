import os

# Set the folder path containing the YOLOv5 .txt annotation files
folder_path = "C:/Users/Joshua/Documents/vig-proj/SADI-Yolov5-Lite/datasets/test/labels"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a YOLOv5 .txt annotation file
    if filename.endswith(".txt"):
        # Read the contents of the file into a list
        with open(os.path.join(folder_path, filename), "r") as file:
            lines = file.readlines()

        # Remove any empty strings and strip whitespace from the end of each line
        lines = [line.rstrip() for line in lines if line.strip()]

        # Join the lines back into a string using the newline character "\n"
        contents = "\n".join(lines)

        # Write the modified contents back to the file
        with open(os.path.join(folder_path, filename), "w") as file:
            file.write(contents)
