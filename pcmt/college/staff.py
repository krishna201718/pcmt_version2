from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from .models import Account
from django.db import IntegrityError
from .models import Subject
from .decorator import allowed_users
from django.contrib.auth.decorators import login_required

import datetime

year_s = datetime.datetime.today().year
YEARS = list(range(year_s, year_s - 6, -1))


def attendance(request):
    if request.POST:
        return HttpResponse("<h1> greate </h1>")
    return render(request, "attendance.html")


def add_mark(request):
    if request.POST:
        return HttpResponse("<h1> greate </h1>")
    return render(request, "add_mark.html")


from .models import Staff


def create_staff(request):
    if request.POST:
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # print(request.POST.get('department'))
        # print('first_name = ', request.POST.get('first_name'))
        # print('last_name = ', request.POST.get('last_name'))
        # print('year = ', request.POST.get('year'))
        # print('semester = ', request.POST.get('semester'))
        # # user.registration_no = request.POST.get('registration_no')
        # # user.university_roll = request.POST.get('university_roll_no')
        # print('department = ', request.POST.get('department'))
        # # user.gender = request.POST.get('gender')
        # print('phone = ', request.POST.get('phone'))
        # # user.address = request.POST.get('address')
        # print('image = ', request.FILES.get("image"))
        # print('password ', password)
        # print('Confirm password ', password_confirm)
        #
        # print('HOD', request.POST.get('hod'))
        # print('BC', request.POST.get('boc'))
        # print('Teacher', request.POST.get('teacher'))
        # return render(request, "create_staff.html")

        if password != password_confirm:
            msg = "password does not match"
            color = 'danger'
            return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})

        else:
            if len(password) >= 8:
                if password.isdigit():
                    msg = "password should atleaset 8 charactor and combination with alphanumberic charactor"
                    color = 'danger'
                    return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})

                else:
                    if password.isalpha():
                        msg = "password should atleaset 8 charactor and combination with alphanumberic charactor"
                        color = 'danger'
                        return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})
                    else:

                        try:

                            user = Account()
                            if request.POST.get('hod') == 'on' and request.POST.get('boc') == 'on' and request.POST.get('teacher') == 'on':
                                user.is_HOD = True
                                user.is_BOC = True
                                user.is_teacher = True

                            elif request.POST.get('hod') is None and request.POST.get('boc') == 'on' and request.POST.get('teacher') == 'on':
                                user.is_HOD = False
                                user.is_BOC = True
                                user.is_teacher = True

                            elif request.POST.get('hod') is None and request.POST.get('boc') is None and request.POST.get('teacher') == 'on':
                                user.is_HOD = False
                                user.is_BOC = False
                                user.is_teacher = True
                            elif request.POST.get('hod') == 'on' and request.POST.get('boc') == 'on' and request.POST.get('teacher') is None:
                                user.is_HOD = True
                                user.is_BOC = True
                                user.is_teacher = None
                            elif request.POST.get('hod') == 'on' and request.POST.get('boc') is None and request.POST.get('teacher') == 'on':
                                user.is_HOD = True
                                user.is_BOC = False
                                user.is_teacher = True
                            elif request.POST.get('staff') == 'on':
                                user.is_HOD = False
                                user.is_BOC = False
                                user.is_teacher = False
                                user.is_staff = True
                                # msg = 'Staff is created'
                                # color = 'success'
                                # return render(request, "create_staff.html", context={'msg': msg, 'color': color})

                            user.email = request.POST.get('email').lower()
                            user.set_password(request.POST.get('password'))
                            user.save()
                            if request.FILES.get("image") is None:
                                msg = 'Please select Image'
                                color = 'danger'
                                return render(request, "create_staff.html", context={'msg': msg, 'color': color})
                            else:
                                staff = Staff()
                                staff.staff_data = user
                                staff.email = request.POST.get('email').lower()
                                staff.first_name = request.POST.get('first_name')
                                staff.last_name = request.POST.get('last_name')
                                staff.joined_year = request.POST.get('year')
                                staff.department = request.POST.get('department')
                                staff.address = request.POST.get('address')
                                staff.phone = request.POST.get('phone')
                                staff.image = request.FILES.get("image")
                            if request.POST.get('hod') == 'on' and request.POST.get('boc') == 'on' and request.POST.get(
                                    'teacher') == 'on':
                                staff.is_HOD = True
                                staff.is_BOC = True
                                staff.is_teacher = True

                            elif request.POST.get('hod') is None and request.POST.get(
                                    'boc') == 'on' and request.POST.get('teacher') == 'on':
                                staff.is_HOD = False
                                staff.is_BOC = True
                                staff.is_teacher = True

                            elif request.POST.get('hod') is None and request.POST.get(
                                    'boc') is None and request.POST.get('teacher') == 'on':
                                staff.is_HOD = False
                                staff.is_BOC = False
                                staff.is_teacher = True
                            elif request.POST.get('hod') == 'on' and request.POST.get(
                                    'boc') == 'on' and request.POST.get('teacher') is None:
                                staff.is_HOD = True
                                staff.is_BOC = True
                                staff.is_teacher = None
                            elif request.POST.get('hod') == 'on' and request.POST.get(
                                    'boc') is None and request.POST.get('teacher') == 'on':
                                staff.is_HOD = True
                                staff.is_BOC = False
                                staff.is_teacher = True
                            elif request.POST.get('staff') == 'on':
                                staff.is_HOD = False
                                staff.is_BOC = False
                                staff.is_teacher = False
                                staff.is_staff = True
                            else:
                                msg = 'Staff option is not selected'
                                color = 'danger'
                                return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})

                            if request.POST.get('gender') == 1:
                                staff.gender = request.POST.get("gender")
                            else:
                                staff.gender = request.POST.get("gender")

                            staff.save()

                            msg = 'successfully submitted'
                            color = 'success'
                            return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})
                        except IntegrityError:
                            msg = 'Email already Exist'
                            color = 'danger'
                            return render(request, "create_staff.html", context={'msg': msg, 'color': color,'years': YEARS})
            else:

                msg = "password should atleaset 8 charactor and combination with alphanumberic charactor"
                color = 'danger'
                return render(request, "create_staff.html", context={'msg': msg, 'color': color})

    return render(request, "create_staff.html", {'years': YEARS})


