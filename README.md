# BOSS RC-30 Loop Station Utility Scripts

This repository contains Python scripts to help manage `.wav` files for the **BOSS RC-30 Loop Station**. These scripts simplify renaming, organizing, and preparing `.wav` files for loading into the RC-30, ensuring compatibility with its requirements.

## Table of Contents
1. [Introduction](#introduction)
2. [Scripts Overview](#scripts-overview)
3. [Instructions for File Preparation](#instructions-for-file-preparation)
4. [Connecting the RC-30 to Your Computer](#connecting-the-rc-30-to-your-computer)
5. [Disclaimer](#disclaimer)

## LLM Code Generation Notice

Portions of this codebase were generated or refined using large language models (LLMs) including models such as Gemini, ChatGPT, Claude, DeepSeek, Qwen, Dolphin-Llama, and more, integrated API Plugins Such as Cline, Continue, Roo Code, and more, and Service Providers such as OpenRouter, Ollama, HuggingFace, Cursor, and GitHub Copilot and more. Final code was reviewed and adapted by the project maintainer. Use at your own risk.

# Limitation of Liability Statement

For a complete Limitation of Liability Statement, please visit my [website](https://crossofthemessiah.w3spaces.com/).

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

# How to Clear BOSS RC-30
## Before proceeding, copy entire "ROLAND" folder on RC-30 to backup drive
## 1. In the BOSS RC-30 drive, delete the "ROLAND" folder
### -backup "ROLAND" to another drive to prevent data loss
## 2. Copy entire "ROLAND" folder (empty phrases) in pwd to the BOSS RC-30 drive. 
### -All tracks are now clear
## Folder Structure
``` plaintext
BOSS_RC_30/
└── ROLAND/
    └── WAVE/
```

# How to Load Phrases into BOSS RC-30
## 1. Same as step 1 above
## 2. Copy .wav files from computer drive into the respective folder on BOSS RC-30 drive, e.g., copy 001_1.wav and 001_2.wav files into /001_1/ and /001_2/ folders, repspectively, and so on, that is, up to 099_1.wav and 099_2.wav into /099_1/ and /099_2/, repspectively.
## Folder Structure
``` plaintext
BOSS_RC_30/
└── ROLAND/
    └── WAVE/
        ├── 001_1/
        │   └── 001_1.WAV
        ├── 001_2/
        │   └── 001_2.WAV
        ├── 002_1/
        │   └── 002_1.WAV
        ├── 002_2/
        │   └── 002_2.WAV
        └── ...
        ├── 099_1/
        │   └── 099_1.WAV
        └── 099_2/
            └── 099_2.WAV

```
### All files must be .wav data format, 16-bit linear, stereo bitrate, and 44.1kHz sampling frequency
### Option A. Copy each phrase individually. 
### Option B. Compile all phrases into the "ROLAND" folder before hand and copy entire "ROLAND" folder.
## Folder Structure
``` plaintext
BOSS_RC_30/
└── ROLAND/
    └── WAVE/
```