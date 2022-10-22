from ctypes import addressof
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
    intro = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
class TheLoai(models.Model):
    # tl_id
    tl_ten = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.tl_ten
    
class Truyen(models.Model):
    # tr_id 
    tl = models.ManyToManyField('TheLoai', blank=True, null=True)
    tr_ten = models.CharField(max_length=255, null=False)
    ngay_phat_hanh = models.DateTimeField(auto_now_add=True)
    tac_gia = models.CharField(max_length=255, null=False)
    anh = models.ImageField(upload_to='uploads/%Y/%m')
    tong_so_tap = models.IntegerField()
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    so_tap_da_phat_hanh = models.IntegerField()
    lich_phat_hanh = models.TextField(null=True, blank=True)
    so_luot_thich = models.IntegerField()
    diem_danh_gia = models.DecimalField(max_digits=5, decimal_places=2)
    so_luong_doc = models.IntegerField()
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tl_ten

class Chuong(models.Model):
    # ch_id
    tr = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    stt_chuong = models.IntegerField()
    ch_ten = models.CharField(max_length=255, null=False)
    noi_dung = models.TextField(null=True, blank=True)

class YeuThich(models.Model):
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    tr = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    thoi_gian = models.DateTimeField(auto_now_add=True)

class BinhLuan(models.Model):
    # bl_id 
    tr = models.ForeignKey(Truyen, on_delete=models.CASCADE)
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    ch = models.ForeignKey(Chuong, on_delete=models.CASCADE)
    noi_dung = models.TextField(null=True, blank=True)
    thoi_gian = models.DateTimeField(auto_now_add=True)

class LichSu(models.Model):
    us = models.ForeignKey(User, on_delete=models.CASCADE)
    thoi_gian = models.DateTimeField(auto_now_add=True)
    ch = models.ForeignKey(Chuong, on_delete=models.CASCADE)
    tr = models.ForeignKey(Truyen, on_delete=models.CASCADE)