from django.db import models

# Create your models here.
class Shop(models.Model):
    OPENING_STATUS = (
        ('open', '営業中'),
        ('closed', '本日休み'),
        ('preparing', '準備中')
    )

    STOCK_STATUS = (
        ('available', '在庫あり'),
        ('low', '残り少ない'),
        ('sold_out', '売り切れ'),
    )

    name = models.CharField('店舗名', max_length=100)
    description = models.TextField('店舗説明', max_length=1000, blank=True)
    address = models.CharField('住所', max_length=200, blank=True)
    opening_status = models.CharField('営業状況',max_length=20, choices=OPENING_STATUS, default='preparing')
    stock_status = models.CharField('在庫状況',max_length=20, choices=STOCK_STATUS, default='available')
    today_menu = models.TextField('本日のメニュー',max_length=1000, blank=True)
    special_notice_enabled = models.BooleanField('今だけ情報公開', default=False)
    special_notice = models.TextField('今だけ情報', max_length=1000, blank=True)
    updated_at = models.DateTimeField('最終更新日時', auto_now=True)

    class Meta:
        verbose_name = '店舗'
        verbose_name_plural = '店舗'