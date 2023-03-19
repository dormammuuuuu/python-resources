import os
import shutil

person_folder = 'path/to/person/folder'
cat_folder = 'path/to/cat/folder'
output_folder = 'path/to/output/folder'

for person_image in os.listdir(person_folder):
    if person_image in os.listdir(cat_folder):
        with open(os.path.join(person_folder, person_image.replace('.jpg', '.txt'))) as person_file:
            person_annotation = person_file.read().splitlines()
        with open(os.path.join(cat_folder, person_image.replace('.jpg', '.txt'))) as cat_file:
            cat_annotation = cat_file.read().splitlines()

        merged_annotation = person_annotation + cat_annotation

        with open(os.path.join(output_folder, person_image.replace('.jpg', '.txt')), 'w') as outfile:
            outfile.write('\n'.join(merged_annotation))

    else:
        shutil.move(os.path.join(person_folder, person_image), os.path.join(output_folder, person_image))
        with open(os.path.join(output_folder, person_image.replace('.jpg', '.txt')), 'w') as outfile:
            outfile.write('')
