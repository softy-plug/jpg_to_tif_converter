import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        tiff_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".tiff")
        im.save(tiff_path, format="TIFF", quality=100)

def main():
    print("Welcome to JPG to TIFF Converter!")
    jpg_folder = input("Enter the path to the folder containing JPG images: ")
    while not os.path.exists(jpg_folder):
        jpg_folder = input("The folder doesn't exist. Please enter a valid path to the JPG folder: ")
    tiff_folder = input("Enter the path to the folder where converted TIFF images will be saved: ")
    while not os.path.exists(tiff_folder):
        tiff_folder = input("The folder doesn't exist. Please enter a valid path to the TIFF folder: ")
    # Create the TIFF folder if it doesn't exist yet
    if not os.path.exists(tiff_folder):
        os.makedirs(tiff_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, tiff_folder)
    print("All images converted successfully to TIFF format and saved in the chosen folder!")


if __name__ == "__main__":
    main()

# softy_plug