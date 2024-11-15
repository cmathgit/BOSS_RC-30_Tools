# gen_dir_mv_wav_files.py
# This script will generate a directory for each .wav file in the specified directory and move the .wav file into the newly created folder.
# this is useful for organizing .wav files into folders based on their names for import into the BOSS RC-30 Loop Station.
# Programmer: Cruz Macias

import os
import shutil

def organize_wav_files(directory):
    # Open the track_sources.txt file in append mode
    with open('track_sources.txt', 'a') as log_file:
        # List all files in the specified directory
        for file_name in os.listdir(directory):
            # Check if the file has a .wav extension
            if file_name.endswith('.wav'):
                # Create the folder name by stripping the .wav extension
                folder_name = os.path.splitext(file_name)[0]

                # Create the folder path with ROLAND/WAVE subdirectories
                folder_path = os.path.join('ROLAND', 'WAVE', folder_name)
                
                # Create the folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)
                
                # Move the .wav file into the newly created folder
                file_path = os.path.join(directory, file_name)
                new_file_path = os.path.join(folder_path, file_name)
                shutil.move(file_path, new_file_path)
                
                # Create the output message
                message = f"Moved '{file_name}' to '{folder_path}'"
                print(message)
                log_file.write(message + '\n')

# Specify the directory where your .wav files are located
# files will be moved to ROLAND/WAVE/ folder located in the same directory as this script
directory = 'renamed_tracks'
organize_wav_files(directory)
