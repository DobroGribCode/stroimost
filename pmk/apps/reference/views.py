import datetime
import io
import random
import mimetypes
import os
import cherrypy
import openpyxl

from openpyxl import Workbook

from docx import Document
from docx.shared import Pt
from docx.shared import Inches
from docxtpl import DocxTemplate

from io import StringIO, BytesIO
from cherrypy.lib import file_generator

from random import randint
from random import randrange

from datetime import date
from wsgiref.util import FileWrapper
import mimetypes
import os, os.path

from django.core.files.base import File
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.base import File
from django.contrib.auth.decorators import login_required
from openpyxl.worksheet import worksheet
from django.conf import settings
from django.http import HttpResponse, Http404

from ..reference.forms import TabForm, ObjsForm, TaskForm, AutoForm, GroupForm,PersoneForm, DriverForm, AgreementForm, TempFileForm
from ..reference.models import persone, period,tabel_list, objs,task_head, task_body, group, automobile, driver, driver_list, agreement, agreement_accepter,agreement_step,accepter_list,agreementer_list, ender_list
from django.contrib.auth.models import User

# Create your views here.

class reference:
    @login_required(login_url="/login/")
    def ref(request):
        context = {'segment': 'ref'}
        html_template = loader.get_template('reference/ref.html')
        return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def objs(request):
        obj = objs.objects.all()
        context = {'obj': obj, 'segment': 'task'}
        html_template = loader.get_template('reference/object/objects.html')
        return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def new_object(request):
        obj = objs.objects.all()
        forms = ObjsForm
        if request.method == 'POST':
            forms = ObjsForm(request.POST)
            if forms.is_valid():
                post = forms.save(commit=False)
                post.save()
                return redirect('objs')
            else:
                erorr = 'Некорректные данные'
                context = {'segment': 'ref',
                           'obj': obj,
                           'forms': forms,
                           'erorr': erorr
                           }
                html_template = loader.get_template('reference/object/new_object.html')
                return HttpResponse(html_template.render(context, request))
        else:
            context = {'segment': 'ref',
                       'obj': obj,
                       'forms': forms
                       }
            html_template = loader.get_template('reference/object/new_object.html')
            return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def auto(request):
        auto = automobile.objects.all()
        context = {'auto': auto, 'segment': 'ref'}
        html_template = loader.get_template('reference/auto/auto.html')
        return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def new_auto(request):
        auto = automobile.objects.all()
        forms = AutoForm
        if request.method == 'POST':
            forms = AutoForm(request.POST)
            if forms.is_valid():
                post = forms.save(commit=False)
                post.save()
                return redirect('auto')
            else:
                erorr = 'Некорректные данные'
                context = {'segment': 'ref',
                            'auto': auto,
                            'forms': forms,
                            'erorr': erorr
                            }
                html_template = loader.get_template('reference/auto/new_auto.html')
                return HttpResponse(html_template.render(context, request))
        else:
            context = {'segment': 'ref',
                        'auto': auto,
                        'forms': forms
                        }
            html_template = loader.get_template('reference/auto/new_auto.html')
            return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def group(request):
        groups = group.objects.all()
        context = {'group': groups, 'segment': 'ref'}
        html_template = loader.get_template('reference/group/group.html')
        return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def new_group(request):
        groups = group.objects.all()
        forms = GroupForm
        if request.method == 'POST':
            forms = GroupForm(request.POST)
            if forms.is_valid():
                post = forms.save(commit=False)
                post.save()
                return redirect('group')
            else:
                erorr = 'Некорректные данные'
                context = {'segment': 'ref',
                           'group': groups,
                           'forms': forms,
                           'erorr': erorr
                           }
                html_template = loader.get_template('reference/group/new_group.html')
                return HttpResponse(html_template.render(context, request))
        else:
            context = {'segment': 'ref',
                       'group': groups,
                       'forms': forms
                       }
            html_template = loader.get_template('reference/group/new_group.html')
            return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def persones(request):
        pers = persone.objects.all()
        context = {'pers': pers, 'segment': 'ref'}
        html_template = loader.get_template('reference/persone/persones.html')
        return HttpResponse(html_template.render(context, request))

    @login_required(login_url="/login/")
    def new_persone(request):
        pers = persone.objects.all()
        forms = PersoneForm
        if request.method == 'POST':
            forms = PersoneForm(request.POST)
            if forms.is_valid():
                post = forms.save(commit=False)
                post.save()
                return redirect('persones')
            else:
                erorr = 'Некорректные данные'
                context = {'segment': 'ref',
                           'pers': pers,
                           'forms': forms,
                           'erorr': erorr
                           }
                html_template = loader.get_template('reference/persone/new_persone.html')
                return HttpResponse(html_template.render(context, request))
        else:
            context = {'segment': 'ref',
                       'pers': pers,
                       'forms': forms
                       }
            html_template = loader.get_template('reference/persone/new_persone.html')
            return HttpResponse(html_template.render(context, request))
