import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .App.FileWorker import FileWorker


def index(request):
    files = FileWorker.getDirsToCalc()
    data = {
        'time': time.time(),
        'files': files,
        'kek': request.GET,
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
    if request.method != 'POST':
        return render(request, 'pages/500.html', {})
    myfile = request.FILES['document']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)

    data = {
        'time': time.time(),
        # 'names': arr_images_names,
        # 'files': files,
        'kek': '1111',
    }
    return render(request, 'base.html', {
        # 'uploaded_file_url': uploaded_file_url,
        'context': data,
    })


def tmp_ajax(request):
    return {
        'kek': request.POST
    }
