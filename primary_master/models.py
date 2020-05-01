from django.db import models
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect


class Province(models.Model):
    code = models.IntegerField()
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False, null=False, blank=False)

    def __str__(self):
        return self.name_lc

class District(models.Model):
    code = models.IntegerField()
    province_id = models.ForeignKey(Province, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    
    def __str__(self):
        return self.name_lc

class LocalLevelType(models.Model):
    code = models.IntegerField()
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    
    def __str__(self):
        return self.name_lc

class LocalLevel(models.Model):
    code = models.IntegerField()
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    local_level_type_id = models.ForeignKey(LocalLevelType, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    wards_count = models.IntegerField(null=True)
    gps_lat = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    gps_long = models.DecimalField(max_digits=10,decimal_places=7, null=True)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    
class FiscalYear(models.Model):
    code = models.CharField(max_length=7)
    from_date_bs = models.CharField(max_length=10)
    from_date_ad = models.DateField()
    to_date_bs = models.CharField(max_length=10)
    to_date_ad = models.DateField()
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

class NepaliMonth(models.Model):
    code = models.IntegerField()
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    
class Gender(models.Model):
    code = models.CharField(max_length=10)
    name_en = models.CharField(max_length=50)
    name_lc = models.CharField(max_length=50)
    display_order = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False, null=False, blank=False)    

