from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import os
from uuid import uuid4

from django.db.models import CharField
# qrcode
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw, ImageFont


# qrcode

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("A Email Required")
        # if not username:
        #     raise ValueError("Usename Required")
        user = self.model(
            email=self.normalize_email(email),
            # username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_approved = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    # common field for staff and student
    email = models.EmailField(max_length=100, verbose_name="email", unique=True)

    recovery_email = models.EmailField(max_length=255, default="admin@pcmt-india.net")

    last_login = models.DateTimeField(auto_now=True)

    enrollment_no = models.CharField(max_length=20, default='')

    # user privileges
    is_approved = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    is_HOD = models.BooleanField(default=False)
    is_BOC = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    object = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, objec=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Staff(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'staff/'
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    staff_data = models.ForeignKey(Account, on_delete=models.CASCADE)

    # common field for staff and student
    email = models.EmailField(max_length=100, verbose_name="email", unique=True)
    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100, )
    joined_year = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, )
    phone = models.CharField(max_length=15, verbose_name='phone')
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, default='')
    active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    # user privileges
    is_HOD = models.BooleanField(default=False)
    is_BOC = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    object = AccountManager()


class Student(models.Model):
    def profile(instance, filename):
        upload_to = 'profile/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def rank_card(instance, filename):
        upload_to = 'rank_card/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_aadhar_card(instance, filename):
        upload_to = 'aadhar_card/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def admit_card(instance, filename):
        upload_to = 'admit_card_entrance/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_admit_card_10(instance, filename):
        upload_to = 'admit_card_10/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_10(instance, filename):
        upload_to = 'marksheet_10/'
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_admit_card_12(instance, filename):
        upload_to = 'admit_card_12/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_12(instance, filename):
        upload_to = 'marksheet_12/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_cast_certificate(instance, filename):
        upload_to = 'cast_certificate/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_physically_certificate(instance, filename):
        upload_to = 'physically_certificate/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_certificateDiploma(instance, filename):
        upload_to = 'certificateDiploma/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_diploma(instance, filename):
        upload_to = 'marksheet_diploma/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_qr_code(instance, filename):
        upload_to = 'qrCode/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    student_data = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    # university fields
    registration_no = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    semester = models.IntegerField(default=1)
    university_roll = models.CharField(max_length=20)

    enrollment_no = models.CharField(max_length=255, default='', unique=True)
    qr_code = models.ImageField(upload_to=image_qr_code, blank=True, )

    # personal information
    contact_no = models.CharField(max_length=10, verbose_name='phone')
    email = models.EmailField(max_length=100, verbose_name="email", unique=True)

    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100, )
    dob = models.CharField(max_length=255, blank=True, default="")
    gender = models.CharField(max_length=10, )

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

    fathers_name = models.CharField(max_length=255, default='')
    mothers_name = models.CharField(max_length=255, default='')
    blood_group = models.CharField(max_length=255, default='')
    mothers_tongue = models.CharField(max_length=255, default='')

    fathers_contact_no = models.CharField(max_length=255, default='')
    fathers_email = models.EmailField(max_length=100, default='')
    guardian_name = models.CharField(max_length=255, blank=True, default='')
    guardian_contact_no = models.CharField(max_length=255, blank=True, default='')
    relation_with_guardian = models.CharField(max_length=255, blank=True, default='')

    nationality = models.CharField(max_length=255, blank=True)
    cast = models.CharField(max_length=8)
    religion = models.CharField(max_length=8)
    physically_challenge = models.CharField(max_length=8)

    department = models.CharField(max_length=255)
    aadhar_card_no = models.CharField(max_length=255)

    aadhar_card = models.ImageField(upload_to=image_aadhar_card, blank=True, )
    cast_certificate = models.ImageField(upload_to=image_cast_certificate, max_length=255, null=True, blank=True)
    physically_certificate = models.ImageField(upload_to=image_physically_certificate, max_length=255, null=True,
                                               blank=True)
    photo = models.ImageField(upload_to=profile, max_length=255, null=True, blank=True)

    # wbjee or main

    admission_cat = models.CharField(max_length=255)
    conducted_by = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=255)

    allotment = models.CharField(max_length=10)
    rank_card = models.ImageField(upload_to=rank_card, max_length=255, null=True, blank=True)
    admit_card = models.ImageField(upload_to=admit_card, max_length=255, null=True, blank=True)

    # education details
    # 10th
    school_name_10 = models.CharField(max_length=255, blank=True, default="")
    board_10 = models.CharField(max_length=255, blank=True, default="")
    medium_10 = models.CharField(max_length=255, blank=True, default="")

    address10 = models.CharField(max_length=255, blank=True, default=0)
    city10 = models.CharField(max_length=255, blank=True, default=0)
    state10 = models.CharField(max_length=255, blank=True, default=0)
    country10 = models.CharField(max_length=255, blank=True, default=0)
    passing_year_10 = models.CharField(max_length=255, blank=True, default=0)

    sub1 = models.CharField(max_length=255, blank=True, default=0)
    sub2 = models.CharField(max_length=255, blank=True, default=0)
    sub3 = models.CharField(max_length=255, blank=True, default=0)
    sub4 = models.CharField(max_length=255, blank=True, default=0)
    sub5 = models.CharField(max_length=255, blank=True, default=0)
    aggregate10 = models.CharField(max_length=255, blank=True, default='')

    admit10 = models.ImageField(upload_to=image_admit_card_10, max_length=255, null=True, blank=True)
    mark10 = models.ImageField(upload_to=image_marksheet_10, max_length=255, null=True, blank=True)
    certificate10 = models.ImageField(upload_to=image_marksheet_10, max_length=255, null=True, blank=True)

    # 12th
    school_name_12 = models.CharField(max_length=255, blank=True, default=" ")
    board_12 = models.CharField(max_length=255, blank=True, default="")
    medium_12 = models.CharField(max_length=255, blank=True, default="")

    address12 = models.CharField(max_length=255, blank=True, default=0)
    city12 = models.CharField(max_length=255, blank=True, default=0)
    state12 = models.CharField(max_length=255, blank=True, default=0)
    country12 = models.CharField(max_length=255, blank=True, default=0)
    passing_year_12 = models.CharField(max_length=255, blank=True, default=0)

    english = models.CharField(max_length=255, blank=True, default=0)
    chemistry = models.CharField(max_length=255, blank=True, default=0)
    physics = models.CharField(max_length=255, blank=True, default=0)
    math = models.CharField(max_length=255, blank=True, default=0)
    optional = models.CharField(max_length=255, blank=True, default=0)
    aggregate12 = models.CharField(max_length=255, blank=True, default='')

    mark12 = models.ImageField(upload_to=image_marksheet_12, max_length=255, null=True, blank=True)
    admit12 = models.ImageField(upload_to=image_admit_card_12, max_length=255, null=True, blank=True)
    certificate12 = models.ImageField(upload_to=image_marksheet_12, max_length=255, null=True, blank=True)

    # diploma
    school_name_diploma = models.CharField(max_length=255, blank=True, default=" ")
    board_diploma = models.CharField(max_length=255, blank=True, default="")
    medium_diploma = models.CharField(max_length=255, blank=True, default="")

    addressDiploma = models.CharField(max_length=255, blank=True, default=0)
    cityDiploma = models.CharField(max_length=255, blank=True, default=0)
    stateDiploma = models.CharField(max_length=255, blank=True, default=0)
    countryDiploma = models.CharField(max_length=255, blank=True, default=0)
    passing_year_Diploma = models.CharField(max_length=255, blank=True, default=0)

    marksDiploma = models.CharField(max_length=255, blank=True, default='')
    aggregateDiploma = models.CharField(max_length=255, blank=True, default='')
    division = models.CharField(max_length=255, blank=True, default='')

    markDiploma = models.ImageField(upload_to=image_marksheet_diploma, max_length=255, null=True, blank=True)
    certificateDiploma = models.ImageField(upload_to=image_certificateDiploma, max_length=255, null=True, blank=True)

    # others
    loan = models.CharField(max_length=255, blank=True, default='')
    hostel = models.CharField(max_length=255, blank=True, default='')
    gap = models.CharField(max_length=255, blank=True, default="")
    reason = models.CharField(max_length=255, blank=True, default='')

    last_login = models.DateTimeField(auto_now=True)
    joined_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def saveQrCode(self, enrollment_no=''):
        qrcode_img = qrcode.make(enrollment_no)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        draw = ImageDraw.Draw(canvas)
        draw.text((45, 250), self.enrollment_no, fill=(0, 0, 0), font=ImageFont.truetype('assets/RobotoMono'
                                                                                         '-VariableFont_wght.ttf',
                                                                                         22), align="center")

        fname = f'qr_code-{enrollment_no}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

    objects = models.Manager()


