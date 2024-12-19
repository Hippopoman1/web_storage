from django.db import models

from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # Store hashed passwords
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Stor(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)
    location = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    equipment_id = models.ForeignKey(Stor, on_delete=models.CASCADE)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()