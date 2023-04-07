import os

# Set the folder path containing the YOLOv5 .txt annotation files
folder_path = "C:/Users/Joshua/Documents/vig-proj/SADI-Yolov5-Lite/datasets/valid/labels"

# Set the new index value
new_index = "3"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a YOLOv5 .txt annotation file
    if filename.endswith(".txt"):
        # Open the file for reading
        with open(os.path.join(folder_path, filename), "r") as file:
            # Read each line of the file
            lines = file.readlines()

        # Open the file for writing
        with open(os.path.join(folder_path, filename), "w") as file:
            # Loop through each line of the file
            # Loop through each line of the file
            for line in lines:
                # Split the line into its components
                components = line.strip().split(" ")

                # Check if the first component is "3"
                if components[0] == "bed":
                    # Update the first component with the new value
                    print("Index Found")
                    components[0] = str(new_index)

                # Write the modified line to the file
                file.write(" ".join(components) + "\n")
