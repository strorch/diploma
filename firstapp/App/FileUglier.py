from copy import copy
from .ImageWorker import Image
from .ImageTranformation import ImageTransformation
from .FileWorker import FileWorker


class FileUglier(object):

    def __init__(self, imageName):
        self._imageName = imageName

    def GetUgly(self):
        return {
            'affine': ImageTransformation.Affine,
            'resize': ImageTransformation.Resize,
            'perspective': ImageTransformation.Perspective,
            'rotate': ImageTransformation.Rotate,
            'gaussian': ImageTransformation.Gaussian,
            'light_gaussian': ImageTransformation.LightGaussian,
            'brightness': ImageTransformation.Brightness,
            'light_brightness': ImageTransformation.LightBrightness,
        }

    @staticmethod
    def CreateFileEnv(name):
        path = '%s/%s/' % (FileWorker.startPath(), name)
        FileWorker.CreateDir(path)
        return path

    def startProcess(self):
        im_name = self._imageName
        splitted_name = im_name.split('/')[2]
        ext_file = splitted_name.split('.')[1]
        env_path = FileUglier.CreateFileEnv(splitted_name)
        img = Image(im_name[1:])
        img.Load()
        img.Save(env_path+splitted_name)
        ugles = self.GetUgly()
        for func in ugles:
            tmp = copy(img)
            transformed = ugles[func](tmp.image)
            tmp.image = transformed
            file_name_res = env_path + func + '.' + ext_file
            tmp.Save(file_name_res)
        FileWorker.RemoveDir('media')
