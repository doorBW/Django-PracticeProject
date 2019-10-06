from django.shortcuts import render, redirect
from datetime import datetime
from .models import * 
from signup.models import *

# Create your views here.
def fileView(request):
    return render(request, 'upload/uploadFile.html')

def uploadFile(request):
    try:
        user_file = request.FILES['fileInput']
        origin_file_name = user_file.name
        user_id = request.session['user_id']
        now_HMS = datetime.today().strftime('%H%M%S')
        file_upload_name = now_HMS+'_'+origin_file_name
        user_file.name = file_upload_name
        user = User.objects.get(user_id=user_id)
        document = Document(file_path=user_file, file_name=origin_file_name, user_id=user)
        document.save()
    except:
        message = '알 수 없는 오류가 발생하였습니다.'
        return render(request, 'main/error.html', { "message": message })

    return redirect('/index/')
