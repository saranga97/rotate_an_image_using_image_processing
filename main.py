import cv2


def rotate_image(image, angle):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Perform the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image


def main():
    # Read the image
    image = cv2.imread('input_image.jpg')

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Could not open or find the image.")
        return

    # Rotate the image by 45 degrees
    rotated_image_45 = rotate_image(image, 45)

    # Rotate the image by 90 degrees
    rotated_image_90 = rotate_image(image, 90)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image 45 degrees', rotated_image_45)
    cv2.imshow('Rotated Image 90 degrees', rotated_image_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
