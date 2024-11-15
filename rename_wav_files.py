# rename_wav_files.py
# This script will rename .wav files in the specified directory to the next available track number.
# Programmer: Cruz Macias
import os
import shutil

def rename_and_copy_wav_files(directory):
    # Create renamed_tracks directory if it doesn't exist
    renamed_dir = os.path.join(os.path.dirname(directory), 'renamed_tracks')
    os.makedirs(renamed_dir, exist_ok=True)
    
    # Create/open log file
    log_file_path = os.path.join(os.path.dirname(directory), 'track_sources.txt')
    print(f"Creating log file at: {log_file_path}")  # Debug print
    
    with open(log_file_path, 'w') as log_file:
        log_file.write("Track Renaming Log\n")
        log_file.write("=================\n\n")
        
        # Generate a list of available track numbers (only _1 pattern for renaming)
        available_tracks = [f"{str(i).zfill(3)}_1.wav" for i in range(1, 100)]
        
        # First, copy any existing correctly named files (_1 and _2 patterns)
        for file_name in os.listdir(directory):
            # Check for _1.wav pattern
            if file_name in available_tracks:
                src_path = os.path.join(directory, file_name)
                dst_path = os.path.join(renamed_dir, file_name)
                shutil.copy(src_path, dst_path)
                log_message = f"Copied existing file: {file_name} (preserved original name)\n"
                print(log_message.rstrip())
                log_file.write(log_message)
                available_tracks.remove(file_name)
            # Check for _2.wav pattern
            # elif (file_name.endswith('_2.wav') and len(file_name) == 8 and file_name[:3].isdigit()):
            elif (file_name.endswith('_2.wav')):
                src_path = os.path.join(directory, file_name)
                dst_path = os.path.join(renamed_dir, file_name)
                shutil.copy(src_path, dst_path)
                log_message = f"Copied existing file: {file_name} (preserved original name)\n"
                print(log_message.rstrip())
                log_file.write(log_message)

        # Sort the remaining available tracks
        available_tracks.sort()
        
        # Counter to keep track of renaming progress
        copied_count = 0

        # Loop through files in the directory
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            # Skip directories and non-wav files
            if not os.path.isfile(file_path) or not file_name.endswith('.wav'):
                continue

            # Skip files already in the correct format (both _1 and _2 patterns)
            #if (file_name in available_tracks or (file_name.endswith('_2.wav') and len(file_name) == 8 and file_name[:3].isdigit())):
            if (file_name in available_tracks or file_name.endswith('_2.wav') or file_name.endswith('_1.wav')):
                continue

            # If no more available tracks, stop the process
            if not available_tracks:
                log_message = "Maximum limit of available tracks reached (099_1.wav).\n"
                print(log_message.rstrip())
                log_file.write(log_message)
                break

            # Get the next available track name
            new_name = available_tracks.pop(0)
            new_path = os.path.join(renamed_dir, new_name)

            # Copy the file to renamed_tracks with the new name
            shutil.copy(file_path, new_path)
            log_message = f"Renamed: {file_name} -> {new_name}\n"
            print(log_message.rstrip())
            log_file.write(log_message)
            copied_count += 1

        # Write summary to log
        summary = f"\nProcess complete. Total files copied and renamed: {copied_count}.\n"
        print(summary.rstrip())
        log_file.write(summary)

# Specify the directory containing .wav files
directory = 'converted_tracks'
script_dir = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(script_dir, 'converted_tracks')

# Add debug prints
print(f"Looking for .wav files in: {directory}")
files = os.listdir(directory)
print(f"Files found in directory: {files}")

rename_and_copy_wav_files(directory)
