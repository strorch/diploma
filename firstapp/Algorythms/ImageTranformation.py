
class ImageTransformation:
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