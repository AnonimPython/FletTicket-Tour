import flet as ft
from flet import *
from random import randint
import sqlite3

import smtplib

# / закончен =================
# ! но требуется небольшой рефакторинг

# todo: сделать отправку на почту html документа 


# анимация кнопки (мигание)
from time import sleep

# / «Простота – предпосылка надежности» — Эдсгер Дейкстра
# / Если оптимизировать всё, что можно, то вы будете вечно несчастным. Donald Knuth
# from pages.verification import view as verification_view


# * настройка почты и запуск сервера
email = 'iintelekt@internet.ru'
password = 'T4b3xRtuVbTkmMKcQek6'

# / почта
# * функция отправляет письмо на почту
def send_email(user_mail):
    #  переадресация переменной в файл verification.py для проверки одноразового кода
    # global secret_code
    
    # secret_code = randint(1111, 9999)
    # secret_code = randint(1, 9)
    
    
    #* Формирование текста сообщения с темой
    # full_message = f"Subject: Ваш одноразовый код\n\nКод: {secret_code}"
    full_message = f"Subject: ТурГостеприимство\n\nНаш сервис рад , что Вы зарегестрировались на нашем ресурсе\n\nВаш Логин: {user_login.value}\n\nВаш пароль: {user_login.value}\n"
     
    # * проверка на доступность к почте
    try:
        # * Отправка с запуском сервера
        with smtplib.SMTP('smtp.mail.ru', 587) as server:
            server.starttls()
            server.login(email, password)
            server.sendmail(email, user_mail, full_message.encode('utf-8'))
            # print("Функция send_mail Код:" , secret_code)
    except Exception as e:
        e.page.go("/register")
        print(f"Ошибка при отправке почты: {e}")
        
    
        



# тестовая почта
# user_mail = "moscow.retro@list.ru"
# заглушка чтоб код работал и мог запускать окно с верификацией
# user_mail = ""
# send_email(user_mail)



