import cv2
import numpy as np


class Image(object):

    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def SetupImage(self):
        self.image = cv2.imread(self.filename)

    def Harris(self):
        img = self.image.Copy()
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
        img = self.image.Copy()
        img = ImageWorker.ResizeImg(img)
        avarage = ImageWorker.AvarageColor(img)
        # img = ImageWorker.AffineTransorm(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        corners_blue = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners_blue = np.int0(corners_blue)

        for i in range(len(corners_blue)):
            x, y = corners_blue[i].ravel()
            cv2.circle(img, (x, y), 3, 255, -1)
        img = ImageWorker.SetColorToBlack(img, avarage)
        return img

    def OtherPoints(self):
        minHessian = 400
        detector = cv.xfeatures2d_SURF.create(hessianThreshold=minHessian)
        keypoints = detector.detect(src)

        # -- Draw keypoints
        img_keypoints = np.empty((src.shape[0], src.shape[1], 3), dtype=np.uint8)
        cv.drawKeypoints(src, keypoints, img_keypoints)
        return img_keypoints

    def Save(self, path):
        cv2.imwrite(path, self.image)
