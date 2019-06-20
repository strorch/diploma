import os
from .ImageWorker import ImageWorker


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
    def mainWork(folderName):
        true_files = FileWorker.getDirFiles(folderName)
        staticdir = FileWorker.getStaticPath(folderName)
        FileWorker.CreateDir(staticdir)

        array = []
        for i in range(len(true_files)):
            nature_file_path = FileWorker.getNatureFilePath(folderName, true_files[i])

            worker = ImageWorker(nature_file_path)

            harris = worker.Harris()

            static_file_path = "%s/%s" % (staticdir, true_files[i])
            ImageWorker.SaveImg(static_file_path, harris)

            array.append(static_file_path)
        return list(array)
