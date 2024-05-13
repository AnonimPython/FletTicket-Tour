
# / закончен=====================================================
import flet as ft

import sqlite3
from time import sleep

# /Эдсгер Вибе Дейкстра «Если отладка — процесс удаления ошибок, то программирование должно быть процессом их внесения».

def view(page):
        
    user_login = ft.TextField(
        label="Логин",
        prefix_icon=ft.icons.PEOPLE,
        # width=Page.window_width,
        border_color="white",
    )
    user_password = ft.TextField(
        label="Пароль",
        password=True,
        # width=Page.window_width,
        can_reveal_password=True,
        prefix_icon=ft.icons.PASSWORD,        
        border_color="white"
    )
    
    # def snak(e):
    #     ft.SnackBar(content=ft.Text("Hello, world!"),action="Alright!",open=True)
        
    # * авторизация на аккаунт
    def log_in(e):
        
        # * пдключение к бд
        db = sqlite3.connect('users.db')
        # * активация курсора
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE login=? AND password=?", (user_login.value, user_password.value))

        user = cur.fetchone()
        if user:
            e.page.go("/tour")
            user_login.value = ''
            user_password.value = ''
            
            e.page.update()
        else:
            # log_in.on_click = snak
            # e.page.go("/auth")
            
            e.page.update()

        page.session.set("user_name", user_login.value)
        value = page.session.get("user_name")
        print(f'{value} login.py имя пользователя')
        db.commit()
        # * закрываем БД
        db.close()
        

        # * после сохранения чистим поля
        user_login.value = ''
        user_password.value = ''
        
        
        e.page.update()
        
    
    


    
    # * кнопка входа в аккаунт
    log_in = ft.ElevatedButton(
            "Войти в аккаунт",
            width=400,
            height=50,
            # on_click=lambda e: (e.page.go("/verification"),send_email(user_mail))
            on_click=log_in
            # on_click=register
        )
    reg_btn = ft.ElevatedButton(
            "Зарегестрироваться",
            width=400,
            height=50,
            on_click= lambda e: e.page.go("/auth")
        )
    
    # btn_reg = ft.OutlinedButton(text="Создать аккаунт", on_click= register, disabled=True)
    company_name = ft.Row(
        [
            ft.Text("ТурГостеприимство",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=29,
                    ),
            ft.Icon(name=ft.icons.AIRLINE_SEAT_FLAT, color="yellow")
        ]
    )
    main_text = ft.Column(
        [
            company_name,
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
        margin=ft.margin.only(left=30)
    )
    
    
    
    
    # * поля для ввода пользователем данных
    user_inputs = ft.Column(
        [
            user_login,
            user_password,

        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    inputs_align = ft.Container(
        content=user_inputs,
        margin=ft.margin.only(bottom=40)
    )
        
    panel_login = ft.Row(
             [
                #  * создание вертикального ряда
                 ft.Column(
                    [
                        text_align ,
                        ft.Container(
                            margin = ft.margin.only(left=50),
                            content=inputs_align
                        ),
                        log_in,
                        reg_btn,
                    ]
                 )
             ],alignment=ft.MainAxisAlignment.CENTER
         )
    
    
    
    return ft.Column(
                    controls=[
                        ft.Container(
                            # alignment=ft.alignment.center,
                            
                            # padding=10,
                            margin = ft.margin.only(top=150),
                            content=panel_login
                        ),
                    ]
                    
            )
