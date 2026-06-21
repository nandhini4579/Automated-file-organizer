# Automated File Organizer Using Python

## Project Overview

The Automated File Organizer is a Python project that automatically sorts files into different folders based on their file extensions. It helps keep directories organized by moving images, documents, music, videos, and other files into their respective folders.

---

## Features

* Automatically organizes files by type
* Creates folders if they do not exist
* Supports Images, Documents, Music, and Videos
* Moves unknown file types to an "Others" folder
* Simple and easy to use

---

## Technologies Used

* Python 3
* os Module
* shutil Module
* Visual Studio Code (VS Code)

---

## Project Structure

TestFolder/

├── Images/

├── Documents/

├── Music/

├── Videos/

├── Others/

└── file_organizer.py

---

## Installation

### 1. Install Python

Download and install Python from:
https://www.python.org

### 2. Install Visual Studio Code

Download and install VS Code from:
https://code.visualstudio.com

### 3. Install Python Extension

Open VS Code and install the Python extension by Microsoft.

---

## How to Run

### Step 1

Create a folder containing sample files.

Example:

photo.jpg

document.pdf

song.mp3

video.mp4

### Step 2

Open the project folder in VS Code.

### Step 3

Create a file named:

file_organizer.py

### Step 4

Paste the Python code into the file.

### Step 5

Update the source folder path:

source_folder = r"D:\TestFolder"

### Step 6

Open Terminal and run:

python file_organizer.py

or

py file_organizer.py

---

## Expected Output

photo.jpg moved to Images

document.pdf moved to Documents

song.mp3 moved to Music

video.mp4 moved to Videos

File organization completed successfully!

---

## Modules Used

### os

Used for:

* Accessing files and folders
* Creating folder paths
* Listing directory contents

### shutil

Used for:

* Moving files from one folder to another

---

## Advantages

* Saves time
* Reduces manual work
* Keeps files organized
* Easy to maintain large folders

---

## Applications

* Downloads folder management
* Office document organization
* Personal file organization
* Student project management

---

## Future Enhancements

* GUI using Tkinter
* Drag and Drop support
* Automatic scheduling
* Duplicate file detection
* File size-based organization

---






