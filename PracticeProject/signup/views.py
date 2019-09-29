from django.shortcuts import render, redirect
import hashlib
from .models import *
from django.db import IntegrityError
from random import *
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def signupView(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    return render(request, 'signup/signup.html')

def email(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    user_name = request.POST['signupName']
    user_id = request.POST['signupEmail']
    user_pw = request.POST['signupPW']

    # 이름/이메일의 길이 초과시
    if len(user_id) >= 200:
        message = '입력하신 이메일이 너무 길어요.'
        return render(request, 'main/error.html', { "message": message })
    if len(user_name) >= 30:
        message = '입력하신 이름이 너무 길어요.'
        return render(request, 'main/error.html', { "message": message })

    try:
        #PW 암호화
        encoded_userPW = user_pw.encode()
        encrypted_userPW = hashlib.sha256(encoded_userPW).hexdigest()

        new_user = User(user_id = user_id, user_name = user_name, user_pw = encrypted_userPW)
        new_user.save()
        code = randint(1000, 9999)
        content = {'verifyCode':code}
        msg_html = render_to_string('signup/email_format.html',content)
        msg = EmailMessage(subject="인증코드 발송 메일",body=msg_html,from_email="djangoemailtester001@gmail.com",bcc=[user_id])
        msg.content_subtype='html'
        msg.send()
        request.session['code'] = code
        request.session['user_id'] = user_id
        return redirect('signup_verifyView')

    #중복된 이메일로 가입 시
    except IntegrityError:
        message = '이미 존재하는 이메일입니다.'
        return render(request, 'main/error.html', { "message": message })
            
    #알 수 없는 오류 발생 시
    except:
        message = '알 수 없는 오류가 발생하였습니다.'
        return render(request, 'main/error.html', { "message": message })

def verifyView(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    return render(request, 'signup/verifyCode.html')

def verify(request):
    if 'user_id' in request.session.keys():
        return redirect('main_index')
    user_code = request.POST['verifyCode']
    session_code = request.session['code']
    if user_code == str(session_code):
        user = User.objects.get(user_id = request.session['user_id'])
        user.validation = 1
        user.save()
        del request.session['code']
        del request.session['user_id']
        return redirect('/')
    else:
        return redirect('signup_verifyView')