def attendance_view(request):
    if request.POST:
        return HttpResponse("<h1> greate </h1>")
    return render(request, "attendance_view.html")


def view_staff(request):
    if request.POST:
        return HttpResponse("<h1> greate </h1>")

    if request.user.is_HOD:
        user = Staff.object.filter(is_teacher=True, department=request.session['department'])
        return render(request, "view_staff.html", context={'user': user})
    elif request.user.is_admin:
        user = Staff.object.filter()

        return render(request, "view_staff.html", context={'user': user})

    elif request.user.is_teacher:
        user = Staff.object.filter(id=request.user.id)
        return render(request, "view_staff.html", context={'user': user})


def subject_assign(request):
    if request.POST and not ((request.POST.get('email') is None) or (request.POST.get('subject') is None) or (
            request.POST.get('year') is None)):
        email = request.POST.get('email')
        subject_id = request.POST.get('subject')
        user = Staff.object.get(email=email)
        subject = Subject.objects.get(id=subject_id)
        subject.teacher = user
        subject.allocated = True
        subject.save()
        msg = "Subjected allocated successfully"
        color = 'success'
        teacher = Staff.object.filter(department=request.session['department'], is_teacher=True, active=True)
        return render(request, "subject_assign.html", {'msg': msg, 'color': color, 'teacher': teacher, 'years': YEARS})


    elif request.user.is_admin:
        teacher = Staff.object.filter(is_teacher=True, active=True)
        return render(request, "subject_assign.html", {'teacher': teacher, 'years': YEARS})

    teacher = Staff.object.filter(department=request.session['department'], is_teacher=True, active=True)
    return render(request, "subject_assign.html", {'teacher': teacher, 'years': YEARS})


#  obj.image_field
#  obj.image_field.url
#  obj.image_field.path


def create_subject(request):
    if request.POST:
        user = Staff.object.get(email=request.user.email, is_HOD=request.user.is_HOD, )
        subject = Subject()
        # print('Year',request.POST.get('year'))
        # print('Semester',request.POST.get('semester'))
        # print('Subject',request.POST.get('subject'))
        # print('Subject', request.POST.get('subject_code'))
        subject.year = request.POST.get('year')
        subject.semester = request.POST.get('semester')
        subject.name = request.POST.get('subject')
        subject.department = user.department
        subject.subject_code = request.POST.get('subject_code')
        subject.teacher = user

        try:
            subject.save()
            msg = 'Created Succesfully'
            color = 'success'
            return render(request, "create_subject.html", context={'msg': msg, 'color': color})
        except:
            msg = 'Subject already exist'
            color = 'danger'
            return render(request, "create_subject.html", context={'msg': msg, 'color': color})

    return render(request, "create_subject.html", {'years': YEARS})


