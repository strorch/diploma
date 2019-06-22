import os

from .Methods import Methods
from .ImageWorker import Image


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
            harris = method(img)
            static_file_path = "%s/%s" % (staticdir, true_files[i])
            harris.Save(static_file_path)
            array.append(static_file_path)

        return list(array)
