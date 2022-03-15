from django.db import models
class Gender(models.Model):
    Gender = models.CharField('Gender', max_length=30, null=True)

    def __str__(self):
        return self.Gender


# Create your models here.
class Form(models.Model):
    '''
        first_name = models.CharField('First Name', max_length=30, null=True)
    Last_name = models.CharField('Last Name', max_length=30, null=True)
    dob = models.DateField('Date of Birth', null=True)
    Gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    email = models.EmailField('Email', max_length=80, null=True)

       phone_number = models.IntegerField('Phone Number', null=True)
    address = models.TextField('Address', null=True)
    city = models.CharField('City', max_length=80, null=True)
    state = models.CharField('State', max_length=80, null=True)
    country = models.CharField('Country', max_length=80, null=True)
    pin_code = models.IntegerField('Pin Code', null=True)
    signature = models.FileField(upload_to='sign/', null=True)

    '''
    name = models.CharField('Name', max_length=30, null=True)
    email = models.EmailField('Email', max_length=80, unique=True, null=True)
    phone1 = models.IntegerField("Phone Number", null=True)
    phone2 = models.IntegerField("Phone Number 2", null=True)
    address = models.CharField("Address", max_length=200, null=True)
    father_name = models.CharField("Father Name", max_length=30, null=True)
    mother_name = models.CharField("Mother Name", max_length=30, null=True)
    college = models.CharField("College Name", max_length=200, null=True)
    registerNo = models.IntegerField("Register No", null=True)
    course = models.CharField("Course", max_length=100, null=True)
    department = models.CharField("Department", max_length=100, null=True)
    year = models.CharField("Year", max_length=20, null=True)
    photo = models.FileField(upload_to='photo/', null=True)
    signature = models.FileField(upload_to='sign/', null=True)

    def __str__(self):
        return "{} - {}".format(self.name, str(self.registerNo))


class info_team(models.Model):
    name = models.CharField('Name', max_length=120, null=True)
    register_no = models.IntegerField('Register Number', null=True)
    batch = models.CharField('Batch', max_length=80, null=True)
    photo = models.FileField('Photo', upload_to='photos/', null=True)

    def __str__(self):
        return self.name
