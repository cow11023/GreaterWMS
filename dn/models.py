from django.db import models

class DnListModel(models.Model):
    dn_code = models.CharField(max_length=255, verbose_name="DN Code")
    dn_status = models.BigIntegerField(default=1, verbose_name="DN Status")
    total_weight = models.FloatField(default=0, verbose_name="Total Weight")
    total_volume = models.FloatField(default=0, verbose_name="Total Volume")
    customer = models.CharField(max_length=255, verbose_name="DN Customer")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    bar_code = models.CharField(max_length=255, verbose_name="Bar Code")
    back_order_label = models.BooleanField(default=False, verbose_name='Back Order Label')
    openid = models.CharField(max_length=255, verbose_name="Openid")
    transportation_fee = models.JSONField(default=dict, verbose_name="Transportation Fee")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'dnlist'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['-id']

    def __str__(self):
        return self.pk

class DnDetailModel(models.Model):
    dn_code = models.CharField(max_length=255, verbose_name="DN Code")
    dn_status = models.BigIntegerField(default=1, verbose_name="DN Status")
    customer = models.CharField(max_length=255, verbose_name="DN Customer")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    goods_qty = models.BigIntegerField(default=0, verbose_name="Goods QTY")
    pick_qty = models.BigIntegerField(default=0, verbose_name="Goods Pre Pick QTY")
    picked_qty = models.BigIntegerField(default=0, verbose_name="Goods Picked QTY")
    intransit_qty = models.BigIntegerField(default=0, verbose_name="Intransit QTY")
    delivery_actual_qty = models.BigIntegerField(default=0, verbose_name="Delivery Actual QTY")
    delivery_shortage_qty = models.BigIntegerField(default=0, verbose_name="Delivery Shortage QTY")
    delivery_more_qty = models.BigIntegerField(default=0, verbose_name="Delivery More QTY")
    delivery_damage_qty = models.BigIntegerField(default=0, verbose_name="Delivery More QTY")
    goods_weight = models.FloatField(default=0, verbose_name="Goods Weight")
    goods_volume = models.FloatField(default=0, verbose_name="Goods Volume")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    back_order_label = models.BooleanField(default=False, verbose_name='Back Order Label')
    openid = models.CharField(max_length=255, verbose_name="Openid")
    is_delete = models.BooleanField(default=False, verbose_name='Delete Label')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'dndetail'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['-id']

    def __str__(self):
        return self.pk

class PickingListModel(models.Model):
    dn_code = models.CharField(max_length=255, verbose_name="DN Code")
    bin_name = models.CharField(max_length=255, verbose_name="Bin Name")
    goods_code = models.CharField(max_length=255, verbose_name="Goods Code")
    pick_qty = models.BigIntegerField(default=0, verbose_name="Goods Pre Pick QTY")
    picked_qty = models.BigIntegerField(default=0, verbose_name="Picked QTY")
    creater = models.CharField(max_length=255, verbose_name="Who Created")
    t_code = models.CharField(max_length=255, verbose_name="Transaction Code")
    openid = models.CharField(max_length=255, verbose_name="Openid")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Create Time")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Update Time")

    class Meta:
        db_table = 'pickinglist'
        verbose_name = 'data id'
        verbose_name_plural = "data id"
        ordering = ['-id']

    def __str__(self):
        return self.pk