# ajax view
def view_subjects(request):
    staff_obj = Staff.object.get(email=request.user.email)
    if request.POST:
        return HttpResponse("<h1> greate </h1>")

    if request.user.is_HOD:
        subject = Subject.objects.filter(department=staff_obj.department)
        return render(request, "view_subjects.html", context={'Subjects': subject})
    elif request.user.is_admin:
        subject = Subject.objects.all()
        return render(request, "view_subjects.html", context={'Subjects': subject})

    elif request.user.is_BOC:
        subject = Subject.objects.filter(teacher=staff_obj.id)
        return render(request, "view_subjects.html", context={'Subjects': subject})

    elif request.user.is_teacher:
        subject = Subject.objects.filter(teacher=staff_obj.id)
        return render(request, "view_subjects.html", context={'Subjects': subject})


from .models import Question, Result, ExamData


def exam_information(request):
    user = Staff.object.get(is_teacher=request.user.is_teacher, email=request.user.email)
    semesters = Subject.objects.filter(teacher=user).distinct()
    sem_list = []
    for sem in semesters:
        sem_list.append(sem.semester)
    sem_list = set(sem_list)
    if request.POST:
        email = request.POST.get('email')
        exam_type = request.POST.get('ca')
        semesters = request.POST.get('semester')
        subject_id = request.POST.get('subject')
        total_mark = request.POST.get('total_mark')
        total_question = request.POST.get('total_question')
        try:
            user = Staff.object.get(email=email)
            get_subject_id = Subject.objects.get(id=subject_id)
            try:
                if ExamData.objects.get(subject=get_subject_id, semester=semesters, exam=exam_type,
                                        department=user.department):
                    exam_data_obj = ExamData.objects.get(subject=get_subject_id, semester=semesters, exam=exam_type)
                    exam_data_obj.total_marks = total_mark
                    exam_data_obj.total_question = total_question
                    exam_data_obj.student = user
                    exam_data_obj.save()
                    msg = 'Updated Successfully'
                    color = 'success'
                    return render(request, 'exam_information.html', {'msg': msg, 'color': color, 'sem_list': sem_list})
                else:
                    exam_data_obj = ExamData()
                    exam_data_obj.subject = get_subject_id
                    exam_data_obj.semester = semesters
                    exam_data_obj.exam = exam_type
                    exam_data_obj.department = user.department
                    exam_data_obj.total_marks = total_mark
                    exam_data_obj.total_question = total_question
                    exam_data_obj.teacher = user
                    exam_data_obj.save()
                    msg = 'Submitted Successfully in try'
                    color = 'success'
                    return render(request, 'exam_information.html', {'msg': msg, 'color': color, 'sem_list': sem_list})

            except:
                exam_data_obj = ExamData()
                exam_data_obj.subject = get_subject_id
                exam_data_obj.semester = semesters
                exam_data_obj.exam = exam_type
                exam_data_obj.department = user.department
                exam_data_obj.total_marks = total_mark
                exam_data_obj.total_question = total_question
                exam_data_obj.teacher = user
                exam_data_obj.save()
                msg = 'Submitted Successfully in Except'
                color = 'success'
                return render(request, 'exam_information.html', {'msg': msg, 'color': color, 'sem_list': sem_list})


        except:
            msg = 'Please Fill the fields carefully'
            color = 'danger'
            return render(request, 'exam_information.html', {'msg': msg, 'color': color, 'sem_list': sem_list})
        # print(request.POST.get('ca'))
        # print(request.POST.get('semester'))
        # print(request.POST.get('subject'))
        # print(request.POST.get('total_mark'))
        # print(request.POST.get('email'))
        # return render(request, 'exam_information.html', {'sem_list': sem_list})

    return render(request, 'exam_information.html', {'sem_list': sem_list})


