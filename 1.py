# import os

# # Define the directory path
# dir_path = 'steel_seg_all/images/test'

# # Get a list of all .txt files in the directory
# txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

# # Process each file
# for file_name in txt_files:
#     # Define the full file path
#     file_path = os.path.join(dir_path, file_name)
    
#     # Read the content of the file
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
    
#     # Modify the first number in each line
#     modified_lines = [f'1{line[1:]}' if line.startswith('0') else line for line in lines]
    
#     # Write the modified content back to the file
#     with open(file_path, 'w') as file:
#         file.writelines(modified_lines)
    
#     # Rename the file itself if it starts with '0'
#     if file_name.startswith('0'):
#         new_file_name = f'1{file_name[1:]}'  # Change the first digit to '1'
#         new_file_path = os.path.join(dir_path, new_file_name)
#         os.rename(file_path, new_file_path)

# # List the modified files to confirm changes
# modified_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]
# modified_files

import os

# Define the directory path
dir_path = 'steel_seg_all/images/test'

# Get a list of all .jpg files in the directory
jpg_files = [f for f in os.listdir(dir_path) if f.endswith('.jpg')]

# Process each file
for file_name in jpg_files:
    # Check if the file name starts with '0'
    if file_name.startswith('0'):
        # Define the new file name
        new_file_name = f'1{file_name[1:]}'  # Change the first digit to '1'
        new_file_path = os.path.join(dir_path, new_file_name)
        
        # Rename the file
        os.rename(os.path.join(dir_path, file_name), new_file_path)

# List the renamed files to confirm changes
renamed_files = [f for f in os.listdir(dir_path) if f.endswith('.jpg')]
renamed_files
