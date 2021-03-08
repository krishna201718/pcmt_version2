from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views ,student,staff


app_name = 'college'

urlpatterns = [
    # common view
    path('', views.index, name='index'),

    path('admission_data', views.admission_data, name='admission_data'),

    path('home_student', views.home_student, name='home_student'),
    path('home_staff', views.home_staff, name='home_staff'),
    path('home_general', views.home_general, name='home_general'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('logout', views.log_out, name='logout'),
    path('course', views.course, name='course'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('admission', views.admission, name='admission'),
    path('new_enrollment', views.new_enrollment, name='new_enrollment'),

    # exam
    path('exam', views.exam, name='exam'),
    path('exam_information', staff.exam_information, name='exam_information'),
    path('question_view/<int:semester>/<int:ca>/<int:subject>/<int:question_id>', views.question_view, name='question_view'),
    path('question/<semester>/<ca>/<subject>', views.question, name='question'),
    path('view_reports', views.view_reports, name='view_reports'),
    path('download_report', views.download_report, name='download_report'),
    path('add_question', staff.add_question, name='add_question'),
    path('add_question_load_subject', staff.add_question_load_subject, name='add_question_load_subject'),
    path('add_question_load_exam_type', staff.add_question_load_exam_type, name='add_question_load_exam_type'),

    # student
    path('studentsRegistration', student.studentsRegistration, name='studentsRegistration'),
    path('student_data_view', student.student_data_view, name='student_data_view'),
    path('profile/<id>', views.profile, name='profile'),

    # staff
    path('create_staff', staff.create_staff, name='create_staff'),
    path('attendance_view', staff.attendance_view, name='attendance_view'),
    path('view_staff', staff.view_staff, name='view_staff'),
    path('attendance', staff.attendance, name='attendance'),
    path('add_mark', staff.add_mark, name='add_mark'),
    path('subject_assign', staff.subject_assign, name='subject_assign'),
    path('create_subject', staff.create_subject, name='create_subject'),
    path('view_subjects', staff.view_subjects, name='view_subjects'),

    # ajax file
    path('load_subject', staff.load_subject, name='load_subject'),
    path('load_semester', staff.load_semester, name='load_semester'),

    # print
    path('export_admission_pdf/<email>', views.export_admission_pdf, name='export_admission_pdf'),
    path('export_pdf/<email>', views.export_pdf, name='export_pdf'),
    path('export_student_data_pdf', views.export_student_data_pdf, name='export_student_data_pdf'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