def add_question(request):
    user = Staff.object.get(is_teacher=request.user.is_teacher, email=request.user.email)
    semesters = ExamData.objects.filter(teacher=user).distinct()
    sem_list = []
    for sem in semesters:
        sem_list.append(sem.semester)

    sem_list = set(sem_list)

    if request.POST:
        find_user = request.POST.get('email')
        user = Staff.object.get(email=find_user)

        question = request.POST.get('question')
        exam_type = request.POST.get('ca')
        subject_id = request.POST.get('subject')

        # print(exam_type)

        choice_1 = request.POST.get('choice_1')
        choice_2 = request.POST.get('choice_2')
        choice_3 = request.POST.get('choice_3')
        choice_4 = request.POST.get('choice_4')
        correct_choice = request.POST.get('correct')

        get_subject = Subject.objects.get(id=subject_id)
        sem = get_subject.semester
        total_questions = ExamData.objects.get(teacher=user.id, semester=sem, exam=exam_type,
                                               subject=get_subject).total_question

        try:
                if Question.objects.filter(semester=sem, exam=exam_type, subject=get_subject.id,
                                           teacher=user.id).count() <= total_questions-1:
                    num = Question.objects.filter(semester=sem, exam=exam_type,subject=get_subject.id).count()

                    question_obj = Question()
                    question_obj.question_text = question
                    question_obj.subject = get_subject
                    question_obj.exam = exam_type
                    question_obj.teacher = user
                    question_obj.semester = sem
                    question_obj.question_no = (num + 1)

                    # adding choice Corrosponding with answer
                    question_obj.choice_text1 = choice_1
                    question_obj.choice_text2 = choice_2
                    question_obj.choice_text3 = choice_3
                    question_obj.choice_text4 = choice_4
                    question_obj.correct = correct_choice
                    question_obj.save()
                    print('in try loop')
                    msg = 'Next question'
                    color = 'success'
                    return render(request, 'add_question.html',
                                  {'question_no': num + 1, 'total_questions': total_questions, 'msg': msg, 'color': color,
                                   'sem_list': sem_list})
                elif not Question.objects.filter(semester=sem, exam=exam_type, subject=get_subject.id,
                                             teacher=user.id,).exists():

                    question_obj = Question()
                    question_obj.question_text = question
                    question_obj.subject = get_subject
                    question_obj.exam = exam_type
                    question_obj.teacher = user
                    question_obj.semester = sem
                    question_obj.question_no = 1

                    # adding choice Corrosponding with answer
                    question_obj.choice_text1 = choice_1
                    question_obj.choice_text2 = choice_2
                    question_obj.choice_text3 = choice_3
                    question_obj.choice_text4 = choice_4
                    question_obj.correct = correct_choice
                    question_obj.save()
                    msg = 'Next question'
                    color = 'success'
                    return render(request, 'add_question.html',
                                  {'question_no': 1, 'total_questions': total_questions, 'msg': msg, 'color': color,
                                   'sem_list': sem_list})
                else:
                    msg = 'All question done thank you'
                    color = 'danger'
                    return render(request, 'add_question.html',
                                  {'question_no': 1, 'total_questions': total_questions, 'msg': msg, 'color': color,
                                   'sem_list': sem_list})
        except:
                msg = 'Try to fill all the details'
                color = 'danger'
                return render(request, 'add_question.html',
                              {'question_no': 1, 'total_questions': total_questions, 'msg': msg, 'color': color,
                               'sem_list': sem_list})

    return render(request, 'add_question.html', {'question_no': 1, 'sem_list': sem_list})


def add_question_load_exam_type(request):
    if request.GET.get('sub_id') is "":
        subject = {}
        return render(request, 'ca_options.html', {'Subjects': subject})
    elif request.GET.get('email') is "":
        subject = {}
        return render(request, 'ca_options.html', {'Subjects': subject})
    else:
        dep = Staff.object.get(email=request.GET.get('email'))
        sub = Subject.objects.get(id=request.GET.get('sub_id'))
        if ExamData.objects.filter(subject=sub.id, department=dep.department, teacher=dep.id):
            subject = ExamData.objects.filter(subject=sub.id, department=dep.department, teacher=dep.id)
            return render(request, 'ca_options.html', {'Subjects': subject})
        else:
            subject = {}
            return render(request, 'ca_options.html', {'Subjects': subject})


def add_question_load_subject(request):
    if request.GET.get('semester') is "":
        subject = {}
        return render(request, 'subject_options.html', {'Subjects': subject})
    elif request.GET.get('email') is "":
        subject = {}
        return render(request, 'subject_options.html', {'Subjects': subject})
    else:
        dep = Staff.object.get(email=request.GET.get('email'))
        semester = request.GET.get('semester')
        if Subject.objects.filter(semester=semester, department=dep.department, teacher=dep.id):
            subject = Subject.objects.filter(semester=semester, department=dep.department,teacher=dep.id)
            print(subject)
            return render(request, 'subject_options.html', {'Subjects': subject})
        else:
            subject = {}
            return render(request, 'subject_options.html', {'Subjects': subject})


def load_subject(request):
    if request.GET.get('semester') == "":
        subject = {}
        return render(request, 'subject_options.html', {'Subjects': subject})
    elif request.GET.get('year') == "":
        subject = {}
        return render(request, 'subject_options.html', {'Subjects': subject})
    else:
        if Subject.objects.filter(semester=request.GET.get('semester'), department=request.session['department'],
                                  year=request.GET.get('year')):
            subject = Subject.objects.filter(semester=request.GET.get('semester'),
                                             department=request.session['department'],
                                             year=request.GET.get('year'), allocated=False)
            return render(request, 'subject_options.html', {'Subjects': subject})


def load_semester(request):
    if request.GET.get('year') == "":
        sem = {}
        return render(request, 'semester_options.html', {'Semester': sem})
    else:
        sem = Subject.objects.filter(year=request.GET.get('year'))
        year = []
        for s in sem:
            year.append(s.semester)
        year = set(year)
        return render(request, 'semester_options.html', {'Semester': year})
