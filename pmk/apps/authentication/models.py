from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):

############################################################################################################################################
    #{% if request.user.profile. %}
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Меню
    menu_personal = models.BooleanField(default=False, verbose_name="Видеть в меню Табели Персонала")
    menu_driver = models.BooleanField(default=False, verbose_name="Видеть в меню Табели Водителей")
    menu_reference = models.BooleanField(default=False, verbose_name="Видеть в меню Справочник")
############################################################################################################################################
    # tp - tabel personal
    # Табели персонала главное
    tp_menu = models.BooleanField(default=False, verbose_name="Видеть меню табелей персонала")
    tp_view = models.BooleanField(default=False, verbose_name="Видеть все табели персонала")
    tp_add = models.BooleanField(default=False, verbose_name="Создавать табели персонала")
    tp_delete = models.BooleanField(default=False, verbose_name="Удалять табели персонала")

    # Просмотр Табеля Персонала:
    open_tp_view = models.BooleanField(default=False, verbose_name="Просмотр содержимого табеля персонала")
    open_tp_finance = models.BooleanField(default=False, verbose_name="Видеть финансовые данные в табеле персонала")
    open_tp_edit = models.BooleanField(default=False, verbose_name="Редактирование содержимого табеля персонала")

    # Сотрудники в Табелях Персонала:
    tp_add_personal = models.BooleanField(default=False, verbose_name="Добавление сотрудников в табель персонала")
    tp_move_personal = models.BooleanField(default=False, verbose_name="Перемещение сотрудников по группам в табеле персонала")
    tp_comment_personal = models.BooleanField(default=False, verbose_name="Оставлять комментарии в табеле персонала")
    tp_delete_personal = models.BooleanField(default=False, verbose_name="Удаление сотрудников из табелей персонала")

############################################################################################################################################
    # td - tabel driver
    # Табели водителей главное
    td_menu = models.BooleanField(default=False, verbose_name="Видеть меню табелей водителей")
    td_view = models.BooleanField(default=False, verbose_name="Видеть все табели водителей")
    td_add = models.BooleanField(default=False, verbose_name="Создавать табели водителей")
    td_delete = models.BooleanField(default=False, verbose_name="Удалять табели водителей")

    # Просмотр Табеля водителей:
    open_td_view = models.BooleanField(default=False, verbose_name="Просмотр содержимого табеля водителей")
    open_td_finance = models.BooleanField(default=False, verbose_name="Видеть финансовые данные в табеле персонала")
    open_td_edit = models.BooleanField(default=False, verbose_name="Редактирование содержимого табеля водителей")

    # Сотрудники в Табелях водителей:
    td_add_personal = models.BooleanField(default=False, verbose_name="Добавление сотрудников в табель водителей")
    td_move_personal = models.BooleanField(default=False, verbose_name="Перемещение сотрудников по группам в табеле водителей")
    td_comment_personal = models.BooleanField(default=False, verbose_name="Оставлять комментарии в табеле водителей")
    td_delete_personal = models.BooleanField(default=False, verbose_name="Удаление сотрудников из табелей водителей")

############################################################################################################################################
    # Справочник объектов
    view_obj = models.BooleanField(default=False, verbose_name="Видеть справочник объектов")
    add_obj = models.BooleanField(default=False, verbose_name="Добавлять объекты")

    # Справочник ТС
    view_ts = models.BooleanField(default=False, verbose_name="Видеть справочник ТС")
    add_ts = models.BooleanField(default=False, verbose_name="Добавлять ТС")

    # Справочник Групп
    view_group = models.BooleanField(default=False, verbose_name="Видеть справочник групп")
    add_group = models.BooleanField(default=False, verbose_name="Добавлять группы")

    # Справочник Должностей
    view_position = models.BooleanField(default=False, verbose_name="Видеть справочник должностей")
    add_position = models.BooleanField(default=False, verbose_name="Добавлять должности")

    # Справочник Разрядов
    view_grade = models.BooleanField(default=False, verbose_name="Видеть справочник разрядов")
    add_grade = models.BooleanField(default=False, verbose_name="Добавлять разряды")

    # Справочник Персонала
    view_personal = models.BooleanField(default=False, verbose_name="Видеть справочник персонала")
    add_personal = models.BooleanField(default=False, verbose_name="Добавлять персонал")
    edit_personal = models.BooleanField(default=False, verbose_name="Редактировать персонал")
    edit_tax_personal = models.BooleanField(default=False, verbose_name="Редактировать тариф водителя")
    search_personal = models.BooleanField(default=False, verbose_name="Поиск сотрудника по табелям")


    def __str__(self):
        return f"Профиль: {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()