class Admission(models.Model):
    def profile(instance, filename):
        upload_to = 'profile/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def rank_card(instance, filename):
        upload_to = 'rank_card/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_aadhar_card(instance, filename):
        upload_to = 'aadhar_card/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def admit_card(instance, filename):
        upload_to = 'admit_card_entrance/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_admit_card_10(instance, filename):
        upload_to = 'admit_card_10/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_10(instance, filename):
        upload_to = 'marksheet_10/'
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_admit_card_12(instance, filename):
        upload_to = 'admit_card_12/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_12(instance, filename):
        upload_to = 'marksheet_12/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_cast_certificate(instance, filename):
        upload_to = 'cast_certificate/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_physically_certificate(instance, filename):
        upload_to = 'physically_certificate/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_certificateDiploma(instance, filename):
        upload_to = 'certificateDiploma/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_marksheet_diploma(instance, filename):
        upload_to = 'marksheet_diploma/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    def image_qr_code(instance, filename):
        upload_to = 'qrCode/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)

    student_data = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    enrollment_no = models.CharField(max_length=255, default='', unique=True)
    qr_code = models.ImageField(upload_to=image_qr_code, blank=True, )

    year = models.CharField(max_length=4)

    # personal information
    contact_no = models.CharField(max_length=10, verbose_name='phone')
    email = models.EmailField(max_length=100, verbose_name="email", unique=True)

    first_name = models.CharField(max_length=100, )
    last_name = models.CharField(max_length=100, )
    dob = models.CharField(max_length=255, blank=True, default="")
    gender = models.CharField(max_length=10, )

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

    fathers_name = models.CharField(max_length=255, default='')
    mothers_name = models.CharField(max_length=255, default='')
    blood_group = models.CharField(max_length=255, default='')
    mothers_tongue = models.CharField(max_length=255, default='')

    fathers_contact_no = models.CharField(max_length=255, default='')
    fathers_email = models.EmailField(max_length=100, default='')
    guardian_name = models.CharField(max_length=255, blank=True, default='')
    guardian_contact_no = models.CharField(max_length=255, blank=True, default='')
    relation_with_guardian = models.CharField(max_length=255, blank=True, default='')

    nationality = models.CharField(max_length=255, blank=True)
    cast = models.CharField(max_length=8)
    religion = models.CharField(max_length=8)
    physically_challenge = models.CharField(max_length=8)

    department = models.CharField(max_length=255)
    aadhar_card_no = models.CharField(max_length=255)

    aadhar_card = models.ImageField(upload_to=image_aadhar_card, blank=True, )
    cast_certificate = models.ImageField(upload_to=image_cast_certificate, max_length=255, null=True, blank=True)
    physically_certificate = models.ImageField(upload_to=image_physically_certificate, max_length=255, null=True,
                                               blank=True)
    photo = models.ImageField(upload_to=profile, max_length=255, null=True, blank=True)

    # wbjee or main

    admission_cat = models.CharField(max_length=255)
    conducted_by = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=255)

    allotment = models.CharField(max_length=10)
    rank_card = models.ImageField(upload_to=rank_card, max_length=255, null=True, blank=True)
    admit_card = models.ImageField(upload_to=admit_card, max_length=255, null=True, blank=True)

    # education details
    # 10th
    school_name_10 = models.CharField(max_length=255, blank=True, default="")
    board_10 = models.CharField(max_length=255, blank=True, default="")
    medium_10 = models.CharField(max_length=255, blank=True, default="")

    address10 = models.CharField(max_length=255, blank=True, default=0)
    city10 = models.CharField(max_length=255, blank=True, default=0)
    state10 = models.CharField(max_length=255, blank=True, default=0)
    country10 = models.CharField(max_length=255, blank=True, default=0)
    passing_year_10 = models.CharField(max_length=255, blank=True, default=0)

    sub1 = models.CharField(max_length=255, blank=True, default=0)
    sub2 = models.CharField(max_length=255, blank=True, default=0)
    sub3 = models.CharField(max_length=255, blank=True, default=0)
    sub4 = models.CharField(max_length=255, blank=True, default=0)
    sub5 = models.CharField(max_length=255, blank=True, default=0)
    aggregate10 = models.CharField(max_length=255, blank=True, default='')

    admit10 = models.ImageField(upload_to=image_admit_card_10, max_length=255, null=True, blank=True)
    mark10 = models.ImageField(upload_to=image_marksheet_10, max_length=255, null=True, blank=True)
    certificate10 = models.ImageField(upload_to=image_marksheet_10, max_length=255, null=True, blank=True)

    # 12th
    school_name_12 = models.CharField(max_length=255, blank=True, default=" ")
    board_12 = models.CharField(max_length=255, blank=True, default="")
    medium_12 = models.CharField(max_length=255, blank=True, default="")

    address12 = models.CharField(max_length=255, blank=True, default=0)
    city12 = models.CharField(max_length=255, blank=True, default=0)
    state12 = models.CharField(max_length=255, blank=True, default=0)
    country12 = models.CharField(max_length=255, blank=True, default=0)
    passing_year_12 = models.CharField(max_length=255, blank=True, default=0)

    english = models.CharField(max_length=255, blank=True, default=0)
    chemistry = models.CharField(max_length=255, blank=True, default=0)
    physics = models.CharField(max_length=255, blank=True, default=0)
    math = models.CharField(max_length=255, blank=True, default=0)
    optional = models.CharField(max_length=255, blank=True, default=0)
    aggregate12 = models.CharField(max_length=255, blank=True, default='')

    mark12 = models.ImageField(upload_to=image_marksheet_12, max_length=255, null=True, blank=True)
    admit12 = models.ImageField(upload_to=image_admit_card_12, max_length=255, null=True, blank=True)
    certificate12 = models.ImageField(upload_to=image_marksheet_12, max_length=255, null=True, blank=True)

    # diploma
    school_name_diploma = models.CharField(max_length=255, blank=True, default=" ")
    board_diploma = models.CharField(max_length=255, blank=True, default="")
    medium_diploma = models.CharField(max_length=255, blank=True, default="")

    addressDiploma = models.CharField(max_length=255, blank=True, default=0)
    cityDiploma = models.CharField(max_length=255, blank=True, default=0)
    stateDiploma = models.CharField(max_length=255, blank=True, default=0)
    countryDiploma = models.CharField(max_length=255, blank=True, default=0)
    passing_year_Diploma = models.CharField(max_length=255, blank=True, default=0)

    marksDiploma = models.CharField(max_length=255, blank=True, default='')
    aggregateDiploma = models.CharField(max_length=255, blank=True, default='')
    division = models.CharField(max_length=255, blank=True, default='')

    markDiploma = models.ImageField(upload_to=image_marksheet_diploma, max_length=255, null=True, blank=True)
    certificateDiploma = models.ImageField(upload_to=image_certificateDiploma, max_length=255, null=True, blank=True)

    # others
    loan = models.CharField(max_length=255, blank=True, default='')
    hostel = models.CharField(max_length=255, blank=True, default='')
    gap = models.CharField(max_length=255, blank=True, default="")
    reason = models.CharField(max_length=255, blank=True, default='')

    last_login = models.DateTimeField(auto_now=True)
    joined_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def saveQrCode(self, enrollment_no=''):
        qrcode_img = qrcode.make(enrollment_no)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        draw = ImageDraw.Draw(canvas)
        draw.text((45, 250), self.enrollment_no, fill=(0, 0, 0), font=ImageFont.truetype('assets/RobotoMono'
                                                                                         '-VariableFont_wght.ttf',
                                                                                         22), align="center")

        fname = f'qr_code-{enrollment_no}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

    objects = models.Manager()


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField(default="")
    allow_test = models.BooleanField(default=False)
    department = models.CharField(max_length=255, )
    name = models.CharField(max_length=255, verbose_name='Subject_name')
    subject_code = models.CharField(max_length=255, verbose_name='Subject_code', default='', )
    allocated = models.BooleanField(default=False)
    objects = models.Manager()


from datetime import datetime


class Question(models.Model):
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    question_no = models.IntegerField()
    semester = models.IntegerField()
    exam = models.IntegerField()

    # time  for everyone or  one people
    exam_start_time = models.DateTimeField(default=datetime.today())
    exam_end_time = models.DateTimeField(default=datetime.today())

    question_text = models.CharField(max_length=255)
    choice_text1 = models.CharField(max_length=255)
    choice_text2 = models.CharField(max_length=255)
    choice_text3 = models.CharField(max_length=255)
    choice_text4 = models.CharField(max_length=255)
    correct = models.IntegerField()

    pub_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ExamData(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    exam = models.IntegerField()
    total_question = models.IntegerField()
    department = models.CharField(max_length=255, default='please enter department')
    semester = models.IntegerField()
    total_marks = models.IntegerField(default=0)
    exam_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.ForeignKey(ExamData, on_delete=models.CASCADE)

    exam = models.IntegerField()
    department = models.CharField(max_length=255, default='please enter department')
    semester = models.IntegerField()
    marks = models.IntegerField(default=0)
    exam_done = models.BooleanField(default=False)
    exam_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
