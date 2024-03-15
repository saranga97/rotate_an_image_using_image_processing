import cv2


def rotate_image(image, angle):

    height, width = image.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image


def main():

    image = cv2.imread('input_image.jpg')

    if image is None:
        print("Error: Could not open or find the image.")
        return

    rotated_image_45 = rotate_image(image, 45)

    rotated_image_90 = rotate_image(image, 90)

    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image 45 degrees', rotated_image_45)
    cv2.imshow('Rotated Image 90 degrees', rotated_image_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
