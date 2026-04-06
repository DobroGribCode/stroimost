import datetime

from django.db import models
from django.contrib.auth.models import User

class tabel_group(models.Model):
    date = models.DateField('Период группы', blank=True, null=True)
    comment = models.CharField('Комментарий',max_length=5000, blank=True,null=True)
    def __str__(self):
        return str(self.date)
    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Группа табелей'
        verbose_name_plural = 'Группы табелей'

class objs(models.Model):
    status = (('Открыт', 'Открыт'), ('Консервирован', 'Консервирован'), ('Завершен', 'Завершен'))
    prorab = models.ForeignKey(User,verbose_name='Прораб', related_name='Прораб',on_delete=models.PROTECT,blank=True, null=True)
    watch1 = models.ForeignKey(User,verbose_name='Наблюдатель1', related_name='Наблюдатель1',on_delete=models.PROTECT,blank=True, null=True)
    watch2 = models.ForeignKey(User,verbose_name='Наблюдатель2', related_name='Наблюдатель2',on_delete=models.PROTECT,blank=True, null=True)
    name = models.CharField('Наименование', max_length=450)
    status = models.CharField('Статус', max_length=55, choices=status, default=1)
    comment = models.CharField('Комментарий', max_length=5000, blank=True, null=True)
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

class group(models.Model):
    name = models.CharField('Наименование', max_length=50)
    comment = models.CharField('Комментарий',max_length=5000, blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class category(models.Model):
    name = models.CharField('Наименование', max_length=50)
    comment = models.CharField('Комментарий',max_length=5000, blank=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class automobile(models.Model):
    name = models.CharField('Наименование модели', max_length=125)
    owner = models.CharField('Собственник', max_length=125, default='Компания')
    comment = models.CharField('Комментарий',max_length=5000, blank=True,null=True)
    number = models.CharField('Гос. номер', max_length=125, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'


# Табели
class persone(models.Model):
    org_c = (
        (1, 'Оформлен'),
        (2, 'Неоформ'),
    )
    country_c = (
        ('РФ', 'РФ'),
        ('Иностранец', 'Иностранец'),
    )
    cat_c = ((1,'Геодезия'),(2,'ПТО'),(3,'Рабочие'),(4,'АУП'),(5,'МОП'))
    g = ((1,'Вахта'),(2,'5/7'),(3,'6/7'),(4,'2/2'),(5,'7'))
    d = ((1,'Водитель'),(0,'Нет'))

    resident = models.CharField('Гражданство', choices=country_c, null=True, blank=True, max_length=50)
    company = models.IntegerField('Организация', choices=org_c, null=True, blank=True)
    snils = models.CharField('СНИЛС', max_length=16, default='')
    inn = models.CharField('ИНН', max_length=12, default='', null=True,blank=True)
    full_name = models.CharField('ФИО', max_length=55)
    group = models.ForeignKey(group, verbose_name='Группа',on_delete=models.PROTECT,blank=True,null=True)
    position = models.CharField('Должность', max_length=55, null=True, blank=True)
    grade = models.CharField('Разряд', max_length=15, blank=True,null=True)
    driver = models.IntegerField('Водитель?',default=0, choices=d)
    salary = models.FloatField('Оклад', max_length=9,default=0, null=True, blank=True)
    exception = models.IntegerField('Исключение', default=0)
    sum_method = models.IntegerField('Метод расчета', default=0)
    graphic = models.IntegerField('График',default='1',choices=g, null=True, blank=True)
    output = models.IntegerField('Выходные',default=1,blank=True, null=True)
    date_accept = models.DateField('Дата приема', blank=True, null=True)
    date_leave = models.DateField('Дата увольнения', blank=True, null=True)
    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.PROTECT, blank=True, null=True)
    work_hours = models.CharField('Часы работы', max_length=55,default=10, null=True, blank=True)
    comment = models.CharField('Комментарий', max_length=5000, blank=True, null=True)
    idea = models.CharField('Заметки', max_length=5000, blank=True, null=True)
    leaved = models.IntegerField('Уволен?',default=0)
    phone_number = models.CharField('Номер телефона', max_length=17, default='', blank=True, null=True)
    workgroup = models.CharField('Отдел', max_length=52, blank=True, null=True)
    education = models.CharField('Образование', max_length=152, blank=True, null=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class persone_salary(models.Model):
    persone = models.ForeignKey(persone,verbose_name='Сотрудник', on_delete=models.CASCADE)
    date = models.DateField('Дата', default=datetime.date.today())
    salary = models.FloatField('Оклад', default=0,blank=True,null=True)
    grade = models.CharField('Разряд', max_length=15, blank=True,null=True)
    comment = models.CharField('Комментарий', blank=True,null=True, max_length=1024)
    def __str__(self):
        return f"{self.persone.full_name} {self.date.month}"
    class Meta:
        verbose_name = 'Оклад и разряд'
        verbose_name_plural = 'Оклады и разряды'

class driver_tax(models.Model):
    driver = models.ForeignKey(persone, verbose_name='Водитель',on_delete=models.PROTECT)
    tax = models.FloatField('Тариф', default=0)

    def __str__(self):
        return self.driver.full_name
    class Meta:
        verbose_name = 'Тариф водителя'
        verbose_name_plural = 'Тарифы водителей'

class driver_tax_lagacy(models.Model):
    driver = models.ForeignKey(persone, verbose_name='Водитель',on_delete=models.PROTECT)
    tax = models.FloatField('Тариф', default=0)
    date = models.DateField('Дата', blank=True, null=True)
    def __str__(self):
        return self.driver.full_name
    class Meta:
        verbose_name = 'Тариф водителя старые'
        verbose_name_plural = 'Тарифы водителей старые '


class driver(models.Model):
    date = models.DateField('Период', blank=True, null=True)
    obj = models.ForeignKey(objs, verbose_name='Объект', on_delete=models.PROTECT, blank=True,null=True, default=1)
    fullblock = models.IntegerField('Полная блокировка табеля', blank=True, null=True)
    dw1 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw2 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw3 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw4 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw5 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw6 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw7 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw8 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw9 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw10 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw11 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw12 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw13 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw14 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw15 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw16 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw17 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw18 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw19 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw20 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw21 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw22 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw23 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw24 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw25 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw26 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw27 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw28 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw29 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw30 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw31 = models.DateField('День недели', max_length=5, blank=True, null=True)
    db1 = models.IntegerField('Блокировка 1 дня', blank=True, null=True)
    db2 = models.IntegerField('Блокировка 2 дня', blank=True, null=True)
    db3 = models.IntegerField('Блокировка 3 дня', blank=True, null=True)
    db4 = models.IntegerField('Блокировка 4 дня', blank=True, null=True)
    db5 = models.IntegerField('Блокировка 5 дня', blank=True, null=True)
    db6 = models.IntegerField('Блокировка 6 дня', blank=True, null=True)
    db7 = models.IntegerField('Блокировка 7 дня', blank=True, null=True)
    db8 = models.IntegerField('Блокировка 8 дня', blank=True, null=True)
    db9 = models.IntegerField('Блокировка 9 дня', blank=True, null=True)
    db10 = models.IntegerField('Блокировка 10 дня', blank=True, null=True)
    db11 = models.IntegerField('Блокировка 11 дня', blank=True, null=True)
    db12 = models.IntegerField('Блокировка 12 дня', blank=True, null=True)
    db13 = models.IntegerField('Блокировка 13 дня', blank=True, null=True)
    db14 = models.IntegerField('Блокировка 14 дня', blank=True, null=True)
    db15 = models.IntegerField('Блокировка 15 дня', blank=True, null=True)
    db16 = models.IntegerField('Блокировка 16 дня', blank=True, null=True)
    db17 = models.IntegerField('Блокировка 17 дня', blank=True, null=True)
    db18 = models.IntegerField('Блокировка 18 дня', blank=True, null=True)
    db19 = models.IntegerField('Блокировка 19 дня', blank=True, null=True)
    db20 = models.IntegerField('Блокировка 20 дня', blank=True, null=True)
    db21 = models.IntegerField('Блокировка 21 дня', blank=True, null=True)
    db22 = models.IntegerField('Блокировка 22 дня', blank=True, null=True)
    db23 = models.IntegerField('Блокировка 23 дня', blank=True, null=True)
    db24 = models.IntegerField('Блокировка 24 дня', blank=True, null=True)
    db25 = models.IntegerField('Блокировка 25 дня', blank=True, null=True)
    db26 = models.IntegerField('Блокировка 26 дня', blank=True, null=True)
    db27 = models.IntegerField('Блокировка 27 дня', blank=True, null=True)
    db28 = models.IntegerField('Блокировка 28 дня', blank=True, null=True)
    db29 = models.IntegerField('Блокировка 29 дня', blank=True, null=True)
    db30 = models.IntegerField('Блокировка 30 дня', blank=True, null=True)
    db31 = models.IntegerField('Блокировка 31 дня', blank=True, null=True)
    da1 = models.IntegerField('Проверка 1 дня', blank=True, null=True)
    da2 = models.IntegerField('Проверка 2 дня', blank=True, null=True)
    da3 = models.IntegerField('Проверка 3 дня', blank=True, null=True)
    da4 = models.IntegerField('Проверка 4 дня', blank=True, null=True)
    da5 = models.IntegerField('Проверка 5 дня', blank=True, null=True)
    da6 = models.IntegerField('Проверка 6 дня', blank=True, null=True)
    da7 = models.IntegerField('Проверка 7 дня', blank=True, null=True)
    da8 = models.IntegerField('Проверка 8 дня', blank=True, null=True)
    da9 = models.IntegerField('Проверка 9 дня', blank=True, null=True)
    da10 = models.IntegerField('Проверка 10 дня', blank=True, null=True)
    da11 = models.IntegerField('Проверка 11 дня', blank=True, null=True)
    da12 = models.IntegerField('Проверка 12 дня', blank=True, null=True)
    da13 = models.IntegerField('Проверка 13 дня', blank=True, null=True)
    da14 = models.IntegerField('Проверка 14 дня', blank=True, null=True)
    da15 = models.IntegerField('Проверка 15 дня', blank=True, null=True)
    da16 = models.IntegerField('Проверка 16 дня', blank=True, null=True)
    da17 = models.IntegerField('Проверка 17 дня', blank=True, null=True)
    da18 = models.IntegerField('Проверка 18 дня', blank=True, null=True)
    da19 = models.IntegerField('Проверка 19 дня', blank=True, null=True)
    da20 = models.IntegerField('Проверка 20 дня', blank=True, null=True)
    da21 = models.IntegerField('Проверка 21 дня', blank=True, null=True)
    da22 = models.IntegerField('Проверка 22 дня', blank=True, null=True)
    da23 = models.IntegerField('Проверка 23 дня', blank=True, null=True)
    da24 = models.IntegerField('Проверка 24 дня', blank=True, null=True)
    da25 = models.IntegerField('Проверка 25 дня', blank=True, null=True)
    da26 = models.IntegerField('Проверка 26 дня', blank=True, null=True)
    da27 = models.IntegerField('Проверка 27 дня', blank=True, null=True)
    da28 = models.IntegerField('Проверка 28 дня', blank=True, null=True)
    da29 = models.IntegerField('Проверка 29 дня', blank=True, null=True)
    da30 = models.IntegerField('Проверка 30 дня', blank=True, null=True)
    da31 = models.IntegerField('Проверка 31 дня', blank=True, null=True)

    def __str__(self):
        return str(self.date)
    class Meta:
        ordering = ['-id', ]
        verbose_name = 'Табель водителя'
        verbose_name_plural = 'Табели водителей'


class dayapproved(models.Model):
    approver = models.ForeignKey(User,related_name='ПодтвердившийВ', verbose_name='ПодтвердившийВ', on_delete=models.PROTECT, blank=True,null=True, default=1)
    per = models.ForeignKey(driver,related_name='ТабельВ', verbose_name='ТабельВ', on_delete=models.PROTECT, blank=True,null=True, default=1)
    day = models.IntegerField('День')
    time = models.DateTimeField('Время проверки', blank=True,null=True)
    def __str__(self):
        return str(str(self.approver.username) +' подтвердил '+ str(self.day) + 'день в табель от ' + str(self.per))
    class Meta:
        verbose_name = 'Проверка дня'
        verbose_name_plural = 'Проверки дней'



class driver_list(models.Model):
    period = models.ForeignKey(driver, verbose_name='Период',on_delete=models.PROTECT, blank=True, null=True)
    persone = models.ForeignKey(persone, verbose_name='Сотрудник',on_delete=models.PROTECT, blank=True, null=True)
    company = models.CharField('Организация', max_length=15, blank=True, null=True)
    full_name = models.CharField('ФИО', max_length=55, blank=True, null=True)
    sum = models.FloatField('Расчетная', max_length=15, blank=True, null=True)
    comment = models.CharField('Комментарий', max_length=999,blank=True,null=True)
    salary = models.FloatField('Итог', max_length=15, blank=True, null=True)
    position = models.CharField('Должность', max_length=55, blank=True, null=True)
    fine = models.FloatField('Штраф', max_length=8, blank=True,null=True)
    add = models.FloatField('Премия', max_length=8, blank=True,null=True)
    auto = models.ForeignKey(automobile, verbose_name='Т/С', on_delete=models.PROTECT, blank=True, null=True)
    salaryedit = models.IntegerField('Изменение итога', default=0)
    salared = models.FloatField('Начисленно', max_length=15, blank=True,null=True)
    block = models.IntegerField('Открытые дни', default=3)
    days = models.IntegerField('Сумма дней', default=0)
    hours = models.IntegerField('Часы работы', default=0)
    used = models.IntegerField('Использованно выходных',blank=True,null=True,default=0)
    output = models.IntegerField('Выходные',default=1,blank=True,null=True)
    auto_block = models.IntegerField('Блокировка Т\С', blank=True, null=True)
    d1 = models.CharField('День', max_length=5, blank=True, null=True)
    d1c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d2 = models.CharField('День', max_length=5, blank=True, null=True)
    d2c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d3 = models.CharField('День', max_length=5, blank=True, null=True)
    d3c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d4 = models.CharField('День', max_length=5, blank=True, null=True)
    d4c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d5 = models.CharField('День', max_length=5, blank=True, null=True)
    d5c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d6 = models.CharField('День', max_length=5, blank=True, null=True)
    d6c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d7 = models.CharField('День', max_length=5, blank=True, null=True)
    d7c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d8 = models.CharField('День', max_length=5, blank=True, null=True)
    d8c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d9 = models.CharField('День', max_length=5, blank=True, null=True)
    d9c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d10 = models.CharField('День', max_length=5, blank=True, null=True)
    d10c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d11 = models.CharField('День', max_length=5, blank=True, null=True)
    d11c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d12 = models.CharField('День', max_length=5, blank=True, null=True)
    d12c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d13 = models.CharField('День', max_length=5, blank=True, null=True)
    d13c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d14 = models.CharField('День', max_length=5, blank=True, null=True)
    d14c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d15 = models.CharField('День', max_length=5, blank=True, null=True)
    d15c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d16 = models.CharField('День', max_length=5, blank=True, null=True)
    d16c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d17 = models.CharField('День', max_length=5, blank=True, null=True)
    d17c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d18 = models.CharField('День', max_length=5, blank=True, null=True)
    d18c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d19 = models.CharField('День', max_length=5, blank=True, null=True)
    d19c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d20 = models.CharField('День', max_length=5, blank=True, null=True)
    d20c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d21 = models.CharField('День', max_length=5, blank=True, null=True)
    d21c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d22 = models.CharField('День', max_length=5, blank=True, null=True)
    d22c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d23 = models.CharField('День', max_length=5, blank=True, null=True)
    d23c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d24 = models.CharField('День', max_length=5, blank=True, null=True)
    d24c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d25 = models.CharField('День', max_length=5, blank=True, null=True)
    d25c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d26 = models.CharField('День', max_length=5, blank=True, null=True)
    d26c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d27 = models.CharField('День', max_length=5, blank=True, null=True)
    d27c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d28 = models.CharField('День', max_length=5, blank=True, null=True)
    d28c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d29 = models.CharField('День', max_length=5, blank=True, null=True)
    d29c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d30 = models.CharField('День', max_length=5, blank=True, null=True)
    d30c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d31 = models.CharField('День', max_length=5, blank=True, null=True)
    d31c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    db1 = models.IntegerField('Блокировка 1 дня', blank=True, null=True)
    db2 = models.IntegerField('Блокировка 2 дня', blank=True, null=True)
    db3 = models.IntegerField('Блокировка 3 дня', blank=True, null=True)
    db4 = models.IntegerField('Блокировка 4 дня', blank=True, null=True)
    db5 = models.IntegerField('Блокировка 5 дня', blank=True, null=True)
    db6 = models.IntegerField('Блокировка 6 дня', blank=True, null=True)
    db7 = models.IntegerField('Блокировка 7 дня', blank=True, null=True)
    db8 = models.IntegerField('Блокировка 8 дня', blank=True, null=True)
    db9 = models.IntegerField('Блокировка 9 дня', blank=True, null=True)
    db10 = models.IntegerField('Блокировка 10 дня', blank=True, null=True)
    db11 = models.IntegerField('Блокировка 11 дня', blank=True, null=True)
    db12 = models.IntegerField('Блокировка 12 дня', blank=True, null=True)
    db13 = models.IntegerField('Блокировка 13 дня', blank=True, null=True)
    db14 = models.IntegerField('Блокировка 14 дня', blank=True, null=True)
    db15 = models.IntegerField('Блокировка 15 дня', blank=True, null=True)
    db16 = models.IntegerField('Блокировка 16 дня', blank=True, null=True)
    db17 = models.IntegerField('Блокировка 17 дня', blank=True, null=True)
    db18 = models.IntegerField('Блокировка 18 дня', blank=True, null=True)
    db19 = models.IntegerField('Блокировка 19 дня', blank=True, null=True)
    db20 = models.IntegerField('Блокировка 20 дня', blank=True, null=True)
    db21 = models.IntegerField('Блокировка 21 дня', blank=True, null=True)
    db22 = models.IntegerField('Блокировка 22 дня', blank=True, null=True)
    db23 = models.IntegerField('Блокировка 23 дня', blank=True, null=True)
    db24 = models.IntegerField('Блокировка 24 дня', blank=True, null=True)
    db25 = models.IntegerField('Блокировка 25 дня', blank=True, null=True)
    db26 = models.IntegerField('Блокировка 26 дня', blank=True, null=True)
    db27 = models.IntegerField('Блокировка 27 дня', blank=True, null=True)
    db28 = models.IntegerField('Блокировка 28 дня', blank=True, null=True)
    db29 = models.IntegerField('Блокировка 29 дня', blank=True, null=True)
    db30 = models.IntegerField('Блокировка 30 дня', blank=True, null=True)
    db31 = models.IntegerField('Блокировка 31 дня', blank=True, null=True)
    daypicker1 = models.ForeignKey(User, related_name='d1', on_delete=models.PROTECT, verbose_name='Кто установил 1 дня', blank=True, null=True)
    daypicker2 = models.ForeignKey(User, related_name='d2', on_delete=models.PROTECT, verbose_name='Кто установил 2 дня', blank=True, null=True)
    daypicker3 = models.ForeignKey(User, related_name='d3', on_delete=models.PROTECT, verbose_name='Кто установил 3 дня', blank=True, null=True)
    daypicker4 = models.ForeignKey(User, related_name='d4', on_delete=models.PROTECT, verbose_name='Кто установил 4 дня', blank=True, null=True)
    daypicker5 = models.ForeignKey(User, related_name='d5', on_delete=models.PROTECT, verbose_name='Кто установил 5 дня', blank=True, null=True)
    daypicker6 = models.ForeignKey(User, related_name='d6', on_delete=models.PROTECT, verbose_name='Кто установил 6 дня', blank=True, null=True)
    daypicker7 = models.ForeignKey(User, related_name='d7', on_delete=models.PROTECT, verbose_name='Кто установил 7 дня', blank=True, null=True)
    daypicker8 = models.ForeignKey(User, related_name='d8', on_delete=models.PROTECT, verbose_name='Кто установил 8 дня', blank=True, null=True)
    daypicker9 = models.ForeignKey(User, related_name='d9', on_delete=models.PROTECT, verbose_name='Кто установил 9 дня', blank=True, null=True)
    daypicker10 = models.ForeignKey(User, related_name='d10', on_delete=models.PROTECT, verbose_name='Кто установил 10 дня', blank=True, null=True)
    daypicker11 = models.ForeignKey(User, related_name='d11', on_delete=models.PROTECT, verbose_name='Кто установил 11 дня', blank=True, null=True)
    daypicker12 = models.ForeignKey(User, related_name='d12', on_delete=models.PROTECT, verbose_name='Кто установил 12 дня', blank=True, null=True)
    daypicker13 = models.ForeignKey(User, related_name='d13', on_delete=models.PROTECT, verbose_name='Кто установил 13 дня', blank=True, null=True)
    daypicker14 = models.ForeignKey(User, related_name='d14', on_delete=models.PROTECT, verbose_name='Кто установил 14 дня', blank=True, null=True)
    daypicker15 = models.ForeignKey(User, related_name='d15', on_delete=models.PROTECT, verbose_name='Кто установил 15 дня', blank=True, null=True)
    daypicker16 = models.ForeignKey(User, related_name='d16', on_delete=models.PROTECT, verbose_name='Кто установил 16 дня', blank=True, null=True)
    daypicker17 = models.ForeignKey(User, related_name='d17', on_delete=models.PROTECT, verbose_name='Кто установил 17 дня', blank=True, null=True)
    daypicker18 = models.ForeignKey(User, related_name='d18', on_delete=models.PROTECT, verbose_name='Кто установил 18 дня', blank=True, null=True)
    daypicker19 = models.ForeignKey(User, related_name='d19', on_delete=models.PROTECT, verbose_name='Кто установил 19 дня', blank=True, null=True)
    daypicker20 = models.ForeignKey(User, related_name='d20', on_delete=models.PROTECT, verbose_name='Кто установил 20 дня', blank=True, null=True)
    daypicker21 = models.ForeignKey(User, related_name='d21', on_delete=models.PROTECT, verbose_name='Кто установил 21 дня', blank=True, null=True)
    daypicker22 = models.ForeignKey(User, related_name='d22', on_delete=models.PROTECT, verbose_name='Кто установил 22 дня', blank=True, null=True)
    daypicker23 = models.ForeignKey(User, related_name='d23', on_delete=models.PROTECT, verbose_name='Кто установил 23 дня', blank=True, null=True)
    daypicker24 = models.ForeignKey(User, related_name='d24', on_delete=models.PROTECT, verbose_name='Кто установил 24 дня', blank=True, null=True)
    daypicker25 = models.ForeignKey(User, related_name='d25', on_delete=models.PROTECT, verbose_name='Кто установил 25 дня', blank=True, null=True)
    daypicker26 = models.ForeignKey(User, related_name='d26', on_delete=models.PROTECT, verbose_name='Кто установил 26 дня', blank=True, null=True)
    daypicker27 = models.ForeignKey(User, related_name='d27', on_delete=models.PROTECT, verbose_name='Кто установил 27 дня', blank=True, null=True)
    daypicker28 = models.ForeignKey(User, related_name='d28', on_delete=models.PROTECT, verbose_name='Кто установил 28 дня', blank=True, null=True)
    daypicker29 = models.ForeignKey(User, related_name='d29', on_delete=models.PROTECT, verbose_name='Кто установил 29 дня', blank=True, null=True)
    daypicker30 = models.ForeignKey(User, related_name='d30', on_delete=models.PROTECT, verbose_name='Кто установил 30 дня', blank=True, null=True)
    daypicker31 = models.ForeignKey(User, related_name='d31', on_delete=models.PROTECT, verbose_name='Кто установил 31 дня', blank=True, null=True)
    comment = models.CharField('Комментарий', max_length=950, blank=True,null=True)

    def __str__(self):
        return str(self.full_name)
    class Meta:
        verbose_name = 'Список в табели водителей'
        verbose_name_plural = 'Списки в табелях водителей'


class period(models.Model):
    g = ((1, 'Вахта'), (5, '5/7'), (6, '6/7'), (2, '2/2'))
    t = ((1, 'Геодезия'),(2,'ПТО'), (3, 'Рабочие'), (4, 'АУП'), (5, 'Кухня'))
    type = models.IntegerField('Тип табеля', default=1,choices=t)
    date = models.DateField('Период', blank=True, null=True)
    graphic = models.IntegerField('График', blank=True, null=True, choices=g)
    obj = models.ForeignKey(objs, verbose_name='Объект', on_delete=models.PROTECT, blank=True,null=True, default=1)
    workdays = models.IntegerField('Количество рабочих дней', blank=True, default=30)
    workdays5 = models.IntegerField('Количество рабочих дней графика 5/2', blank=True, default=22)
    fullblock = models.IntegerField('Полная блокировка табеля', blank=True, null=True)
    group = models.ForeignKey(tabel_group,verbose_name='Группа табелей персонала',related_name='Группа',on_delete=models.CASCADE, blank=True,null=True)
    dw1 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw2 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw3 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw4 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw5 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw6 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw7 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw8 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw9 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw10 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw11 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw12 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw13 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw14 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw15 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw16 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw17 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw18 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw19 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw20 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw21 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw22 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw23 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw24 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw25 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw26 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw27 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw28 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw29 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw30 = models.DateField('День недели', max_length=5, blank=True, null=True)
    dw31 = models.DateField('День недели', max_length=5, blank=True, null=True)
    db1 = models.IntegerField('Блокировка 1 дня', blank=True, null=True)
    db2 = models.IntegerField('Блокировка 2 дня', blank=True, null=True)
    db3 = models.IntegerField('Блокировка 3 дня', blank=True, null=True)
    db4 = models.IntegerField('Блокировка 4 дня', blank=True, null=True)
    db5 = models.IntegerField('Блокировка 5 дня', blank=True, null=True)
    db6 = models.IntegerField('Блокировка 6 дня', blank=True, null=True)
    db7 = models.IntegerField('Блокировка 7 дня', blank=True, null=True)
    db8 = models.IntegerField('Блокировка 8 дня', blank=True, null=True)
    db9 = models.IntegerField('Блокировка 9 дня', blank=True, null=True)
    db10 = models.IntegerField('Блокировка 10 дня', blank=True, null=True)
    db11 = models.IntegerField('Блокировка 11 дня', blank=True, null=True)
    db12 = models.IntegerField('Блокировка 12 дня', blank=True, null=True)
    db13 = models.IntegerField('Блокировка 13 дня', blank=True, null=True)
    db14 = models.IntegerField('Блокировка 14 дня', blank=True, null=True)
    db15 = models.IntegerField('Блокировка 15 дня', blank=True, null=True)
    db16 = models.IntegerField('Блокировка 16 дня', blank=True, null=True)
    db17 = models.IntegerField('Блокировка 17 дня', blank=True, null=True)
    db18 = models.IntegerField('Блокировка 18 дня', blank=True, null=True)
    db19 = models.IntegerField('Блокировка 19 дня', blank=True, null=True)
    db20 = models.IntegerField('Блокировка 20 дня', blank=True, null=True)
    db21 = models.IntegerField('Блокировка 21 дня', blank=True, null=True)
    db22 = models.IntegerField('Блокировка 22 дня', blank=True, null=True)
    db23 = models.IntegerField('Блокировка 23 дня', blank=True, null=True)
    db24 = models.IntegerField('Блокировка 24 дня', blank=True, null=True)
    db25 = models.IntegerField('Блокировка 25 дня', blank=True, null=True)
    db26 = models.IntegerField('Блокировка 26 дня', blank=True, null=True)
    db27 = models.IntegerField('Блокировка 27 дня', blank=True, null=True)
    db28 = models.IntegerField('Блокировка 28 дня', blank=True, null=True)
    db29 = models.IntegerField('Блокировка 29 дня', blank=True, null=True)
    db30 = models.IntegerField('Блокировка 30 дня', blank=True, null=True)
    db31 = models.IntegerField('Блокировка 31 дня', blank=True, null=True)
    da1 = models.IntegerField('Проверка 1 дня', blank=True, null=True)
    da2 = models.IntegerField('Проверка 2 дня', blank=True, null=True)
    da3 = models.IntegerField('Проверка 3 дня', blank=True, null=True)
    da4 = models.IntegerField('Проверка 4 дня', blank=True, null=True)
    da5 = models.IntegerField('Проверка 5 дня', blank=True, null=True)
    da6 = models.IntegerField('Проверка 6 дня', blank=True, null=True)
    da7 = models.IntegerField('Проверка 7 дня', blank=True, null=True)
    da8 = models.IntegerField('Проверка 8 дня', blank=True, null=True)
    da9 = models.IntegerField('Проверка 9 дня', blank=True, null=True)
    da10 = models.IntegerField('Проверка 10 дня', blank=True, null=True)
    da11 = models.IntegerField('Проверка 11 дня', blank=True, null=True)
    da12 = models.IntegerField('Проверка 12 дня', blank=True, null=True)
    da13 = models.IntegerField('Проверка 13 дня', blank=True, null=True)
    da14 = models.IntegerField('Проверка 14 дня', blank=True, null=True)
    da15 = models.IntegerField('Проверка 15 дня', blank=True, null=True)
    da16 = models.IntegerField('Проверка 16 дня', blank=True, null=True)
    da17 = models.IntegerField('Проверка 17 дня', blank=True, null=True)
    da18 = models.IntegerField('Проверка 18 дня', blank=True, null=True)
    da19 = models.IntegerField('Проверка 19 дня', blank=True, null=True)
    da20 = models.IntegerField('Проверка 20 дня', blank=True, null=True)
    da21 = models.IntegerField('Проверка 21 дня', blank=True, null=True)
    da22 = models.IntegerField('Проверка 22 дня', blank=True, null=True)
    da23 = models.IntegerField('Проверка 23 дня', blank=True, null=True)
    da24 = models.IntegerField('Проверка 24 дня', blank=True, null=True)
    da25 = models.IntegerField('Проверка 25 дня', blank=True, null=True)
    da26 = models.IntegerField('Проверка 26 дня', blank=True, null=True)
    da27 = models.IntegerField('Проверка 27 дня', blank=True, null=True)
    da28 = models.IntegerField('Проверка 28 дня', blank=True, null=True)
    da29 = models.IntegerField('Проверка 29 дня', blank=True, null=True)
    da30 = models.IntegerField('Проверка 30 дня', blank=True, null=True)
    da31 = models.IntegerField('Проверка 31 дня', blank=True, null=True)

    def __str__(self):
        return str(self.date)+str(self.obj)+str(self.type)
    class Meta:
        ordering = ['-id',]
        verbose_name = 'Табель персонала'
        verbose_name_plural = 'Табели персонала'

class dayapprove(models.Model):
    approver = models.ForeignKey(User,related_name='Подтвердивший', verbose_name='Подтвердивший', on_delete=models.PROTECT, blank=True,null=True, default=1)
    per = models.ForeignKey(period,related_name='Табель', verbose_name='Табель', on_delete=models.PROTECT, blank=True,null=True, default=1)
    day = models.IntegerField('День')
    time = models.DateTimeField('Время проверки', blank=True,null=True)
    def __str__(self):
        return str(str(self.approver.username) +' подтвердил '+ str(self.day) + 'день в табель от ' + str(self.per))
    class Meta:
        verbose_name = 'Проверка дня'
        verbose_name_plural = 'Проверки дней'


class tabel_list(models.Model):
    period = models.ForeignKey(period,verbose_name='Период',on_delete=models.PROTECT, blank=True, null=True)
    persone = models.ForeignKey(persone, verbose_name='Сотрудник',on_delete=models.PROTECT, blank=True, null=True)
    graphic = models.IntegerField('График',default=1, null=True, blank=True)
    company = models.CharField('Организация', max_length=15, blank=True, null=True)
    snils = models.CharField('СНИЛС', max_length=16, blank=True, null=True)
    full_name = models.CharField('ФИО', max_length=55, blank=True, null=True)
    group = models.ForeignKey(group, verbose_name='Группа', on_delete=models.PROTECT, blank=True, null=True)
    category = models.CharField('Категория', max_length=15, blank=True, null=True)
    position = models.CharField('Должность', max_length=55, blank=True, null=True)
    sum = models.FloatField('Расчетная', max_length=15, blank=True, null=True)
    salary = models.FloatField('Итог', max_length=15, blank=True, null=True)
    hours = models.IntegerField('Часы работы', default=0)
    output = models.IntegerField('Выходные',default=1,blank=True,null=True)
    used = models.IntegerField('Использованно выходных',blank=True,null=True,default=0)
    comment = models.CharField('Комментарий', max_length=999,blank=True,null=True)
    fine = models.FloatField('Штраф', max_length=8, blank=True,null=True)
    add = models.FloatField('Премия', max_length=8, blank=True,null=True)
    salaryedit = models.IntegerField('Изменение итога', default=0)
    salared = models.FloatField('Начисленно', max_length=15, blank=True,null=True)
    block = models.IntegerField('Открытые дни', default=3)
    days = models.IntegerField('Сумма дней', default=0)
    d1 = models.CharField('День', max_length=5, blank=True, null=True)
    d1c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d2 = models.CharField('День', max_length=5, blank=True, null=True)
    d2c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d3 = models.CharField('День', max_length=5, blank=True, null=True)
    d3c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d4 = models.CharField('День', max_length=5, blank=True, null=True)
    d4c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d5 = models.CharField('День', max_length=5, blank=True, null=True)
    d5c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d6 = models.CharField('День', max_length=5, blank=True, null=True)
    d6c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d7 = models.CharField('День', max_length=5, blank=True, null=True)
    d7c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d8 = models.CharField('День', max_length=5, blank=True, null=True)
    d8c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d9 = models.CharField('День', max_length=5, blank=True, null=True)
    d9c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d10 = models.CharField('День', max_length=5, blank=True, null=True)
    d10c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d11 = models.CharField('День', max_length=5, blank=True, null=True)
    d11c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d12 = models.CharField('День', max_length=5, blank=True, null=True)
    d12c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d13 = models.CharField('День', max_length=5, blank=True, null=True)
    d13c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d14 = models.CharField('День', max_length=5, blank=True, null=True)
    d14c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d15 = models.CharField('День', max_length=5, blank=True, null=True)
    d15c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d16 = models.CharField('День', max_length=5, blank=True, null=True)
    d16c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d17 = models.CharField('День', max_length=5, blank=True, null=True)
    d17c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d18 = models.CharField('День', max_length=5, blank=True, null=True)
    d18c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d19 = models.CharField('День', max_length=5, blank=True, null=True)
    d19c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d20 = models.CharField('День', max_length=5, blank=True, null=True)
    d20c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d21 = models.CharField('День', max_length=5, blank=True, null=True)
    d21c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d22 = models.CharField('День', max_length=5, blank=True, null=True)
    d22c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d23 = models.CharField('День', max_length=5, blank=True, null=True)
    d23c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d24 = models.CharField('День', max_length=5, blank=True, null=True)
    d24c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d25 = models.CharField('День', max_length=5, blank=True, null=True)
    d25c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d26 = models.CharField('День', max_length=5, blank=True, null=True)
    d26c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d27 = models.CharField('День', max_length=5, blank=True, null=True)
    d27c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d28 = models.CharField('День', max_length=5, blank=True, null=True)
    d28c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d29 = models.CharField('День', max_length=5, blank=True, null=True)
    d29c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d30 = models.CharField('День', max_length=5, blank=True, null=True)
    d30c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    d31 = models.CharField('День', max_length=5, blank=True, null=True)
    d31c = models.CharField('Цвет фона', max_length=15, blank=True, null=True)
    daypicker1 = models.ForeignKey(User, related_name='dt1', on_delete=models.PROTECT, verbose_name='Кто установил 1 дня', blank=True, null=True)
    daypicker2 = models.ForeignKey(User, related_name='dt2', on_delete=models.PROTECT, verbose_name='Кто установил 2 дня', blank=True, null=True)
    daypicker3 = models.ForeignKey(User, related_name='dt3', on_delete=models.PROTECT, verbose_name='Кто установил 3 дня', blank=True, null=True)
    daypicker4 = models.ForeignKey(User, related_name='dt4', on_delete=models.PROTECT, verbose_name='Кто установил 4 дня', blank=True, null=True)
    daypicker5 = models.ForeignKey(User, related_name='dt5', on_delete=models.PROTECT, verbose_name='Кто установил 5 дня', blank=True, null=True)
    daypicker6 = models.ForeignKey(User, related_name='dt6', on_delete=models.PROTECT, verbose_name='Кто установил 6 дня', blank=True, null=True)
    daypicker7 = models.ForeignKey(User, related_name='dt7', on_delete=models.PROTECT, verbose_name='Кто установил 7 дня', blank=True, null=True)
    daypicker8 = models.ForeignKey(User, related_name='dt8', on_delete=models.PROTECT, verbose_name='Кто установил 8 дня', blank=True, null=True)
    daypicker9 = models.ForeignKey(User, related_name='dt9', on_delete=models.PROTECT, verbose_name='Кто установил 9 дня', blank=True, null=True)
    daypicker10 = models.ForeignKey(User, related_name='dt10', on_delete=models.PROTECT, verbose_name='Кто установил 10 дня', blank=True, null=True)
    daypicker11 = models.ForeignKey(User, related_name='dt11', on_delete=models.PROTECT, verbose_name='Кто установил 11 дня', blank=True, null=True)
    daypicker12 = models.ForeignKey(User, related_name='dt12', on_delete=models.PROTECT, verbose_name='Кто установил 12 дня', blank=True, null=True)
    daypicker13 = models.ForeignKey(User, related_name='dt13', on_delete=models.PROTECT, verbose_name='Кто установил 13 дня', blank=True, null=True)
    daypicker14 = models.ForeignKey(User, related_name='dt14', on_delete=models.PROTECT, verbose_name='Кто установил 14 дня', blank=True, null=True)
    daypicker15 = models.ForeignKey(User, related_name='dt15', on_delete=models.PROTECT, verbose_name='Кто установил 15 дня', blank=True, null=True)
    daypicker16 = models.ForeignKey(User, related_name='dt16', on_delete=models.PROTECT, verbose_name='Кто установил 16 дня', blank=True, null=True)
    daypicker17 = models.ForeignKey(User, related_name='dt17', on_delete=models.PROTECT, verbose_name='Кто установил 17 дня', blank=True, null=True)
    daypicker18 = models.ForeignKey(User, related_name='dt18', on_delete=models.PROTECT, verbose_name='Кто установил 18 дня', blank=True, null=True)
    daypicker19 = models.ForeignKey(User, related_name='dt19', on_delete=models.PROTECT, verbose_name='Кто установил 19 дня', blank=True, null=True)
    daypicker20 = models.ForeignKey(User, related_name='dt20', on_delete=models.PROTECT, verbose_name='Кто установил 20 дня', blank=True, null=True)
    daypicker21 = models.ForeignKey(User, related_name='dt21', on_delete=models.PROTECT, verbose_name='Кто установил 21 дня', blank=True, null=True)
    daypicker22 = models.ForeignKey(User, related_name='dt22', on_delete=models.PROTECT, verbose_name='Кто установил 22 дня', blank=True, null=True)
    daypicker23 = models.ForeignKey(User, related_name='dt23', on_delete=models.PROTECT, verbose_name='Кто установил 23 дня', blank=True, null=True)
    daypicker24 = models.ForeignKey(User, related_name='dt24', on_delete=models.PROTECT, verbose_name='Кто установил 24 дня', blank=True, null=True)
    daypicker25 = models.ForeignKey(User, related_name='dt25', on_delete=models.PROTECT, verbose_name='Кто установил 25 дня', blank=True, null=True)
    daypicker26 = models.ForeignKey(User, related_name='dt26', on_delete=models.PROTECT, verbose_name='Кто установил 26 дня', blank=True, null=True)
    daypicker27 = models.ForeignKey(User, related_name='dt27', on_delete=models.PROTECT, verbose_name='Кто установил 27 дня', blank=True, null=True)
    daypicker28 = models.ForeignKey(User, related_name='dt28', on_delete=models.PROTECT, verbose_name='Кто установил 28 дня', blank=True, null=True)
    daypicker29 = models.ForeignKey(User, related_name='dt29', on_delete=models.PROTECT, verbose_name='Кто установил 29 дня', blank=True, null=True)
    daypicker30 = models.ForeignKey(User, related_name='dt30', on_delete=models.PROTECT, verbose_name='Кто установил 30 дня', blank=True, null=True)
    daypicker31 = models.ForeignKey(User, related_name='dt31', on_delete=models.PROTECT, verbose_name='Кто установил 31 дня', blank=True, null=True)
    comment = models.CharField('Комментарий', max_length=950, blank=True,null=True)

    def __str__(self):
        return str(self.full_name)
    class Meta:
        verbose_name = 'Список персонала в табели персонала'
        verbose_name_plural = 'Списки персонала в табелях персонала'

class agreement(models.Model):
    status = (('На проверке', 'На проверке'), ('На согласование', 'На согласование'), ('На корректировке', 'На корректировке'),('Завершен','Завершен'))
    name = models.CharField('Наименование', max_length=50,blank=True,null=True)
    date_create = models.DateTimeField('Дата и время создания')
    creator = models.ForeignKey(User ,verbose_name='Автор',related_name='Инициализатор' ,on_delete=models.PROTECT, blank=True, null=True)
    status = models.CharField('Статус', max_length=55, choices=status, default='На проверке')
    comment = models.CharField('Комментарий', max_length=5650, blank=True,null=True,default='')
    file = models.FileField(upload_to='books/%Y-%m-%d/')
    accept = models.IntegerField('Кол-во одобрений', default=0)
    to_correct = models.ForeignKey(User, verbose_name='Кто отправил на корректировку', related_name='ToCorrect', on_delete=models.CASCADE, blank=True, null=True)
    closer = models.ForeignKey(User, verbose_name='Кто закрыл', related_name='Closer', on_delete=models.CASCADE, blank=True, null=True)
    closed = models.IntegerField('Закрыт', default=0)

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['-date_create', ]
        verbose_name = 'Согласование'
        verbose_name_plural = 'Согласования'

class temp_file(models.Model):
    temp = models.FileField(upload_to='books/%Y-%m-%d/')

    def __str__(self):
        return str(self.temp.name)
    class Meta:
        verbose_name = 'Временный файл'
        verbose_name_plural = 'Временные файлы'

class accepter_list(models.Model):
    user = models.ForeignKey(User, verbose_name='Имя пользователя', related_name='acccepter_list', on_delete=models.CASCADE)

    def __str__(self):
        if self.user.first_name:
            return str(self.user.first_name+' '+self.user.last_name)
        else:
            return str(self.user.username)
    class Meta:
        verbose_name = 'Список проверяющих'
        verbose_name_plural = 'Список проверяющих'


class agreementer_list(models.Model):
    user = models.ForeignKey(User, verbose_name='Имя пользователя', related_name='agreementer_list',on_delete=models.CASCADE)
    def __str__(self):
        if self.user.first_name:
            return str(self.user.first_name + ' ' + self.user.last_name)
        else:
            return str(self.user.username)

    class Meta:
        verbose_name = 'Список одобряющих'
        verbose_name_plural = 'Списки одобряющих'


class ender_list(models.Model):
    user = models.ForeignKey(User, verbose_name='Имя пользователя', related_name='ender_list',on_delete=models.CASCADE)
    def __str__(self):
        if self.user.first_name:
            return str(self.user.first_name + ' ' + self.user.last_name)
        else:
            return str(self.user.username)

    class Meta:
        verbose_name = 'Список закрывающих утверждение'
        verbose_name_plural = 'Списки закрывающих утверждение'

class agreement_step(models.Model):
    type = (('Проверка', 'Проверка'),('Согласование','Согласование'),('Корректировка','Корректировка'),('Завершение','Завершение'))
    step = models.CharField('Этап', max_length=15 ,default='Проверка', choices=type)
    agreem = models.ForeignKey(agreement, verbose_name='Согласование', related_name='accept_key',on_delete=models.CASCADE)
    accepted = models.IntegerField('Принято', default=0)
    need = models.IntegerField('Нужно принять',default=1)

    def __str__(self):
        return str(self.agreem.name +' '+self.step)
    class Meta:
        verbose_name = 'Этап согласования'
        verbose_name_plural = 'Этапы согласования'

class agreement_accepter(models.Model):
    accepting = models.ForeignKey(agreement_step, verbose_name='Этап',related_name='Step', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Имя пользователя',related_name='Accepter',on_delete=models.CASCADE)
    accept = models.IntegerField('Принято', default=0)

    def __str__(self):
        if self.user.first_name:
            return str(self.accepting.agreem.name +' ' + self.accepting.step + ' ' + self.user.first_name+' '+self.user.last_name)
        else:
            return str(self.accepting.agreem.name +' ' + self.accepting.step + ' ' + self.user.username)
    class Meta:
        verbose_name = 'Принятие'
        verbose_name_plural = 'Принятия'

class notificated(models.Model):
    notificated = models.IntegerField('Оповещен',default=0)
    user = models.ForeignKey(User,verbose_name='Пользователь',related_name='notificater',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user.first_name+' '+self.user.last_name + '|' + self.user.username)
    class Meta:
        verbose_name = 'Оповещение для пользователя'
        verbose_name_plural = 'Оповещения для пользователей'

class notifications(models.Model):
    title = models.CharField('Наименование уведомления', max_length=200,blank=True,null=True)
    notification = models.CharField('Уведомления', max_length=2000)
    date = models.DateField('Дата уведомления', default=datetime.date.today())
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

