# Image Splitter

Image Splitter is a Python script that splits an image or batch of images into quadrants. It provides a simple command-line interface to split images and save the resulting quadrants as separate image files.

## Features

- Split a single image into four quadrants: top-left, top-right, bottom-right, and bottom-left.
- Specify the number of pixels for overlapping between the quadrants.
- Enable or disable graphical display of the split for visual confirmation.
- Process a batch of images in a directory and save the quadrants for each image.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/image-splitter.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-line Arguments

- `-i`, `--image`: Path to the input image file or directory.
- `-o`, `--output`: Path to the output directory to save the split images.
- `-l`, `--lap`: The number of pixels the quadrants should overlap (default is 150).
- `-g`, `--graphical`: Enable or disable graphical display of the split.
- `-b`, `--batch`: Enable batch processing of images in a directory.

### Examples

1. Split a single image:

   ```bash
   python image_splitter.py -i input_image.jpg -o output_directory
   ```

2. Split a single image with graphical display:

   ```bash
   python image_splitter.py -i input_image.jpg -o output_directory -g True
   ```

3. Split a batch of images in a directory:

   ```bash
   python image_splitter.py -i input_directory -o output_directory -b True
   ```

## Documentation

For more information on how to use Image Splitter, check the [Sphinx Documentation](docs/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
