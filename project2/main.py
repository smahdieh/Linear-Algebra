from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """
    newimg = np.zeros_like(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            a = np.empty((3 , 1) , int)
            xyz_3d = np.empty((3 , 1) , int)
            a = [i , j , 1]
            xyz_3d = transform_matrix.dot(a)
            xy_2d = [ int(xyz_3d[0] / xyz_3d[2]) , int(xyz_3d[1] / xyz_3d[2]) ]
            if(xy_2d[0] < output_width and xy_2d[1] < output_height):
                newimg[xy_2d[0] , xy_2d[1] , :] = img[i , j , :]
    return newimg[:output_width, :output_height, :]


def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    A = [0.2989 , 0.5870 , 0.1140]
    T = np.array([A , A , A])
    return Filter(img , T)


def crazyFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    TRed = [0 , 1, 1]
    TGreen = [1 , 0 , 0]
    TBlue = [0 , 0 , 0]
    T = np.array([TRed , TGreen , TBlue])
    return Filter(img , T)


def customFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    TRed = [1 , 2, 3]
    TGreen = [1 , 1 , 1]
    TBlue = [0 , 1 , 0]
    T = np.array([TRed , TGreen , TBlue])
    showImage(Filter(img , T), title="User Filter")
    showImage(Filter(Filter(img , T) , np.linalg.inv(T)), title="Inverted User Filter")
    pass

    


def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    oldwidth , oldheight = img.shape[0] , img.shape[1]
    newwidth , newheight = oldwidth * scale_width, oldheight * scale_height
    newimg = np.zeros((newwidth , newheight , 3))
    for i in range(newwidth):
        for j in range(newheight):
            newimg[i , j , :] = img[int(i * (oldwidth / newwidth)) , int(j * (oldheight / newheight)) , :]

    return newimg


def cropImg(img, start_row, end_row, start_column, end_column):
    """
    TODO : Complete this part based on the description in the manual!
    """
    return img[start_column:end_column, start_row:end_row, :]


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[107, 215], [375, 179], [161, 644], [496, 572]])
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

