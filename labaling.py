import os
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
# Ensure pillow-heif is installed for handling HEIC files
try:
    import pillow_heif
except ImportError:
    raise ImportError("Please install the pillow-heif package to handle HEIC images: pip install pillow-heif")
# Set the path to your images directory, output directory, and labels file
images_dir = "C:\\Users\\HP\\Desktop\\project\\good\\good-soyaseed\\GoodSeed"
output_folder = "C:\\Users\\HP\\Desktop\\project\\goodlabel"
labels_file = "C:\\Users\\HP\\Desktop\\project\\goodsoyaseedlabel.txt"
os.makedirs(output_folder, exist_ok=True)
def label_image(image_path, label, output_path):
    # Check if the image is in HEIC format and convert if necessary
    if image_path.lower().endswith(".heic"):
        heif_image = pillow_heif.read_heif(image_path)
        image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # Convert PIL image to cv2 BGR format
    else:
        # Load the image with cv2
        image = cv2.imread(image_path)
    
    if image is None:
        print(f"Failed to load image {image_path}")
        return
    
    # Set font and location for the label
    font = cv2.FONT_HERSHEY_SIMPLEX
    location = (10, 30)  # Starting position of the text
    font_scale = 1
    color = (255, 255, 255)  # White text
    thickness = 2
    
    # Put the label on the image
    labeled_image = cv2.putText(image, label, location, font, font_scale, color, thickness)
    
    # Save the labeled image
    cv2.imwrite(output_path, labeled_image)
    print(f"Labeled image saved at {output_path}")
def label_all_images_with_goodsoyaseed(images_dir, labels_file, output_folder):
    # List all image files in the directory, including HEIC files
    image_files = [f for f in os.listdir(images_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".heic"))]
    
    if not image_files:
        print("No image files found in the specified directory.")
        return

    # Show the first image as a sample
    sample_image_path = os.path.join(images_dir, image_files[0])

    # Check if sample image is HEIC format
    if sample_image_path.lower().endswith(".heic"):
        heif_image = pillow_heif.read_heif(sample_image_path)
        img = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
    else:
        img = Image.open(sample_image_path)
    
    # Display the sample image
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    
    # Set the label as 'goodsoyaseed'
    label = "goodsoyaseed"
    
    # Write the label with numbering to each image and save in output folder, and log it in the labels file
    with open(labels_file, "w") as f:
        for i, filename in enumerate(image_files, start=1):
            image_path = os.path.join(images_dir, filename)
            new_filename = f"{label}_{i}{os.path.splitext(filename)[1]}"
            output_path = os.path.join(output_folder, new_filename)
            
            # Append the number to the label
            numbered_label = f"{label} {i}"
            
            # Label the image and save
            label_image(image_path, numbered_label, output_path)
            
            # Write the new filename and numbered label to the file
            f.write(f"{new_filename},{numbered_label}\n")
    
    print(f"All images in '{images_dir}' labeled with '{label}' and saved to '{output_folder}' with 'goodsoyaseed' prefix and numbering.")
# Run the function to label all images with the "goodsoyaseed" prefix
label_all_images_with_goodsoyaseed(images_dir, labels_file, output_folder)

# Note: This line seems unrelated to the image labeling code above
# cnn.fit(x=training_set, validation_data=test_set, epochs=25)