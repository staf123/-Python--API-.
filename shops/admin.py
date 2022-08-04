django  из.contrib  импортирует  admin
django  из.contrib.auth.admin  импортирует  UserAdmin

из .models  импортируйте  пользователя, магазин, категорию, Продукт, информацию о продукте, параметр, параметр продукта, Заказ, элемент заказа, \
    Связаться, подтвердить отправку сообщений


Класс  ProductParameterInline(admin.TabularInline):
    модель = Параметр продукта
    дополнительно  =  1


Класс  ProductInline(admin.TabularInline):
    модель  =  Продукт
    дополнительно  =  1


Класс  OrderItemInline(admin.TabularInline):
    модель =  элемент заказа
    дополнительно  =  2


@admin.register(пользователь)
Пользовательский  класс администратора (UserAdmin):
    модель  =  Пользователь
    = наборы полей (
 (Нет, {'fields': ('email', 'password', 'type')}),
 ('Личная информация', {'поля': ('first_name', 'last_name', 'компания', 'должность')}),
 ('Разрешения', {
            'поля': ('is_active', 'is_staff', 'is_superuser', 'группы', 'user_permissions'),
        }),
 ('Важные даты', {'поля': ('last_login', 'date_joined')}),
    )
    = list_display ('email', 'first_name', 'last_name', 'is_staff')


@admin.register(Магазин)
Класс  администратора магазина (admin.ModelAdmin):
    модель  =  Магазин
    = наборы полей (
 (Нет, {'поля': ('имя', 'состояние')}),
 ('Дополнительная информация', {'поля': ('url', 'пользователь'),
                             'классы': ('свернуть',)}),
    )
    = list_display ('имя', 'состояние', 'url')


@admin.register(Категория)
Класс  CategoryAdmin(admin.ModelAdmin):
    модель  =  Категория
    = inlines [ProductInline]


@admin.register(Продукт)
Класс  ProductAdmin(admin.ModelAdmin):
    пройти


@admin.register(ProductInfo)
Класс  ProductInfoAdmin(admin.ModelAdmin):
    модель =  Информация о продукте
    = наборы полей (
 (Нет, {'fields': ('product', 'model', 'external_id', 'quantity')}),
 ('Цены', {'поля': ('цена', 'price_rrc')}),
    )
    = list_display ('product', 'external_id', 'price', 'price_rrc', 'количество')
    = упорядочивание ('external_id',)
    = inlines [ProductParameterInline]


@admin.register(параметр)
Класс  ParameterAdmin(admin.ModelAdmin):
    пройти


@admin.register(Заказать)
Класс заказа  (admin.ModelAdmin):
    модель  =  Порядок
    =  поля ('пользователь', 'состояние', 'контакт')
    = list_display ('пользователь', 'создан', 'состояние')
    = упорядочивание ('создано',)
    = встроенные строки [
        OrderItemInline,
    ]


@admin.register(элемент заказа)
Класс  OrderItemAdmin(admin.ModelAdmin):
    пройти


@admin.register(Контакт)
Класс  ContactAdmin(admin.ModelAdmin):
    пройти


@admin.register(подтвердите почтовый токен)
Подтвердите  класс mailtokenadmin(admin.ModelAdmin):
    = list_display ('user', 'key', 'created_at',)
