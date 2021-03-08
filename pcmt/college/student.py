from django.shortcuts import render, HttpResponse, redirect
from .models import Account,Admission,Student
from django.db import IntegrityError
from .decorator import allowed_users
from django.contrib.auth.decorators import login_required
import datetime
import secrets, random
import string
import datetime
def gen():
    N = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
    res = 'PCMT' + str(datetime.datetime.today().year) + res
    return res

@login_required(login_url='college:login')
def studentsRegistration(request):
    if request.POST:
        # try:
        if request.POST.get('email'):
            try:
                enrollment_no = gen()
                add_user = Account()
                add_user.email = request.POST.get('email')
                request.session['student_email'] = request.POST.get('email')
                print(request.session['student_email'])
                add_user.enrollment_no = enrollment_no

                add_user.set_password(enrollment_no)
                add_user.is_student = True
                add_user.save()

                user = Student()
                user.semester = request.POST.get('semester')
                user.year = str(datetime.datetime.today().year)
                user.student_data = add_user
                user.enrollment_no = enrollment_no
                user.email = request.POST.get('email')
                user.contact_no = request.POST.get('contact_no')

                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.dob = request.POST.get('dob')
                user.gender = request.POST.get('gender')

                user.address = request.POST.get('address')
                user.city = request.POST.get('city')
                user.state = request.POST.get('state')
                user.country = request.POST.get('country')

                user.fathers_name = request.POST.get('fathers_name')
                user.mothers_name = request.POST.get('mothers_name')
                user.blood_group = request.POST.get('blood_group')
                user.mothers_tongue = request.POST.get('mothers_tongue')

                user.fathers_contact_no = request.POST.get('fathers_contact_no')
                user.guardian_name = request.POST.get('guardian_name')
                user.guardian_contact_no = request.POST.get('guardian_contact_no')
                user.relation_with_guardian = request.POST.get('relation_with_guardian')

                user.nationality = request.POST.get('nationality')
                user.cast = request.POST.get('cast')
                user.religion = request.POST.get('religion')
                user.physically_challenge = request.POST.get('physically_challenge')

                user.department = request.POST.get('department')
                user.aadhar_card_no = request.POST.get('aadhar_card_no')
                user.save()

                user.physically_certificate = request.FILES.get('physically_certificate')
                user.cast_certificate = request.FILES.get('cast_certificate')
                user.photo = request.FILES.get('photo')
                user.aadhar_card = request.FILES.get('aadhar_card')

                user.saveQrCode(enrollment_no=enrollment_no)
                user.save()
                msg = "Saved successfully"
                color = 'success'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
            except:
                if Student.objects.filter(email=request.session['student_email']).count():
                    msg = "Fill Entrance Examination field"
                    color = 'danger'
                    print('hello',Student.objects.filter(email=request.session['student_email']).count)
                    return render(request, 'registration.html', {'msg': msg, 'color': color})
                else:
                    msg = "Try fill all the filed"
                    color = 'danger'
                    return render(request, 'registration.html', {'msg': msg, 'color': color})
        elif request.POST.get('admission_cat'):
            try:
                user = Student.objects.get(email=request.session['student_email'])
                user.admission_cat = request.POST.get('admission_cat')
                user.conducted_by = request.POST.get('conducted_by')
                user.rank = request.POST.get('rank')
                user.roll_no = request.POST.get('roll_no')

                user.allotment = request.POST.get('allotment')
                user.admit_card = request.FILES.get('admit_card')
                user.rank_card = request.FILES.get('rank_card')
                user.roll_no = request.POST.get('roll_no')
                user.save()
                msg = "Saved successfully And Fill Education information 10th"
                color = 'success'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
            except:
                msg = "Entrance examination fill all field"
                color = 'danger'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
        elif request.POST.get('school_name_10'):
            try:
                user = Student.objects.get(email=request.session['student_email'])
                user.school_name_10 = request.POST.get('school_name_10')
                user.board_10 = request.POST.get('board_10')
                user.medium_10 = request.POST.get('medium_10')

                user.address10 = request.POST.get('address10')
                user.city10 = request.POST.get('city10')
                user.state10 = request.POST.get('state10')
                user.country10 = request.POST.get('country10')
                user.passing_year_10 = request.POST.get('passing_year_10')

                user.sub1 = request.POST.get('sub1')
                user.sub2 = request.POST.get('sub2')
                user.sub3 = request.POST.get('sub3')
                user.sub4 = request.POST.get('sub4')
                user.sub5 = request.POST.get('sub5')
                user.aggregate10 = request.POST.get('aggregate10')

                user.mark10 = request.FILES.get('mark10')
                user.admit10 = request.FILES.get('admit10')
                user.certificate10 = request.FILES.get('certificate10')
                user.save()
                msg = "Saved successfully And Fill 12th or Diploma form"
                color = 'success'
                return render(request, 'new_enrollment.html', {'msg': msg, 'color': color})
            except:
                msg = "Fill Education information 10th all field correctly"
                color = 'danger'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
        elif request.POST.get('diploma_or_12') == '12th':
            try:
                user = Student.objects.get(email=request.session['student_email'])
                user.school_name_12 = request.POST.get('school_name_12')
                user.board_12 = request.POST.get('board_12')
                user.medium_12 = request.POST.get('medium_12')

                user.address12 = request.POST.get('address12')
                user.city12 = request.POST.get('city12')
                user.state12 = request.POST.get('state12')
                user.country12 = request.POST.get('country12')
                user.passing_year_12 = request.POST.get('passing_year_12')

                user.english = request.POST.get('english')
                user.chemistry = request.POST.get('chemistry')
                user.physics = request.POST.get('physics')
                user.math = request.POST.get('math')
                user.optional = request.POST.get('optional')
                user.aggregate12 = request.POST.get('aggregate12')

                user.mark12 = request.FILES.get('mark12')
                user.admit12 = request.FILES.get('admit12')
                user.certificate12 = request.FILES.get('certificate12')
                user.save()
                msg = "Saved successfully And Fill others form"
                color = 'success'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
            except:
                msg = "Fill Education 12th or Diploma"
                color = 'danger'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
        elif request.POST.get('diploma_or_12') == 'diploma':
            try:
                user = Student.objects.get(email=request.session['student_email'])
                user.school_name_diploma = request.POST.get('school_name_diploma')
                user.board_diploma = request.POST.get('board_diploma')
                user.medium_diploma = request.POST.get('medium_diploma')

                user.addressDiploma = request.POST.get('addressDiploma')
                user.cityDiploma = request.POST.get('cityDiploma')
                user.stateDiploma = request.POST.get('stateDiploma')
                user.countryDiploma = request.POST.get('countryDiploma')
                user.passing_year_Diploma = request.POST.get('passing_year_Diploma')

                user.marksDiploma = request.POST.get('marksDiploma')
                user.aggregateDiploma = request.POST.get('aggregateDiploma')
                user.division = request.POST.get('division')
                user.markDiploma = request.FILES.get('markDiploma')
                user.certificateDiploma = request.FILES.get('certificateDiploma')
                user.save()
                msg = "Saved successfully And Fill others form"
                color = 'success'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
            except:
                msg = "Fill Education 12th or Diploma"
                color = 'danger'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
        elif request.POST.get('loan'):
            try:
                user = Student.objects.get(email = request.session['student_email'])
                user.loan = request.POST.get('loan')
                user.gap = request.POST.get('gap')
                user.reason = request.POST.get('reason')
                user.hostel = request.POST.get('hostel')
                user.save()
                msg = "Saved successfully"
                color = 'success'
                return render(request, 'registration.html', {'msg': msg, 'color': color})
            except:
                msg = "Try fill all fields"
                color = 'danger'
                return render(request, 'registration.html', {'msg': msg, 'color': color})

    return render(request, 'registration.html',)



@login_required(login_url='college:login')
def student_data_view(request):
    if request.POST:
        if request.POST.get('university_roll'):
            university_roll = request.POST.get('university_roll')
            print('university_roll', university_roll)
            User = Account.object.filter(university_roll=university_roll)
            return render(request, "student_data_view.html", context={'user': User})
        else:
            year = request.POST.get('go_year')
            semester = request.POST.get('go_semester')
            print('year', year)
            print('semester', semester)

            User = Account.object.filter(semester=semester, year=year)
            return render(request, "student_data_view.html", context={'user': User})
    elif request.user.is_HOD:
        user = Student.objects.filter( department=request.session['department'])
        return render(request, "student_data_view.html", context={'user': user})
    elif request.user.is_admin:
        user = Student.objects.all()
        return render(request, "student_data_view.html", context={'user': user})
    elif request.user.is_student:
        user = Student.objects.filter(email=request.session['email'])
        return render(request, "student_data_view.html", context={'user': user})

    elif request.user.is_BOC:
        # user = Student.objects.filter(is_student=True, year=request.user.year, semester=request.user.semester)
        user = Student.objects.filter( department=request.session['department'])
        return render(request, "student_data_view.html", context={'user': user})
    return render(request, "registration.html")
