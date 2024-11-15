# clean_wav_files.py
# This script will remove all .wav files in the specified directory.
# Programmer: Cruz Macias

import os

def clean_wav_files(directory):
    # Loop through each folder in the specified directory
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        # Check if it's a directory (skip files if any)
        if os.path.isdir(folder_path):
            # Loop through each file in the folder
            for file_name in os.listdir(folder_path):
                # Check if the file is a .wav file
                if file_name.endswith('.wav'):
                    # Construct the full file path
                    file_path = os.path.join(folder_path, file_name)
                    
                    # Remove the .wav file
                    os.remove(file_path)
                    print(f"Removed '{file_path}'")

# Specify the directory containing the folders
directory = 'ROLAND/WAVE'
clean_wav_files(directory)
