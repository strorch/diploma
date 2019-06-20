from django.shortcuts import render
import time
from .Algorythms.FileWorker import FileWorker


def index(request):
    files = FileWorker.getDirsToCalc()
    data = {
        'time': time.time(),
        'files': files,
    }
    return render(request, "base.html", context=data)


def imageInfo(request):

    folderName = request.GET['folder']

    arr_images_names = FileWorker.mainWork(folderName)

    files = FileWorker.getDirsToCalc()

    data = {
        'time': time.time(),
        'names': arr_images_names,
        'files': files,
        'kek': request.GET,
    }

    return render(request, "base.html", context=data)
