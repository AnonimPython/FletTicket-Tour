import math
import flet as ft
from flet import *
import json
# import sqlite3

# /Для каждой сложной задачи существует решение, которое является быстрым, простым и неправильным. H. L. Mencken


# * достаем (читаем) данные пользователя
with open('assets/data/user.json') as file:
    data = json.load(file)


def view(page):
    page.update()
    
    
    
    
    def set_theme_colors(colors, theme_mode):
        color_set = colors[theme_mode]
        # * смена цветов для определенных элементов
        theme_text.color = color_set["theme_text"]
        settings_text.color = color_set["settings_text"]
        accout_text.color = color_set["accout_text"]
        user_name_text.color = color_set["user_name_text"]
        
    # * виброотдача
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    
    def toggle_theme(e):
        hf.heavy_impact() 
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        set_theme_colors(colors, page.theme_mode)

        page.update()

    
    theme_text = ft.Text(
        "Тема",
        size=20,
        color="white",
    )
    theme_toggle = ft.Switch(
        value=page.theme_mode == "light",
        on_change=toggle_theme,
        # * если переключатель вкл точка становится черной
        active_color="white",
        active_track_color="black",
        # * когда переключатель выкл точка становится белой
        inactive_thumb_color="white",
    )
    
    theme = ft.Row([theme_text,theme_toggle])
    
    # * кнопка для возврата на главную страницу
    back_btn = ft.Container(
        margin = ft.margin.only(bottom=100),
        content=ft.IconButton(
            icon=icons.ARROW_BACK_IOS_ROUNDED,
            on_click=lambda e: e.page.go("/tour")
        )
    )
    settings_text = ft.Text(
            "Настройки",
            size=40,
            weight=ft.FontWeight.W_900,
            color="white"
        )
    settings_container = ft.Container(
        margin = ft.margin.only(bottom=50),
        content=settings_text
    )
    accout_text = ft.Text(
        "Аккаунт", 
        color="white",
        size=25,
        weight=ft.FontWeight.W_900,
    )
    
    user_img = ft.Container(
        margin = ft.margin.only(right=50),
        content=ft.CircleAvatar(
            # foreground_image_url="",
            radius=40,
            content=ft.Image(src="/Users/evgenijlevin/Desktop/Диплом/assets/img/plane.png")
        )
    )
    
    edit_button_container = Container()
    
    # / имя пользователя
    # * достаем данные из сессии

    user_name = page.session.get("user_name")
    page.update()
    # user_name = data['user_name'][0]
    
    user_name_text = ft.Text(
        user_name,
        color="white",
        size=20,
    )
    user_name_edit = ft.TextField(
        visible=False,
        width=180
    )
    
    def edit_user(e):
        user_name_text.visible = not user_name_text.visible
        user_name_edit.visible = not user_name_edit.visible
        if user_name_edit.visible:
            user_name_edit.value = user_name
            user_name_edit.focus()
        edit_button_container.content = ft.IconButton(icon=ft.icons.SAVE_ROUNDED, on_click=save_user_name) if user_name_edit.visible else ft.IconButton(icon=icons.EDIT, on_click=edit_user)
        edit_button_container.update()
        page.update()
    
    def save_user_name(e):
        nonlocal user_name
        
        # !!!
        # ! попытаться сделать сохранение имени пользователя в базу данных
        # conn = sqlite3.connect('database.db')
        # cur = conn.cursor()
        # cur.execute('''SELECT user_name FROM users WHERE id = ?''', (id))
        # user_name = cur.fetchone()[0]
        # # Сохранение данных в переменную
        # user_name_variable = user_name

        # # Перезапись данных в базе данных
        # cur.execute('''UPDATE users SET user_name = ? WHERE id = ?''', (user_name_variable, id))

        # # Коммит изменений и закрытие подключения
        # conn.commit()
        # conn.close()
        
        
        user_name = user_name_edit.value
        # * перезаписываем имя пользователя
        page.session.set("user_name", user_name_edit.value)
        value = page.session.get("user_name")
        page.update()
        print(f'{value} settings.py это имя пользователя==================')
        user_name_text.value = user_name
        edit_user(e)
        
        

    # * Страница Аккаунт с пользователем
    edit_button_container.content = IconButton(icon=icons.EDIT, on_click=edit_user)
    user_info = ft.Row([user_img, user_name_text, user_name_edit, edit_button_container])
    
    
    # / банковская карта
    list_cards = ft.ListView(
        expand=1,
        spacing=15,
        horizontal=True,
        padding=0,
    )      

    # * данные по банковской карте
    for card_data in data['user_cards']:
        bank_name = card_data['bank_name']
        card_number = card_data['card_number']
        cvv = card_data['CVV']
        date = card_data['date']

        # * имя банка
        bank = ft.Text(bank_name,size=35,)
        # * номер банковской карты
        card_num = ft.Container(
            margin=ft.margin.only(top=25),
            content=ft.Text(card_number,size=27),
            alignment=ft.alignment.center
        )
        card_CVV = ft.Row(
            [
                ft.Text("CVV"),
                ft.Container(
                    content=ft.Text(cvv)
                ),
                ft.Text("Дата"),
                ft.Container(
                    content=ft.Text(date)
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        card_column = ft.Column(
            [
                bank,
                card_num,
                card_CVV,
            ]
        )
        from random import randint
        random = randint(1,11)
        card_info = ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[
                    "#42E3B4",
                    "#21BA72",
                    "#A0E720",
                    "#FAED00",
                ],
                tile_mode=ft.GradientTileMode.REPEATED,
                #                   5
                
                rotation=math.pi / random,
            ),
            width=420,
            height=200,
            # margin=margin.only(bottom=150),
            # bgcolor=ft.colors.with_opacity(0.9, 'grey'),
            border_radius=20,
            content=card_column,
        )
        page.update()

        # * удаление карты из списка
        def delete_card(e):
            list_cards.controls.remove(e.card)
            page.update()
        
        



        
        card = ft.Row(
            [
                ft.Dismissible(
                    content=card_info,
                    dismiss_direction=ft.DismissDirection.UP,
                    secondary_background=ft.Container(
                        bgcolor="red",
                        content=ft.Text("Удалить карту ?" , size=40,color="white"),
                        # padding=padding.only(top=150),
                        # alignment=ft.alignment.Alignment(0, 1),
                        alignment=ft.alignment.top_center,
                    ),
                    on_dismiss=delete_card, 
                    
                )
            ]
        )

        list_cards.controls.append(card)
        
    

    # * кнопка добавления банковской карты
    add_card = ft.IconButton(
        icon=ft.icons.ADD_CARD_ROUNDED,
        on_click=lambda e : e.page.go("/add_card"),
    )
    add_row = ft.Row(
        [
            # ft.Text("Добавить банковскую карту",size=20,color="white",),
            add_card 
        ]
    )

    content = ft.Column(
        [
            back_btn,
            settings_container,
            accout_text, 
            user_info, 
            theme,
            add_row,
            list_cards,
        ]
    )
    

    
    # * цвета для смены темы
    colors = {
        "light": {
            "theme_text":"black",
            "settings_text":"black",
            "accout_text":"black",
            "user_name_text":"black",
        },
        "dark": {
            "theme_text":"white",
            "settings_text":"white",
            "accout_text":"white",
            "user_name_text":"white", 
         },
    }

    set_theme_colors(colors, page.theme_mode)

    return ft.Column(
        controls=[
            ft.SafeArea(
                ft.Container(
                    width=450,
                    height=900,
                    # margin=ft.margin.only(left=40),
                    content=content
                ),
            ),

            
        ]
    )





