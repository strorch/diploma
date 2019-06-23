import cv2
import numpy as np

from copy import copy
from scipy.ndimage import gaussian_filter


class ImageTransformation:
    @staticmethod
    def SetColorToBlack(img):
        def AvarageColor():
            avg_color_per_row = np.average(img, axis=0)
            return np.average(avg_color_per_row, axis=0)
        img[np.where((img == [0,0,0]).all(axis = 2))] = AvarageColor()
        return img

    @staticmethod
    def Resize(_img, scale_percent=50):
        img = copy(_img)
        while img.shape[1] > 500:
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        return img

    @staticmethod
    def Affine(img):
        rows, cols, ch = img.shape
        cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
        cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
        cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)
        pts1 = np.float32([[83, 90], [447, 90], [83, 472]])
        pts2 = np.float32([[0, 0], [447, 90], [150, 472]])
        matrix = cv2.getAffineTransform(pts1, pts2)
        return cv2.warpAffine(img, matrix, (cols, rows))

    @staticmethod
    def Perspective(img):
        height, width = img.shape[0], img.shape[1]
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [height, 0], [0, width], [height, width]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (height, width))
        return dst

    @staticmethod
    def Rotate(img):
        rows, cols, some = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
        return cv2.warpAffine(img, M, (cols, rows))

    @staticmethod
    def Gaussian(img):
        a = np.arange(50, step=2).reshape((5, 5))
        gaussian_filter(a, sigma=1)
        result = gaussian_filter(img, sigma=5)
        return result
