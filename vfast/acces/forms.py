#!/usr/bin/env python
#encoding=utf-8
from django import forms
from acces.models import Students

my_errors={'required':u'必须填写这个字段'} 

class StudentForm(forms.Form):
    name = forms.CharField(label='Student Name',max_length=10,error_messages=my_errors)
    age = forms.IntegerField(label='age',min_value=0,max_value=100)
    gender = forms.ChoiceField(label='gender',choices=Students.GENDER_CHOICE)
    mobile = forms.CharField(label='mobile',max_length=11)
    height = forms.IntegerField(label='height',required=False)
    weight = forms.IntegerField(label='weight',required=False)
