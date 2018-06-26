
from django import forms
from django.forms import fields,widgets

template_name = 'django/forms/widgets/text.html'
class Form(forms.Form):

    # def __init__(self,*args,**kwargs):
    #     super(Form,self).__init__(*args,**kwargs)
    #     self.fields

    name = fields.CharField(
        label='姓名',
        required=True,
        max_length=8,
        min_length=2,
        error_messages={
            'max_length':'最大值不能超过8位',
            'min_length':'最小不能超过2位'
        }
    )

    age = fields.IntegerField(
        label='年龄',
        error_messages={
            'invaild':'必须是数字'
        }
    )

    love = fields.IntegerField(
        widget=widgets.Select()
    )

    def __init__(self,*args,**kwargs):
        super(Form,self).__init__(*args,**kwargs)
        from app02.models import User
        self.fields["love"].widget.choices = User.objects.values_list('id','name')