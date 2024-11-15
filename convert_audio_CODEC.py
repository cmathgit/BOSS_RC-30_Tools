# convert_audio_CODEC.py
# convert audio files to the required format for the BOSS RC-30 Loop Station
# .wav and .mp3 files are converted to .wav files with the same name in the output directory
# Programmer: Cruz Macias

import os
from pydub import AudioSegment

def convert_audio(input_dir, output_dir):
    """
    Converts .wav and .mp3 files in the input directory to the required format and saves them in the output directory.

    Required format:
    - WAV
    - 16-bit linear, stereo
    - Sampling frequency: 44.1 kHz
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if file_name.lower().endswith(('.wav', '.mp3')):
            try:
                print(f"Processing {file_name}...")
                # Load audio file
                audio = AudioSegment.from_file(file_path)

                # Convert to 44.1 kHz, stereo, 16-bit linear
                converted_audio = audio.set_frame_rate(44100).set_channels(2).set_sample_width(2)

                # Output file name
                output_file_name = os.path.splitext(file_name)[0] + "_converted.wav"
                output_file_path = os.path.join(output_dir, output_file_name)

                # Export the converted file
                converted_audio.export(output_file_path, format="wav")
                print(f"Converted and saved: {output_file_path}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    # Specify input and output directories
    input_directory = "my_tracks"
    output_directory = "converted_tracks"

    convert_audio(input_directory, output_directory)
