import argparse
import os
import pathlib

import cv2

# Getting user arguments
ag = argparse.ArgumentParser(
    prog='ImageSplitter',
    description='This script will split an image or batch of into quadrants.',
    epilog='For more information see secdev.info/projects/ImageSplitter.php'
)

ag.add_argument("-i", "--image", required=True, type=str,
                help="Path to the image file or directory.")
ag.add_argument("-o", "--output", required=True, type=str,
                help="Path to the output directory.")
ag.add_argument("-l", "--lap", required=False, type=int, default=150,
                help="This is the number of px the images should overlap.")
ag.add_argument("-g", "--graphical", required=False, type=bool,
                help="This enables or disables the graphical features.")
ag.add_argument("-b", "--batch", required=False, type=bool,
                help="This allows for batch processing of images.")

args = vars(ag.parse_args())


def split_image(x, y, quarterX, quarterY, image, output_dir):
    print("Splitting image...")
    roi1 = image[0:(quarterY + args["lap"]), 0:(quarterX + args["lap"])]  # top left crop
    roi2 = image[0:(quarterY + args["lap"]), (quarterX - args["lap"]):x]  # top right crop
    roi3 = image[(quarterY - args["lap"]):y, (quarterX - args["lap"]):x]  # bottom right crop
    roi4 = image[(quarterY - args["lap"]):y, 0:(quarterX + args["lap"])]  # bottom left crop
    print("Splitting complete.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print("Saving images...")
    cv2.imwrite(os.path.join(output_dir, "ROI1.jpg"), roi1)
    cv2.imwrite(os.path.join(output_dir, "ROI2.jpg"), roi2)
    cv2.imwrite(os.path.join(output_dir, "ROI3.jpg"), roi3)
    cv2.imwrite(os.path.join(output_dir, "ROI4.jpg"), roi4)
    print("Saving complete.")


def show_split(x, y, quarterX, quarterY, image):
    image2 = image.copy()

    cv2.rectangle(image2, (0, 0), ((quarterX + args["lap"]), (quarterY + args["lap"])), (255, 0, 255),
                  2)  # top left
    cv2.rectangle(image2, ((quarterX - args["lap"]), 0), (x, (quarterY + args["lap"])), (0, 255, 0),
                  2)  # top right
    cv2.rectangle(image2, ((quarterX - args["lap"]), (quarterY - args["lap"])), (x, y), (0, 0, 255),
                  2)  # bottom right
    cv2.rectangle(image2, (0, (quarterY - args["lap"])), ((quarterX + args["lap"]), y), (255, 255, 0),
                  2)  # bottom left

    cv2.imshow("Crop areas.", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def loading_calculating(image_path):
    print("Loading Image...")
    # Loading Image
    image = cv2.imread(image_path)
    print("Image Loaded.")
    # Getting image dimensions
    y, x = image.shape[:2]

    # Calculating coordinates for image quarters
    quarterX = x // 2
    quarterY = y // 2

    return x, y, quarterX, quarterY, image


def main():
    if args["batch"]:
        input_dir = pathlib.Path(args["image"])
        output_parent_dir = pathlib.Path(args["output"])

        if not output_parent_dir.exists():
            output_parent_dir.mkdir()

        # Process each image in the directory
        for file_path in input_dir.glob("*.jpg"):
            if file_path.is_file():
                filename = file_path.stem
                output_dir = output_parent_dir / filename

                x, y, quarterX, quarterY, image = loading_calculating(str(file_path))

                if args["graphical"]:
                    show_split(x, y, quarterX, quarterY, image)

                split_image(x, y, quarterX, quarterY, image, str(output_dir))

    else:
        x, y, quarterX, quarterY, image = loading_calculating(args["image"])

        if args["graphical"]:
            show_split(x, y, quarterX, quarterY, image)

        split_image(x, y, quarterX, quarterY, image, args["output"])


if __name__ == "__main__":
    main()
