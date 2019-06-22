import cv2


class Image(object):

    def __init__(self, filename):
        self.filename = filename
        self.image = None

    def Load(self):
        self.image = cv2.imread(self.filename)

    def Save(self, path):
        cv2.imwrite(path, self.image)
