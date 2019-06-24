import cv2
import numpy as np

from copy import copy
from .ImageTranformation import ImageTransformation


class AbstractMethod(object):

    @staticmethod
    def prepareObj(img_obj, img):
        tmp = img_obj.Copy()
        tmp.image = img
        return tmp

    @staticmethod
    def ImagesConcat():
        image_names = ['original_field_1_0.PNG', 'original_field_1_1.PNG', 'original_field_1_3.PNG',
                       'original_field_1_4.PNG', 'original_field_1_5.PNG']
        images = []
        max_width = 0  # find the max width of all the images
        total_height = 0  # the total height of the images (vertical stacking)

        for name in image_names:
            # open all images and find their sizes
            images.append(cv2.imread(name))
            if images[-1].shape[1] > max_width:
                max_width = images[-1].shape[1]
            total_height += images[-1].shape[0]

        # create a new array with a size large enough to contain all the images
        final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)

        current_y = 0  # keep track of where your current image was last placed in the y coordinate
        for image in images:
            # add an image to the final array and increment the y coordinate
            final_image[current_y:image.shape[0] + current_y, :image.shape[1], :] = image
            current_y += image.shape[0]
        return final_image

    @staticmethod
    def Harris(img_object, start_img_object):
        tmp = copy(img_object)
        img = tmp.image

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 5, 3, 0.04)

        dst = cv2.dilate(dst, None)

        img[dst > 0.01 * dst.max()] = [0, 0, 255]
        img[dst > 0.05 * dst.max()] = [255, 0, 0]
        img[dst > 0.1 * dst.max()] = [255, 0, 255]
        img = ImageTransformation.SetColorToBlack(img)
        tmp.image = img
        return tmp

    @staticmethod
    def ShiTomasi(img_object, start_img_object):
        tmp = copy(img_object)
        img = tmp.image

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        corners_blue = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
        corners_blue = np.int0(corners_blue)

        for i in range(len(corners_blue)):
            x, y = corners_blue[i].ravel()
            cv2.circle(img, (x, y), 3, 255, -1)
        img = ImageTransformation.SetColorToBlack(img)
        tmp.image = img
        return tmp

    @staticmethod
    def BRISK(img_object, start_img_object): # surf orb

        gray1 = cv2.cvtColor(img_object.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(start_img_object.image, cv2.COLOR_BGR2GRAY)

        akaze = cv2.BRISK_create()
        (kps, descs) = akaze.detectAndCompute(gray, None)
        (kps1, descs1) = akaze.detectAndCompute(gray1, None)

        if descs is None or descs1 is None:
            return None
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descs,descs1, k=2)

        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        # cv2.drawMatchesKnn expects list of lists as matches.
        img3 = cv2.drawMatchesKnn(gray,kps,gray1,kps1,good,None,flags=2)
        img_object.image = img3
        return img_object

    @staticmethod
    def AKAZE(img_object, start_img_object): # surf orb

        gray1 = cv2.cvtColor(img_object.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(start_img_object.image, cv2.COLOR_BGR2GRAY)

        akaze = cv2.AKAZE_create()
        (kps, descs) = akaze.detectAndCompute(gray, None)
        (kps1, descs1) = akaze.detectAndCompute(gray1, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descs,descs1, k=2)
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        # cv2.drawMatchesKnn expects list of lists as matches.
        img3 = cv2.drawMatchesKnn(gray,kps,gray1,kps1,good,None,flags=2)
        img_object.image = img3
        return img_object

    @staticmethod
    def ORB(img_object, start_img_object): # surf orb

        gray1 = cv2.cvtColor(img_object.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(start_img_object.image, cv2.COLOR_BGR2GRAY)

        akaze = cv2.ORB_create()
        (kps, descs) = akaze.detectAndCompute(gray, None)
        (kps1, descs1) = akaze.detectAndCompute(gray1, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descs,descs1, k=2)
        # Apply ratio test
        good = []
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
        # cv2.drawMatchesKnn expects list of lists as matches.
        img3 = cv2.drawMatchesKnn(gray,kps,gray1,kps1,good,None,flags=2)
        img_object.image = img3
        return img_object