def view(page):
    global user_login , user_mail

    # / РЕГИСТРАЦИЯ В ПРИЛОЖЕНИИ 
    # ! приложение добавляет пользователя в любом случае
    # ! ВСКОРЕ БУДЕТ ИСПРАВЛЕНО
    # *  регистрация пользователя
    # ! не юзать, хуита
    def register(e):
        # import random
        # import string

        # characters = string.ascii_letters + string.digits
        # user_id = ''.join(random.choice(characters) for i in range(6))
        # print(f"ID уникальный пользователя: {user_id}")
        
        # e.page.go("/verification")
        
        # * подключение к БД
        db = sqlite3.connect('users.db')
        # * активация курсора
        cur = db.cursor()
        # * запрос с помощью SQL
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    password TEXT,
                    mail TEXT
                    )
                    '''
        )
        
        
        cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (user_login.value, user_password.value, user_mail.value))
        # * сохранение данных в БД
        db.commit()
        # * закрываем базу данных
        db.close()
        
        
        

        # * после сохранения чистим поля
        user_login.value = ''
        user_password.value = ''
        user_mail.value = ''
        

        e.page.update()
        
        


    # * валидация для проверки на пустые поля 
    def validate(e):
        if user_password.value == "" and user_login.value == "" and checkbox.value == False and user_mail.value == "":
            reg_btn.disabled = True
        else:
            reg_btn.disabled = False
            

        e.page.update()
    
        
    user_login = ft.TextField(
        label="Логин",
        prefix_icon=ft.icons.PEOPLE,
        # on_change=validate,
        border_color="white",
        # border_color="transparent",
        
    )
    user_password = ft.TextField(
        label="Пароль",
        password=True,
        # on_change=validate,
        can_reveal_password=True,
        prefix_icon=ft.icons.PASSWORD,        
        border_color="white"
        # border_color="transparent",
    )

    user_mail = ft.TextField(
        label="Почта",
        prefix_icon=ft.icons.ALTERNATE_EMAIL,
        border_color="white"
    )
    
    def checkbox_changed(e):
        # * проверка чекбокса на активность
        if checkbox.value == False: 
            reg_btn.disabled = True
        else:
            reg_btn.disabled = False
        reg_btn.update()
        
    

    # * чекбок (адаптивный под разные устройства)
    checkbox = ft.Checkbox(label="Политика конф.", on_change=checkbox_changed, adaptive=True)
        
    # * сохранение данных и отправка письма благодарности на почту
    def verifi(e):
        # * проверка чекбокса на активность
        checkbox.value = False
        
        # * проверка чтобы поле не было пустым и защита от пробелов
        # if user_mail.value == "" or user_login.value == "" or user_password.value == "":
        if user_mail.value.replace(" ", "") == "" and checkbox.value == False:
            bs = ft.BottomSheet(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("This is sheet's content!"),
                        ],
                        tight=True,
                    ),
                    padding=10,
            ),
            )
            page.overlay.append(bs)
            # * отклюбчение чекбокса при ошибке
            checkbox.value = False
            # * красным цветом показывает, что поле пустое
            user_mail.value = ""
            user_mail.bgcolor = "red"
            e.page.update()
            # * секундная задержка
            sleep(1)
            # * возвращает цвет обратно
            user_mail.bgcolor="#171F34"
            reg_btn.disabled = True
        else:
            # * для теста перевод чекбокса и кнопку в бездействие
            checkbox.value = False
            reg_btn.disabled = True
            # * переадресация на следующую страницу
            # e.page.go("/verification")
            # ! при релизе сделать переход на страницу в авторизацией
            # e.page.go("/login")
            e.page.go("/tour")
            # * почту сохраняем в переменную
            user = user_mail.value
            # ! тест куда отправилось письмо
            print(f"Почта: {user_mail.value}")
            # * запуск сервера и сразу отправка сообщения на почту
            send_email(user)
            
            # * подключение к БД
            db = sqlite3.connect('users.db')
            # * активация курсора
            cur = db.cursor()
            # * запрос с помощью SQL
            cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                login TEXT,
                password TEXT,
                mail TEXT,
                user_name TEXT
            )''')
            
            # * сохраняем имя пользователя в сессию
            page.session.set("user_name", user_login.value)
            value = page.session.get("user_name")
            print(f'{value} register.py имя пользователя сохранено')
            
            # * сохраняем в сессию почту пользователя
            page.session.set("user_mail", user)
            user_mail_session = page.session.get("user_mail")
            print(f'{user_mail_session} register.py почта пользователя сохранено')
            
            
            cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", 
                    (user_login.value, user_password.value, user_mail.value, value))
            # * сохранение данных в БД
            db.commit()
            # * закрываем базу данных
            db.close()

            # * после сохранения чистим поля
            user_login.value = ''
            user_password.value = ''
            user_mail.value = ''


        
        e.page.update()
    


    # / кнопки для регистрации или авторизации
       
    # * кнопка для отправки письма на почту и регистрация пользователя
    reg_btn = ft.ElevatedButton(
            width=200,
            height=50,
            # on_click=lambda e: (e.page.go("/verification"),send_email(user_mail))
            on_click=verifi,
            disabled=True,
            # on_click=register,
            # ? тут прописан контекст для текста чтобы было удобно поставить его по центру кнопки
            content=ft.Text("Создать аккаунт", text_align = ft.TextAlign.CENTER,)
        )
    login_btn = ft.ElevatedButton(
            "Есть аккаунт",
            width=200,
            height=50,
            on_click= lambda e: e.page.go("/login")
        )
    # * кнопки находятся сбоку друг от друга
    buttons = ft.Row([login_btn,reg_btn],alignment=ft.MainAxisAlignment.CENTER)
    
    # btn_reg = ft.OutlinedButton(text="Создать аккаунт", on_click= register, disabled=True)

    main_text = ft.Column(
        [
            ft.Row(
                [
                    ft.Text("ТурГостеприимство",
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            size=29,
                    ),
                    ft.Icon(name=ft.icons.AIRLINE_SEAT_FLAT, color="yellow")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ft.Text(
                "Вход в аккаунт",
                size=22,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),
             
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    # * центруем по центру company_name (текст)
    text_align = ft.Container(
        content=main_text,
        margin=ft.margin.only(left=50)
    )
    
    
    
    
    # * поля для ввода пользователем данных
    user_inputs = ft.Column(
        [
            user_login,
            user_password,
            user_mail,
            checkbox,

        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    inputs_align = ft.Container(
        content=user_inputs,
        margin=ft.margin.only(bottom=5)
    )
        
    panel_register = ft.Row(
             [
                #  * создание вертикального ряда
                 ft.Column(
                    [
                        text_align ,
                        
                        ft.Container(
                            margin = ft.margin.only(left=50),
                            content=inputs_align
                        ),
                        buttons,
                    ],scroll = ft.ScrollMode.HIDDEN,
                 )
             ],alignment=ft.MainAxisAlignment.CENTER,expand=True
         )
    
    
    
    return ft.Column(
                    controls=[
                        ft.Container(
                            # alignment=ft.alignment.center,
                            
                            # padding=10,
                            margin = ft.margin.only(top=150),
                            content=panel_register
                        ),
                    ]
                    
                )
