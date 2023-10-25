from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """
    pass


def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def crazyFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def customFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


def cropImg(img, start_row, end_row, start_column, end_column):
    """
    TODO : Complete this part based on the description in the manual!
    """
    pass


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[?, ?], [?, ?], [?, ?], [?, ?]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")

    customFilter(warpedImage)

    croppedImage = cropImg(warpedImage, 50, 300, 50, 225)
    showImage(croppedImage, title="Cropped Image")

    scaledImage = scaleImg(warpedImage, 2, 3)
    showImage(scaledImage, title="Scaled Image")
