from django.shortcuts import render, redirect
from signup.models import *
import hashlib
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    if not 'user_id' in request.session.keys():
        return redirect('')
    return render(request,'main/index.html')

def loginView(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    return render(request, 'main/login.html')

def login(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    user_input_id = request.POST['loginEmail']
    user_input_pw = request.POST['loginPW']
    try:
        user = User.objects.get(user_id = user_input_id)
        encoded_userPW = user_input_pw.encode()
        encrypted_userPW = hashlib.sha256(encoded_userPW).hexdigest()

        if encrypted_userPW == user.user_pw:
            request.session['user_id'] = user.user_id
            request.session['user_name'] = user.user_name
            return redirect('main_index')
        else:
            return redirect('main_loginView')

    except ObjectDoesNotExist:
        message = '이메일이 존재하지 않습니다.'
        return render(request, 'main/error.html', { "message": message })

    except:
        message = '알 수 없는 오류가 발생하였습니다.'
        return render(request, 'main/error.html', { "message": message })

def logout(request):
    del request.seesion['user_id']
    del request.seesion['user_name']
    return redirect('main_loginView')
    