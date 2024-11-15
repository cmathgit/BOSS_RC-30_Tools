# BOSS RC-30 Loop Station Utility Scripts

This repository contains Python scripts to help manage `.wav` files for the **BOSS RC-30 Loop Station**. These scripts simplify renaming, organizing, and preparing `.wav` files for loading into the RC-30, ensuring compatibility with its requirements.

## Table of Contents
1. [Introduction](#introduction)
2. [Scripts Overview](#scripts-overview)
3. [Instructions for File Preparation](#instructions-for-file-preparation)
4. [Connecting the RC-30 to Your Computer](#connecting-the-rc-30-to-your-computer)
5. [Disclaimer](#disclaimer)

---

## Introduction

The **BOSS RC-30 Loop Station** supports playback of `.wav` files in a specific format and folder structure. These utility scripts are designed to:
- Rename `.wav` files to the required format (e.g., `001_1.wav` through `099_1.wav`).
- Organize renamed files into properly structured folders (`001_1`, `002_1`, etc.).
- Clear the RC-30’s `ROLAND` folder in preparation for a new batch of tracks.

### Compatible File Requirements:
- **Format**: `.wav`
- **Bit Rate**: 16-bit linear, stereo
- **Sampling Frequency**: 44.1 kHz
- **Maximum File Size**: 1.7 GB (combined total of all files)
- **Maximum Total Time**: Approximately 3 hours
- **Minimum Time**: 1.5 seconds

---

## Scripts Overview

### 1. `rename_wav_files.py`
- **Purpose**: Renames `.wav` files to the format `001_1.wav` through `099_1.wav`.
- **Key Features**:
  - Skips files already named in the correct format.
  - Stops renaming once `099_1.wav` is reached.
  - Appends the track number to the end of the original filenames to preserve them.

### 2. `gen_dir_mv_wav_files.py`
- **Purpose**: Organizes renamed `.wav` files into folders corresponding to their names (e.g., `001_1`).
- **Key Features**:
  - Creates folders such as `001_1`, `002_1`, etc.
  - Moves each `.wav` file to its respective folder.

### 3. `clean_wav_files.py`
- **Purpose**: Clears all `.wav` files from the RC-30’s `ROLAND` folder while leaving the folder structure intact.
- **Key Features**:
  - Removes `.wav` files from subfolders within the `ROLAND` directory.
  - Ensures a clean slate for the next batch of tracks.

### 4. `convert_audio_CODEC.py`
- **Purpose**: Converts `.wav` and `.mp3` files to the required format for the BOSS RC-30 Loop Station.
- **Key Features**:
  - Converts files to `.wav` format.
  - Appends `_converted` to the original filename.

---

## Instructions for File Preparation

### Step 1: Convert `.wav` Files to the Correct Format
Ensure all `.wav` files meet the RC-30’s requirements:
- Use audio editing software to convert files if needed (e.g., Audacity).
- Verify the following:
  - File format is `.wav`.
  - Bit rate is 16-bit linear, stereo.
  - Sampling frequency is 44.1 kHz.

### Step 2: Rename `.wav` Files
Run the `rename_wav_files.py` script to rename files to the required format:
1. Place your `.wav` files in a directory.
2. Execute the script with the directory as input.
3. The script renames files to `001_1.wav` through `099_1.wav` and appends the track number to the original filenames.

### Step 3: Generate Folders and Move Files
Run the `gen_dir_mv_wav_files.py` script:
1. Place the renamed `.wav` files in a directory.
2. Execute the script.
3. The script creates folders (`001_1`, `002_1`, etc.) and moves each file to its corresponding folder.

### Step 4: Clear the RC-30’s Folder
Before transferring new files, clear the RC-30’s `ROLAND` folder:
1. Connect the RC-30 to your computer (see instructions below).
2. Run the `clean_wav_files.py` script to remove existing `.wav` files while keeping the folder structure intact.

---

## Connecting the RC-30 to Your Computer

### Steps to Connect
1. **Power On**:
   - Turn on the RC-30 by inserting a plug into the OUTPUT L jack.
   - Note: The RC-30 will not operate on USB bus power. Use an AC adaptor to ensure stability.

2. **USB Connection**:
   - Use a commercially available USB cable to connect the RC-30’s USB connector to your computer’s USB 2.0 port.
   - Ensure the RC-30 is stopped and all phrases are saved before connecting.

3. **Access the RC-30’s Drive**:
   - Windows: Open "BOSS_RC30" (or "Removable Disk") under My Computer (or This PC).
   - Mac: Open the "BOSS_RC-30" icon on your desktop.

4. **Transfer Files**:
   - Copy `.wav` files into their respective folders (`001_1`, `002_1`, etc.) in the `ROLAND/WAVE` directory.
   - Do not overwrite existing `.wav` files in any folder.

5. **Safely Disconnect**:
   - Windows: Use the "Safely Remove Hardware" option in the system tray.
   - Mac: Right-click the USB drive icon and select "Eject."
   - Press the RC-30’s [RHYTHM ON/OFF] button to return to normal operation.
   - Disconnect the USB cable.

---

## Disclaimer

These scripts are provided as a convenience tool for managing `.wav` files compatible with the **BOSS RC-30 Loop Station**. Proper use is essential to avoid data loss. Always back up your data before transferring

## Audio Conversion Script

### Overview
This Python script is designed to convert `.wav` and `.mp3` files into a format compatible with devices like the **BOSS RC-30 Loop Station**. It ensures that audio files meet the following specifications:

- **Format**: WAV
- **Bit Rate**: 16-bit linear, stereo
- **Sampling Frequency**: 44.1 kHz
- **File Size**: Maximum of 1.7 GB
- **Total Duration**: Approximately 3 hours (total across all files)
- **Minimum Duration**: 1.5 seconds

### Features
- **File Compatibility**: Supports `.wav` and `.mp3` input formats.
- **Audio Processing**: Converts files to the required specifications, including frame rate, channel count, and bit depth.
- **Output Management**: Saves converted files in a designated output directory, appending `_converted` to the original file name.

### Alternative: Using VLC Media Player for Conversion
If you prefer not to use Python or need a graphical user interface, **VLC Media Player** can also be used to convert audio files to the required format. VLC is free, widely available, and capable of handling the necessary adjustments.

### Usage Instructions

#### Prerequisites
1. **Install Python Dependencies**:  
   This script requires the `pydub` library and `ffmpeg`:
   ```bash
   pip install pydub
