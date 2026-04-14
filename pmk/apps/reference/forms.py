from .models import period,objs, automobile, persone, group, driver, agreement, temp_file, position
from django.forms import ModelForm, Textarea, Select, modelformset_factory, TextInput,DateInput, FileField
from django.contrib.auth.models import User
from django import forms


class TabForm(ModelForm):
    class Meta:
        model = period
        fields = ['type','obj','graphic','workdays']
        widgets = {
            'type':Select(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Наименование',
                'color': '#fff',
                'background': '#369',
            }),
            'obj':Select(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Объект',
                'color': '#fff',
                'background': '#369',
            }),
            'graphic': Select(attrs={
                'type': 'text',
                'class': 'form-control col-lg-2',
                'placeholder': 'Объект',
                'color': '#fff',
                'background': '#369',
            }),
            'workdays':TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Кол-во рабочих дней'
            })
        }


class DriverForm(ModelForm):
    class Meta:
        model = driver
        fields = ['obj']
        widgets = {
            'obj':Select(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Объект',
                'color': '#fff',
                'background': '#369',
            }),

        }

class ObjsForm(ModelForm):
    class Meta:
        model = objs
        fields = ['name','status']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            'status': Select(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Статус объекта',
                'color': '#fff',
                'background': '#369',
            }),
        }

class PositionForm(ModelForm):
    class Meta:
        model = position
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
        }


class GroupForm(ModelForm):
    class Meta:
        model = group
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
        }

class AutoForm(ModelForm):
    class Meta:
        model = automobile
        fields = ['name','owner','number']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Наименование',
                'style': 'width: 500%',
            }),
            'owner': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Собственник',
                'style': 'width: 500%',
            }),
            'number': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Гос. номер',
                'style': 'width: 500%',
            }),
        }


class PersoneForm(ModelForm):
    class Meta:
        model = persone
        fields = ['resident','company','phone_number', 'snils', 'full_name', 'group', 'position', 'salary', 'graphic', 'output','driver']
        widgets = {
            'resident': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'Гражданство',
                'color': '#fff',
                'background': '#369',
            }),
            'full_name': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            'snils': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'СНИЛС'
            }),
            'phone_number': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'group': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'Группа',
                'color': '#fff',
                'background': '#369',
            }),
            'position': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'Группа',
                'color': '#fff',
                'background': '#369',
            }),
            'salary': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Оклад'
            }),
            'graphic': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'График',
                'color': '#fff',
                'background': '#369',
            }),
            'driver': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'Водитель?',
                'color': '#fff',
                'background': '#369',
            }),
            'output': TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'placeholder': 'Выходные'
            }),
            'company': Select(attrs={
                'type': 'text',
                'class': 'form-control text-center',
                'placeholder': 'Организация',
                'color': '#fff',
                'background': '#369',
            }),
        }


class AgreementForm(ModelForm):
    class Meta:
        model = agreement
        fields = ['file']


class TempFileForm(ModelForm):
    class Meta:
        model = temp_file
        fields = ['temp']