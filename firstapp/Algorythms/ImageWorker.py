import cv2
import numpy as np


class ImageWorker(object):

    def __init__(self, filename):
        self.filename = filename

    def Harris(self):
        img = cv2.imread(self.filename)
        img = ImageWorker.ResizeImg(img)
        avarage = ImageWorker.AvarageColor(img)
        # img = ImageWorker.AffineTransorm(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 5, 3, 0.04)

        dst = cv2.dilate(dst, None)

        img[dst > 0.01 * dst.max()] = [0, 0, 255]
        img[dst > 0.05 * dst.max()] = [255, 0, 0]
        img[dst > 0.1 * dst.max()] = [255, 0, 255]
        img = ImageWorker.SetColorToBlack(img, avarage)
        return img

    def ShiTomasi(self):
        img = cv2.imread(self.filename)
        img = ImageWorker.ResizeImg(img)
        avarage = ImageWorker.AvarageColor(img)
        # img = ImageWorker.AffineTransorm(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        corners_blue = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners_red = cv2.goodFeaturesToTrack(gray, 50, 0.05, 20)
        corners_pink = cv2.goodFeaturesToTrack(gray, 75, 0.1, 30)
        corners_blue = np.int0(corners_blue)
        corners_red = np.int0(corners_red)
        corners_pink = np.int0(corners_pink)

        for i in range(len(corners_blue)):
            x, y = corners_blue[i].ravel()
            cv2.circle(img, (x, y), 3, 255, -1)
        img = ImageWorker.SetColorToBlack(img, avarage)
        return img

    @staticmethod
    def ResizeImg(img):
        scale_percent = 90
        while img.shape[1] > 500:
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        return img

    @staticmethod
    def AffineTransorm(img):
        rows, cols, ch = img.shape
        cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
        cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
        cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)
        pts1 = np.float32([[83, 90], [447, 90], [83, 472]])
        pts2 = np.float32([[0, 0], [447, 90], [150, 472]])
        matrix = cv2.getAffineTransform(pts1, pts2)
        return cv2.warpAffine(img, matrix, (cols, rows))

    @staticmethod
    def AvarageColor(img):
        avg_color_per_row = np.average(img, axis=0)
        return np.average(avg_color_per_row, axis=0)

    @staticmethod
    def SetColorToBlack(img, color):
        img[np.where((img == [0,0,0]).all(axis = 2))] = color
        return img

    @staticmethod
    def SaveImg(path, img):
        cv2.imwrite(path, img)
