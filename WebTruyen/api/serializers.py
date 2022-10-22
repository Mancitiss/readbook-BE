from rest_framework import serializers
from backend.models import Truyen,Chuong


class ChuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chuong
        fields = ('id',
                  'tr',
                  'us',
                  'stt_chuong',
                  'ch_ten',
                  'noi_dung')
class TruyenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truyen
        fields = ('id',
                  'tl',
                  'tr_ten',
                  'ngay_phat_hanh',
                  'tac_gia',
                  'anh',
                  'tong_so_tap',
                  'us',
                  'so_tap_da_phat_hanh',
                  'lich_phat_hanh',
                  'so_luot_thich',
                  'diem_danh_gia',
                  'so_luong_doc',
                  'mo_ta'
                  )



