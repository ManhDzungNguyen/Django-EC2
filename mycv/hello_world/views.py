from django.shortcuts import render
import os
import mimetypes
from django.http.response import HttpResponse

# Create your views here.
def cv(request):
    return render(request, "index.html", {})

def cv1(request):
    return render(request, "cv1.html", {})

def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = "Resume_AI-Engineer_NguyenManhDung.pdf"
    # Define the full file path
    filepath = BASE_DIR + "/hello_world/Files/" + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response