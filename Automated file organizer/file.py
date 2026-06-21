import os
import shutil

# Folder to organize
source_folder = r"C:\Users\HP\OneDrive\Desktop\TestFolder"

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"]
}

# Create folders and move files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination_folder = os.path.join(source_folder, folder_name)

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, file)
                )

                print(f"{file} moved to {folder_name}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            print(f"{file} moved to Others")

print("\nFile organization completed successfully!")