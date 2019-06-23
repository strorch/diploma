import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .App.FileWorker import FileWorker
from .App.FileUglier import FileUglier


def index(request):
    success = False
    if request.method == 'GET' and 'success' in request.GET:
        success = True
    files = FileWorker.getDirsToCalc()
    data = {
        'time': time.time(),
        'files': files,
        'kek': request.GET,
        'success': success
    }
    return render(request, "base.html", context=data)


def folderInfo(request):
    folder = request.GET['folder']
    method = request.GET['method']
    arr_images_names = FileWorker.mainWork(folder, method)
    files = FileWorker.getDirsToCalc()
    data = {
        'time': time.time(),
        'names': arr_images_names,
        'files': files,
        'kek': request.GET,
    }
    return render(request, "base.html", context=data)


def imageInfo(request):
    if request.method != 'POST' or len(list(request.FILES)) == 0:
        return redirect('/')
    myfile = request.FILES['document']
    fs = FileSystemStorage()
    file = fs.save(myfile.name, myfile)
    url = fs.url(file)
    uglier = FileUglier(url)
    uglier.startProcess()
    return redirect('/?success=' + url)
