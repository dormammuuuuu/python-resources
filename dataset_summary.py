import os

# Set the folder path containing the YOLOv5 .txt annotation files
folder_path = "C:/Users/Joshua/Documents/vig-proj/SADI-Yolov5-Lite/datasets/valid/labels"

# Initialize a dictionary to store the index distribution
index_counts = {}

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a YOLOv5 .txt annotation file
    if filename.endswith(".txt"):
        # Open the file for reading
        with open(os.path.join(folder_path, filename), "r") as file:
            # Read each line of the file
            lines = file.readlines()

        # Loop through each line of the file
        for line in lines:
            # Split the line into its components
            components = line.strip().split(" ")

            # Get the index component
            index = components[0]

            # Update the index distribution
            if index in index_counts:
                index_counts[index] += 1
            else:
                index_counts[index] = 1

# Display the index distribution summary
print("Index Distribution Summary:")
for index, count in index_counts.items():
    print(f"Index {index}: {count} annotations")
