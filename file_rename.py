import os

directory = 'C:/Users/jeric/Downloads/Compressed/WiderPerson/Annotations'

for filename in os.listdir(directory):
    if filename.endswith('.jpg.txt'):
        new_filename = filename.replace('.jpg.txt', '.txt')
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
