from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.core import serializers


# Create your views here.


def home(request):
    print('home')
    return render(request, "login.html")


# def toLogin(request):
#     return render(request,'login.html')
def optional(request):
    u = request.session['u']
    sc_list = SC.objects.all()

    cno_list = []
    for line in SC.objects.all():
        if line.sno.sno == u:
            cno_s = line.cno.cno
            cno_list.append(cno_s)

    cno_all_list = []
    for line in Course.objects.all():
        cno_all_list.append(line.cno)

    course_list = None
    for c in list(set(cno_all_list) - set(cno_list)):
        if course_list:

            course_list = course_list | Course.objects.filter(cno=c)
        else:
            course_list = Course.objects.filter(cno=c)

    # course_list=request.session['course_list']
    return render(request, 'index.html', {'name': u,
                                          'course_list': course_list})


def login(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')
    course_list = Course.objects.all()
    # print(course_list)
    if u and p:
        user = Student.objects.filter(sno=u, password=p).count()
        if user >= 1:
            request.session['u'] = u
            # course_list_json = serializers.serialize("json", course_list)
            # request.session['course_list'] = course_list_json
            # request.session['course_list']=course_list.toDict
            if u == 'root':
                return render(request, 'root.html', {'name': u,
                                                     'course_list': course_list})
            else:

                sc_list = SC.objects.all()

                cno_list = []
                for line in SC.objects.all():
                    if line.sno.sno == u:
                        cno_s = line.cno.cno
                        cno_list.append(cno_s)

                cno_all_list = []
                for line in Course.objects.all():
                    cno_all_list.append(line.cno)

                course_list = None
                for c in list(set(cno_all_list) - set(cno_list)):
                    if course_list:

                        course_list = course_list | Course.objects.filter(cno=c)
                    else:
                        course_list = Course.objects.filter(cno=c)                

                return render(request, 'index.html', {'name': u,
                                                      'course_list': course_list})
        else:
            return HttpResponse("账号密码错误")
    else:
        return render(request, 'login.html')


def register_view(request):
    return render(request, 'register.html')


def register(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')
    if u and p:
        stu = Student(sno=u, password=p)
        stu.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("账号密码错误")


def choosed(request, pIndex=1):
    u = request.session['u']
    # sc_list = SC.objects.all()
    # course_list=SC.objects.filter(sno=u)
    cno_list = []
    for line in SC.objects.all():
        if line.sno.sno == u:
            cno_s = line.cno.cno
            cno_list.append(cno_s)

    course_list = None
    for c in cno_list:
        if course_list:

            course_list = course_list | Course.objects.filter(cno=c)
        else:
            course_list = Course.objects.filter(cno=c)

    # course_list=Course.objects.all()
    return render(request, 'choosed.html', {'name': u,
                                            'course_list': course_list})


def choose(request, cno):
    print(cno)
    u = request.session['u']
    stu = Student(sno=u)
    cous = Course(cno=cno)
    sc_line = SC(status=1, cno=cous, sno=stu)
    sc_line.save()

    sc_list = SC.objects.all()

    cno_list = []
    for line in SC.objects.all():
        if line.sno.sno == u:
            cno_s = line.cno.cno
            cno_list.append(cno_s)

    cno_all_list = []
    for line in Course.objects.all():
        cno_all_list.append(line.cno)

    course_list = None
    for c in list(set(cno_all_list) - set(cno_list)):
        if course_list:

            course_list = course_list | Course.objects.filter(cno=c)
        else:
            course_list = Course.objects.filter(cno=c)

    # course_list=request.session['course_list']
    return render(request, 'index.html', {'name': u,
                                          'course_list': course_list})


# def add(request, cno_i, cname_i, ccredit_i, cteacher_i, cdeptno_i):
#     print(cno_i)
#     print(cname_i)
#     print(ccredit_i)
#     print(cteacher_i)
#     print(cdeptno_i)
#     u = request.session['u']
#     course_list = Course.objects.all()
#     return render(request, 'root.html', {'name': u,
#                                           'course_list': course_list})


def add(request):
    cno_i = request.POST.get('cno_i', '')
    cname_i = request.POST.get('cname_i', '')
    ccredit_i = request.POST.get('ccredit_i', '')
    cteacher_i = request.POST.get('cteacher_i', '')
    cdeptno_i = request.POST.get('cdeptno_i', '')
    print(cno_i)
    print(cname_i)
    print(ccredit_i)
    print(cteacher_i)
    print(cdeptno_i)

    corse = Course(cno=cno_i, cname=cname_i, ccredit=ccredit_i, cteacher=cteacher_i, cdeptno=cdeptno_i)
    corse.save()

    u = request.session['u']
    course_list = Course.objects.all()
    return render(request, 'root.html', {'name': u,
                                         'course_list': course_list})


def edit(request):
    u = request.session['u']
    me = Student.objects.get(sno=u)
    if me.sno:
        sno_i = me.sno
    if me.name:
        sname_i = me.name
    if me.gender:
        sGender_i = me.gender
    if me.password:
        pwd_i = me.password
    if me.birthday:
        dob_i = me.birthday
    if me.phone:
        phone_i = me.phone
    if me.email:
        email_i = me.email

    return render(request, 'edit.html', locals())


def editData(request):
    u = request.session['u']
    me = Student.objects.get(sno=u)
    print('edit!')
    sno_i = request.POST.get('sno_i', '')
    sname_i = request.POST.get('sname_i', '')
    pwd_i = request.POST.get('pwd_i', '')
    dob_i = request.POST.get('dob_i', '')
    email_i = request.POST.get('email_i', '')
    phone_i = request.POST.get('phone_i', '')
    sGender = request.POST.get('gridRadios', '')
    print('sGender:' + sGender)
    print('sno:' + sno_i)
    print('sname: ' + sname_i)
    print('pwd: ' + pwd_i)
    print('dob: ' + dob_i)
    print('email: '+ email_i)
    print('phone: ' + phone_i)
    if sno_i:
        me.sno = sno_i
    if sGender:
        me.gender = sGender
    if sname_i:
        me.name = sname_i
    if pwd_i:
        me.password = pwd_i
    if dob_i:
        me.birthday = dob_i
    if email_i:
        me.email = email_i
    if phone_i:
        me.phone = phone_i

    me.save()
    return render(request, 'edit.html', {'name': u,
                                         })




def delete(request, cno):
    cls = Course.objects.get(cno=cno)
    cls.delete()
    u = request.session['u']
    course_list = Course.objects.all()

    return render(request, 'root.html', {'name': u,
                                         'course_list': course_list})

def root(request):
    u = request.session['u']
    course_list = Course.objects.all()

    return render(request, 'root.html', {'name': u,
                                         'course_list': course_list})


def drop(request, cno):
    u = request.session['u']
    sc = SC.objects.get(cno=cno, sno=u)
    sc.delete()
    cno_list = []
    for line in SC.objects.all():
        if line.sno.sno == u:
            cno_s = line.cno.cno
            cno_list.append(cno_s)

    course_list = None
    for c in cno_list:
        if course_list:

            course_list = course_list | Course.objects.filter(cno=c)
        else:
            course_list = Course.objects.filter(cno=c)

    # course_list=Course.objects.all()
    return render(request, 'choosed.html', {'name': u,
                                            'course_list': course_list})
