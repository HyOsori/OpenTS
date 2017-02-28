from django.db import models

# Create your models here.
class Data(models.Model):
    shcode = models.CharField(max_length=50, default='code')
    #종목코드
    date = models.CharField(max_length=50, default='date')
    #날짜
    open = models.IntegerField()
    #시가
    high = models.IntegerField()
    #고가
    low = models.IntegerField()
    #저가
    close = models.IntegerField()
    #종가
    sign = models.IntegerField()
    #전일대비구분
    change = models.IntegerField()
    #전일대비
    diff = models.FloatField()
    #등락율
    volume = models.IntegerField()
    #누적거래량
    diff_vol = models.FloatField()
    #거래증가율
    chdegree = models.FloatField()
    #체결강도
    sojinrate = models.FloatField()
    #소진율
    changerate = models.FloatField()
    #회전율
    fpvolume = models.IntegerField()
    #외인순매수
    covolume = models.IntegerField()
    #기관순매수
    value = models.IntegerField()
    #누적거래대금
    ppvolume = models.IntegerField()
    #개인순매수
    o_sign = models.IntegerField()
    #시가대비구분
    o_change = models.IntegerField()
    #시가대비
    o_diff = models.FloatField()
    #시가기준등락율
    h_sign = models.IntegerField()
    #고가대비구분
    h_change = models.IntegerField()
    #고가대비
    h_diff = models.FloatField()
    #고가기준등락율
    l_sign = models.IntegerField()
    #저가대비구분
    l_change = models.IntegerField()
    #저가대비
    l_diff = models.FloatField()
    #저가기준등락율
    marketcap = models.IntegerField()
    #시가총액(백만)