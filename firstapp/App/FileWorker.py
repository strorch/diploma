import os
import shutil

from .Methods import Methods
from .ImageWorker import Image
from .ImageTranformation import ImageTransformation


class FileWorker:

    @staticmethod
    def startPath():
        return 'shi-harris'

    @staticmethod
    def getDirsToCalc():
        startPath = FileWorker.startPath()
        return os.listdir(startPath)

    @staticmethod
    def getStaticPath(folderName):
        return 'static/result_Images/%s' % folderName

    @staticmethod
    def getNaturePath(folderName):
        return '%s/%s' % (FileWorker.startPath(), folderName)

    @staticmethod
    def getNatureFilePath(folderName, filename):
        return '%s/%s' % (FileWorker.getNaturePath(folderName), filename)

    @staticmethod
    def getDirFiles(folderName):
        startPath = FileWorker.getNaturePath(folderName)
        return os.listdir(startPath)

    @staticmethod
    def CreateDir(staticdir):
        try:
            os.mkdir(staticdir)
            print('Dir "%s" successfully created' % staticdir)
        except FileExistsError as e:
            print(e)

    @staticmethod
    def RemoveDir(name):
        try:
            shutil.rmtree(name)
            print('Dir "%s" successfully removed' % name)
        except FileExistsError as e:
            print(e)

    @staticmethod
    def mainWork(folderName, methodName):
        true_files = FileWorker.getDirFiles(folderName)
        staticdir = FileWorker.getStaticPath(folderName)
        method = Methods.getMethod(methodName)
        if method == None:
            raise Exception('No such method')
        FileWorker.CreateDir(staticdir)
        array = []
        for i in range(len(true_files)):
            nature_file_path = FileWorker.getNatureFilePath(folderName, true_files[i])
            img = Image(nature_file_path)
            img.Load()
            resized_img = ImageTransformation.Resize(img.image, 90)
            img.image = resized_img

            startImg = Image(FileWorker.startPath() + '/' + folderName+'/'+folderName)
            startImg.Load()
            resized_img = ImageTransformation.Resize(startImg.image, 90)
            startImg.image = resized_img
            result = method(img, startImg)
            if result is None:
                continue

            static_file_path = "%s/%s" % (staticdir, true_files[i])
            result.Save(static_file_path)
            array.append(static_file_path)
        return list(array)
