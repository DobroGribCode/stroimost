# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from ..home import views

urlpatterns = [



    # Лаборатория
    path('', views.tab.tabels, name='home'),
    path('notifications/', views.get_notifications, name='get_notifications'),
    path('get_notificated_data/', views.get_notificated_data, name='get_notificated_data'),
    path('update_notificated/', views.update_notificated, name='update_notificated'),
    # path('convert4', views.misc.convert4, name='convert4'),
    #path('convert5', views.misc.convert5, name='convert5'),
    path('convert6', views.misc.convert6, name='convert6'),
    #path('convert8', views.misc.convert8, name='convert8'),
    # path('convert12', views.misc.convert12, name='convert12'),
    path('notification_add', views.misc.notification_add, name='notification_add'),
    # path('convert2', views.misc.convert2, name='convert2'),
    # path('convert', views.misc.convert, name='convert'),
    # path('convert_tabel', views.misc.convert_tabel, name='convert_tabel'),
    # path('convert_driver', views.misc.convert_driver, name='convert_driver'),
    # path('auto_number', views.misc.auto_number, name='auto_number'),
    path('persones_info/<str:name>', views.misc.persones_info, name='persones_info/<str:name>'),
    path('month_info/<int:years>/<int:month>/<str:name>', views.misc.month_info, name='month_info/<int:years>/<int:month>/<str:name>'),
    path('month_info_driver/<int:years>/<int:month>/<str:name>', views.misc.month_info_driver, name='month_info_driver/<int:years>/<int:month>/<str:name>'),



    # Табели
    path('driver', views.tab.driver, name='driver'),
    path('new_driver', views.tab.new_driver, name='new_driver'),
    path('view_driver/<int:id>', views.tab.view_driver, name='view_driver/<int:id>'),
    path('view_driver_days/<int:id>', views.tab.view_driver_days, name='view_driver_days/<int:id>'),
    path('hexp_driver/<int:id>/<str:name>', views.tab.hexp_driver, name='hexp_driver/<int:id>/<str:name>'),
    path('group_move_tabelD/<int:ids>/<int:id>', views.tab.group_move_tabelD, name='group_move_tabelD/<int:ids>/<int:id>'),
    path('AddPersoneD/<int:id>/<int:ids>', views.tab.AddPersoneD, name='AddPersoneD/<int:id>/<int:ids>'),
    path('del_driverl/<int:id>/<int:ids>', views.tab.del_driverl, name='del_driverl/<int:id>/<int:ids>'),
    path('del_driver/<int:id>', views.tab.del_driver, name='del_driver/<int:id>'),
    path('approve_table/<int:day>/<int:ids>', views.tab.approve_table, name='approve_table/<int:day>/<int:ids>'),
    path('tabel', views.tab.tabel, name='tabel'),
    path('search/<int:id>', views.tab.search, name='search/<int:id>'),
    path('new_tabel', views.tab.new_tabel, name='new_tabel'),
    path('check_day/', views.tab.check_day_in_other_table, name='check_day_in_other_table'),
    path('save_input/', views.tab.save_input, name='save_input'),
    path('save_add/', views.tab.save_add, name='save_add'),
    path('save_auto/', views.tab.save_auto, name='save_auto'),
    path('view_tabel/<int:id>', views.tab.view_tabel, name='view_tabel/<int:id>'),
    path('hexp_tabel/<int:id>/<str:name>', views.tab.hexp_tabel, name='hexp_tabel/<int:id>/<str:name>'),
    path('del_tabel/<int:id>', views.tab.del_tabel, name='del_tabel/<int:id>'),
    path('del_tabl/<int:id>/<int:ids>', views.tab.del_tabl, name='del_tabl/<int:id>/<int:ids>'),
    path('approve_tableD/<int:day>/<int:ids>', views.tab.approve_tableD, name='approve_tableD/<int:day>/<int:ids>'),
    path('move_worker/<int:id>/<int:ids>/<int:gid>', views.tab.move_worker, name='move_worker/<int:id>/<int:ids>/<int:gid>'),
    path('group_move_tabel/<int:ids>/<int:id>', views.tab.group_move_tabel, name='group_move_tabel/<int:ids>/<int:id>'),
    path('AddPersone/<int:id>/<int:ids>', views.tab.AddPersone, name='AddPersone/<int:id>/<int:ids>'),


    # Справочник
    path('ref', views.reference.ref, name='ref'),
    path('objs', views.reference.objs, name='objs'),
    path('new_object', views.reference.new_object, name='new_object'),
    path('view_object/<int:id>', views.reference.view_object, name='view_object/<int:id>'),
    path('auto', views.reference.auto, name='auto'),
    path('new_auto', views.reference.new_auto, name='new_auto'),
    path('view_auto/<int:id>', views.reference.view_auto, name='view_auto/<int:id>'),
    path('group', views.reference.group, name='group'),
    path('new_group', views.reference.new_group, name='new_group'),
    path('view_group/<int:id>', views.reference.view_group, name='view_group/<int:id>'),
    path('position', views.reference.position, name='position'),
    path('new_position', views.reference.new_position, name='new_position'),
    path('view_position/<int:id>', views.reference.view_position, name='view_position/<int:id>'),
    path('reference/grade/save/', views.reference.grade_save, name='grade_save'),
    path('reference/grade/delete/', views.reference.grade_delete, name='grade_delete'),
    path('persones', views.reference.persones, name='persones'),
    path('persones_in_tabel', views.reference.persone_in_tabel, name='persones_in_tabel'),
    path('hexp_pit/<str:start_date>/<str:end_date>/<str:name>', views.reference.hexp_pit, name='hexp_pit/<str:start_date>/<str:end_date>/<str:name>'),
    path('save_idea/', views.reference.save_idea, name='save_idea'),
    path('new_persone', views.reference.new_persone, name='new_persone'),
    path('view_persone/<int:id>', views.reference.view_persone, name='view_persone/<int:id>'),
    path('get_grades/', views.reference.get_grades_by_position, name='get_grades'),


    #Утверждения
    path('agreements', views.Agreement.agreement_main, name='agreements'),
    path('agreement_file/<int:id>', views.Agreement.agreement_file, name='agreement_file/<int:id>'),
    path('view_agreement/<int:id>', views.Agreement.view_agreement, name='view_agreement/<int:id>'),
    path('new_agreement', views.Agreement.new_agreement, name='new_agreement'),
    path('correct_agreement/<int:id>/<int:ids>/<int:ida>', views.Agreement.correct_agreement, name='correct_agreement/<int:id>/<int:ids>/<int:ida>'),
    path('accept_agreement/<int:id>/<int:ids>/<int:ida>', views.Agreement.accept_agreement, name='accept_agreement/<int:id>/<int:ids>/<int:ida>'),
    path('agreemented/<int:id>/<int:ids>/<int:ida>', views.Agreement.agreemented, name='agreemented/<int:id>/<int:ids>'),
    path('close_agreement/<int:id>/<int:ids>/<int:ida>', views.Agreement.close_agreement, name='close_agreement/<int:id>/<int:ids>/<int:ida>'),
    path('new_file_agreement/<int:id>/<int:ids>/<int:ida>', views.Agreement.new_file_agreement, name='new_file_agreement/<int:id>/<int:ids>/<int:ida>'),


    #Половина
    # Открытие любых HTML файлов
    re_path(r'^.*\.*', views.pages, name='pages'),
]
