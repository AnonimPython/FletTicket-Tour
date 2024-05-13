import flet as ft
from flet import *

import json

import requests
from bs4 import BeautifulSoup as bs

import datetime
import pytz

import sqlite3


# todo : добавить БОЛЬШЕ графиков разнообразных

# / Неработающая программа обычно приносит меньше вреда, чем работающая плохо. Dave Thomas

# / Учитывая текущее плачевное состояние наших программ, можно сказать, что программирование определенно всё ещё черная магия, и пока мы не можем называть его технической дисциплиной. Bill Clinton

now = datetime.datetime.now()
moscow_tz = pytz.timezone('Europe/Moscow')
ny_tz = pytz.timezone('America/New_York')
uk_tz = pytz.timezone('Europe/London')
germany_tz = pytz.timezone('Europe/Berlin')

japan_tz = pytz.timezone('Asia/Tokyo')
china_tz = pytz.timezone('Asia/Shanghai')
india_tz = pytz.timezone('Asia/Kolkata')
la_tz = pytz.timezone('America/Los_Angeles')
canada_tz = pytz.timezone('America/Toronto')

# Получаем текущее время для каждого города
time_moscow = now.astimezone(moscow_tz).strftime("%H:%M")
time_ny = now.astimezone(ny_tz).strftime("%H:%M")
time_uk = now.astimezone(uk_tz).strftime("%H:%M")
time_ger = now.astimezone(germany_tz).strftime("%H:%M")
time_japan = now.astimezone(japan_tz).strftime("%H:%M")
time_china = now.astimezone(china_tz).strftime("%H:%M")
time_india = now.astimezone(india_tz).strftime("%H:%M")
    

# todo: добавить защиту от пустых полей ВЕЗДЕ  , сделать прогноз погоды , сделать цены на акции компаний , попытаться улучшить дизайн по максимому


# * билеты
def read_tikets_data():
    with open('assets/data/tikets.json', 'r') as file:
        data = json.load(file)
    return data['tickets']


# * туры
def read_tours_data():
    with open('assets/data/tours.json', 'r') as file:
        data = json.load(file)
    return data['tours']


# / подсчет кол-во билетов и туров
def summary_tikets():
    with open('assets/data/tikets.json', 'r') as file:
        data = json.load(file)
        tickets = data['tickets']
        num_tickets = len(tickets)
    return tickets, num_tickets

def summary_tours():
    with open('assets/data/tours.json', 'r') as file:
        data = json.load(file)
        tours = data['tours']
        num_tours = len(tours)
    return tours, num_tours


tickets_data, num_tickets = summary_tikets()

tours_data, num_tours = summary_tours()


# / подсчет кол-во пользователей в БД
db = sqlite3.connect('users.db')
cur = db.cursor()
# * Запрос к базе данных для подсчета количества пользователей
cur.execute("SELECT COUNT(*) FROM users")
result = cur.fetchone()
# * Получаем количество пользователей
user_count = result[0]
db.close()






def page(page:ft.Page):
    
    page.title = "Панель управления"
    page.window_control_allow_resize = False
    page.window_left = 300
    page.window_top = 3
    
    page.window_frameless = True

    page.theme_mode = "dark"
    
    page.window_width = 1320
    page.window_height = 820
    
    # * функцию для выхода из разных экранов на главную страницу
    def exit_back(e):
                page.snack_bar = ft.SnackBar(
                        content=ft.Text("Отмена", size=20,color=ft.colors.BLACK),
                        duration=600,
                        bgcolor=ft.colors.RED,
                )
                page.snack_bar.open = True
                right.content.controls.clear()
                right.content.controls.append(chart)
                right.content.controls.append(ft.Divider(height=1.5, color="white"))
                right.content.controls.append(ft.Container(
                            margin=ft.margin.only(left=30,top=40),
                            content=ft.Text("Курсы валют", size=40, color="white", text_align=ft.TextAlign.CENTER)
                        ))
                right.content.controls.append(currency_rate)
                page.update()
    
    
    def set_theme_colors(colors, theme_mode):
        color_set = colors[theme_mode]
        # * смена цветов для определенных элементов
        
        
    # / добавление билетов на тур
    def add_tour(e):
        right.content.controls.clear()

        # * создаем текстовые поля для каждого ключа с пустыми значениями
        title = ft.TextField(
            label='Заголовок',
            hint_text='',
            icon=ft.icons.AIRPLANE_TICKET_OUTLINED,
            border_radius= ft.border_radius.all(15),
        )
        location = ft.TextField(
            label='Локация',
            hint_text='Россия',
            icon=ft.icons.LOCATION_ON_OUTLINED,
            border_radius= ft.border_radius.all(15),
            width=200,
            
        )
        duration = ft.TextField(
            label='Кол-во дней',
            hint_text='7 дней',
            icon=ft.icons.ACCESS_TIME_OUTLINED,
            border_radius= ft.border_radius.all(15),
            width=200,
            
        )
        price = ft.TextField(
            label='Цена',
            hint_text='15000',
            icon=ft.icons.PAYMENTS_OUTLINED,
            border_radius= ft.border_radius.all(15),
            
            width=200,
            
        )
        img = ft.TextField(
            label='Картинка (ссылка)',
            hint_text='ссылка',
            icon=ft.icons.IMAGE,
            border_radius= ft.border_radius.all(15),
        )
        img1 = ft.TextField(
            label='Доп. картинка (ссылка)',
            hint_text='ссылка',
            icon=ft.icons.IMAGE_OUTLINED,
            border_radius= ft.border_radius.all(15),
        )
        main_text = ft.TextField(
            label='Основной текст',
            icon=ft.icons.FORMAT_COLOR_TEXT_SHARP,
            border_radius= ft.border_radius.all(15),
            hint_text='',
        )
        about = ft.TextField(
            label='Подробнее',
            hint_text='',
            icon=ft.icons.DESCRIPTION_OUTLINED,
            border_radius= ft.border_radius.all(15),
        )


        stars = ft.TextField(
            label='Звезд',
            hint_text='4',
            icon=ft.icons.STAR,
            border_radius= ft.border_radius.all(15),
            width=200,
            
        )

        right.content.controls.extend(
            [
                ft.Container(
                    alignment=alignment.center,
                    width=400,
                    margin=ft.margin.only(left=250),
                    content=ft.Column(
                        [
                            ft.Text("Добавление тура", size=25),
                            title,
                            ft.Row([location, duration]),
                            ft.Row([price, stars]),
                            img,
                            img1,
                            main_text,
                            about
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ]
        )

        right.content.controls.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CHECK_OUTLINED,
                            bgcolor=ft.colors.GREEN,
                            icon_color=ft.colors.LIGHT_GREEN,
                            on_click=lambda e: save_tour(
                                e, title, location, duration, price, img, img1, main_text, about, stars
                            ),
                            tooltip="Сохранить",
                        ), 
                        ft.IconButton(
                            bgcolor=ft.colors.RED,
                            icon=ft.icons.CLOSE,
                            icon_color=ft.colors.RED_900,
                            on_click=exit_back,
                            tooltip="Отменить",
                        )
                        
                    ],
                    spacing=65,
                    alignment=ft.MainAxisAlignment.CENTER),
                    margin=ft.margin.only(left=100),


            )
        )

        
        page.update()
    # / сохранение данных в туры
    def save_tour(e, title, location, duration, price, img, img1, main_text, about, stars):
        new_tour = {
            'title': title.value,
            'location': location.value,
            'duration': duration.value,
            'price': price.value,
            'img': img.value,
            'img1': img1.value,
            'main_text': main_text.value,
            'about': about.value,
            'stars': stars.value
        }

        existing_tours = read_tours_data()
        max_id = max(tour['id'] for tour in existing_tours) if existing_tours else 0
        new_tour['id'] = max_id + 1

        existing_tours.append(new_tour)

        with open('assets/data/tours.json', 'w', encoding='utf-8') as file:
            json.dump({"tours": existing_tours}, file, ensure_ascii=False, indent=4)

        right.content.controls.clear()
        right.content.controls.append(chart)
        right.content.controls.append(ft.Divider(height=1.5, color="white"))
        right.content.controls.append(ft.Container(
                    margin=ft.margin.only(left=30,top=40),
                    content=ft.Text("Курсы валют", size=40, color="white", text_align=ft.TextAlign.CENTER)
                ))
        right.content.controls.append(currency_rate)
        page.update()

    # / добавление билетов на самолет
    def add_ticket(e):
        right.content.controls.clear()

        # * создаем текстовые поля для каждого ключа с пустыми значениями
        title = ft.TextField(
            label='Авиакомпания',
            hint_text='Аэрофлот',
            icon=ft.icons.CORPORATE_FARE,
            border_radius= ft.border_radius.all(15),
            
        )
        from_city = ft.TextField(
            label='Откуда',
            hint_text='Москва',
            width=160,
            icon=ft.icons.AIRPLANE_TICKET_OUTLINED,
            border_radius=8
        )
        to = ft.TextField(
            label='Куда',
            hint_text='Стамбул',
            width=180,
            icon=ft.icons.AIRPLANEMODE_ACTIVE,
            border_radius= ft.border_radius.all(15),
            
            
            
        )
        duration = ft.TextField(
            label='Кол-во часов',
            hint_text='5 часов',
            width=180,
            icon=ft.icons.ACCESS_TIME_OUTLINED,
            border_radius= ft.border_radius.all(15),
            
            
            
        )
        # ? по возможности заменить на выпадающий список
        location = ft.TextField(
            label='Аэропорт',
            hint_text='Домодедово',
            width=200,
            icon=ft.icons.LOCATION_ON_OUTLINED,
            border_radius= ft.border_radius.all(15),

            
        )
        price = ft.TextField(
            label='Цена билета',
            hint_text='15000',
            width=200,
            icon=ft.icons.PAYMENTS_OUTLINED,
            border_radius= ft.border_radius.all(15),
        )
        img = ft.TextField(
            label='Картинка (ссылка)',
            hint_text='',
            icon=ft.icons.IMAGE_OUTLINED,
            border_radius= ft.border_radius.all(15),
            

        )
        stars = ft.TextField(
            label='Звезд',
            hint_text='4',
            width=150,
            icon=ft.icons.STAR,
            border_radius= ft.border_radius.all(15),
            
            
        )
        main_text = ft.TextField(
            label='Главный текст',
            hint_text='Летай на здоровье',
            # width=250,
            icon=ft.icons.FORMAT_COLOR_TEXT_SHARP,
            border_radius= ft.border_radius.all(15),
            
        )
        about = ft.TextField(
            label='О компании (перелете)',
            hint_text='45 лет мы с Вами',
            # width=250,
            icon=ft.icons.DESCRIPTION_OUTLINED,
            border_radius= ft.border_radius.all(15),
            
            
        )

        
        right.content.controls.extend(
            [
                ft.Container(
                    # alignment=ft.Alignment(0, 0),
                    width=400,
                    margin=ft.margin.only(left=250),
                    content=ft.Column(
                        [
                            ft.Text("Добавление билеты", size=25),
                            title,
                            ft.Row([from_city, to]),
                            ft.Row([duration, location]),
                            ft.Row([price, stars]),
                            img,
                            main_text,
                            about
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                )
            ]
        )

        right.content.controls.append(
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.CHECK_OUTLINED,
                            bgcolor=ft.colors.GREEN,
                            icon_color=ft.colors.LIGHT_GREEN,
                            on_click=lambda e: save_tiket(
                                e, title, from_city, to, duration, location, price, img, stars, main_text, about,
                            ),
                            tooltip="Сохранить",
                            
                        ),
                        ft.IconButton(
                            bgcolor=ft.colors.RED,
                            icon=ft.icons.CLOSE,
                            icon_color=ft.colors.RED_900,
                            on_click=exit_back,
                            tooltip="Отменить",
                            
                        )
                        
                    ],spacing=65,
                    alignment=ft.MainAxisAlignment.CENTER),
                    margin=ft.margin.only(left=100),


            )
        )

        
        page.update()

    # / сохранение данных в билеты
    def save_tiket(e, title, from_city, to, duration, location, price, img, stars, main_text, about):
        new_tiket = {
            'title': title.value,
            'location': location.value,
            'duration': duration.value,
            'price': price.value,
            'img': img.value,
            'from_city': from_city.value,
            'to': to.value,
            'main_text': main_text.value,
            'about': about.value,
            'stars': stars.value
        }

        existing_tiket = read_tikets_data()
        max_id = max(ticket['id'] for ticket in existing_tiket) if existing_tiket else 0
        new_tiket['id'] = max_id + 1

        existing_tiket.append(new_tiket)

        with open('assets/data/tikets.json', 'w', encoding='utf-8') as file:
            json.dump({"tickets": existing_tiket}, file, ensure_ascii=False, indent=4)

        right.content.controls.clear()
        right.content.controls.append(chart)
        right.content.controls.append(ft.Divider(height=1.5, color="white"))
        right.content.controls.append(ft.Container(
                    margin=ft.margin.only(left=30,top=40),
                    content=ft.Text("Курсы валют", size=40, color="white", text_align=ft.TextAlign.CENTER)
                ))
        right.content.controls.append(currency_rate)
        
        page.update()

    

    def show_tours_list(e):
        right.content.controls.clear()
        tours = read_tours_data()
        
        header = ft.Container(
            margin=ft.margin.only(left=45),
            content=ft.Row([
                ft.IconButton(
                    # bgcolor=ft.colors.RED,
                    icon=ft.icons.ARROW_BACK_IOS_ROUNDED,
                    on_click=exit_back,
                    tooltip="Отменить",
                ),
                ft.Text("Список туров", size=45,color="WHITE")
            ])
        )
        
        
        right.content.controls.append(header)
        
        
        
        
        
        
        
        # Create a list of Tours with 'delete' buttons
        for tour in tours:
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=tour['id']: delete_tour(e, id),
                tooltip="Удалить"
            )
            tour_row = ft.Container(
                margin=ft.margin.only(left=45),
                content=ft.Row(
                [ 
                    
                    #                    , width=200
                    ft.Text(tour['title']),
                    ft.Text(tour['location']),
                    ft.Text(f"дней: {tour['duration']}"),
                    ft.Text(f"цена: {tour['price']}"),
                    ft.Text(f"№: {tour['id']}"),
                    delete_button 
                ]
                )
            )
            right.content.controls.append(tour_row)
        page.update()
   
    def show_tickets_list(e):
        right.content.controls.clear()
        tickets = read_tikets_data()
        header = ft.Container(
            margin=ft.margin.only(left=45),
            content=ft.Row([
                ft.IconButton(
                    # bgcolor=ft.colors.RED,
                    icon=ft.icons.ARROW_BACK_IOS_ROUNDED,
                    on_click=exit_back,
                    tooltip="Отменить",
                ),
                ft.Text("Список авиабилетов", size=45,color="WHITE")
            ])
        )
        
        
        right.content.controls.append(header)

        for ticket in tickets:
            delete_button = ft.IconButton(
                icon=ft.icons.DELETE,
                on_click=lambda e, id=ticket['id']: delete_ticket(e, id),
                tooltip="Удалить"
            )
            ticket_row = ft.Container(
                margin=ft.margin.only(left=45),
                content=ft.Row(
                    [ 
                        ft.Text(ticket['title']), 
                        ft.Text(f"откуда: {ticket['from_city']}"),
                        ft.Text(f"куда: {ticket['to']}"),
                        ft.Text(f"дней: {ticket['duration']}"),
                        ft.Text(f"цена: {ticket['price']}"),
                        ft.Text(f"индентификатор: {ticket['id']}"),
                        
                        delete_button 
                    ]
                )
            )
            right.content.controls.append(ticket_row)

        page.update()


    
    def delete_tour(e, id):
        tours = read_tours_data()
        tours = [tour for tour in tours if tour['id'] != id]

        with open('assets/data/tours.json', 'w', encoding='utf-8') as file:
            json.dump({"tours": tours}, file, ensure_ascii=False, indent=4)

        show_tours_list(e)

    def delete_ticket(e, id):
        tickets = read_tikets_data()
        tickets = [ticket for ticket in tickets if ticket['id'] != id]

        with open('assets/data/tikets.json', 'w', encoding='utf-8') as file:
            json.dump({"tickets": tickets}, file, ensure_ascii=False, indent=4)

        show_tickets_list(e)

    
        
        
    # / левая часть ==================================
    left = ft.Container(
        width=300,
        height=800,
        bgcolor="#1D1D2A",
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(
                            src="/Users/evgenijlevin/Desktop/Диплом/assets/img/logo.png",
                            width=50,
                            height=50,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        ft.Text("TourCMS System", size=30,color=ft.colors.WHITE)
                    ]
                ),
                
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        [
                            ft.ElevatedButton(
                                content=ft.Text("Туры", text_align=ft.TextAlign.CENTER),
                                width=200,
                                on_click=add_tour
                            ),
                            ft.ElevatedButton(
                                content=ft.Text("Билеты",text_align=ft.TextAlign.CENTER),
                                width=200,
                                on_click=add_ticket
                            ),
                            ft.ElevatedButton(
                                content=ft.Text("Список туров",text_align=ft.TextAlign.CENTER),
                                width=200,
                                on_click=show_tours_list
                            ),
                            ft.ElevatedButton(
                                content=ft.Text("Список билетов",text_align=ft.TextAlign.CENTER),
                                width=200,
                                on_click=show_tickets_list
                            ),
                        ]
                    )
                ),
                
            ]
        )
    )
    
    
    chart = ft.Container(
        width=1000,
        margin=ft.margin.only(left=10),
        content=ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=num_tours,
                        width=40,
                        color=ft.colors.AMBER,
                        tooltip=f"Туры\n{num_tours}",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=num_tickets,
                        width=40,
                        color=ft.colors.BLUE,
                        tooltip=f"Билеты\n{num_tickets}",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=user_count,
                        width=40,
                        color=ft.colors.GREEN,
                        tooltip=f"Пользователи\n{user_count}",
                        border_radius=0,
                    ),
                ],
            ),
            

        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Статистика сервиса"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Туры"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Билеты"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Пользователи"), padding=10)
                ),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=70,
        interactive=True,
        expand=True,
        
    )
    )
    
    
    
    # / получение всех курсов валют

    url = 'https://www.cbr.ru/currency_base/daily/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')

        table = soup.find('table', {'class': 'data'})

        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) > 1:
                currency = columns[1].text
                rate = float(columns[4].text.replace(',', '.'))
                rounded_rate = round(rate, 1)

                if currency == 'USD':
                    usd_rate = rounded_rate
                elif currency == 'EUR':
                    eur_rate = rounded_rate
                elif currency == 'GBP':
                    gbp_rate = rounded_rate
                elif currency == 'JPY':
                    jpy_rate = rounded_rate
                elif currency == 'AUD':
                    aud_rate = rounded_rate
                elif currency == 'CAD':
                    cad_rate = rounded_rate
                elif currency == 'CHF':
                    chf_rate = rounded_rate
    
    
    else:
        print("Ошибка при получении данных. Пожалуйста, попробуйте позже.")

    
    # * Доллары
    usd = ft.Text(f"{usd_rate}" , size=40)

    # * Евро
    euro = ft.Text(f"{eur_rate}" , size=40)

    # * Фунт стерлингов
    gbp = ft.Text(f"{gbp_rate}" , size=40)

    # * Японская иена
    jpy = ft.Text(f"{jpy_rate}" , size=40)

    # * Австралийский доллар
    aud = ft.Text(f"{aud_rate}" , size=40)

    # * Канадский доллар
    cad = ft.Text(f"{cad_rate}" , size=40)

    # * Швейцарский франк
    chf = ft.Text(f"{chf_rate}" , size=40)


    # * контейнер куда будет помещаеться поверх валют
    def handle_hover(e, currency, name, size, image_path):
        if e.data == "true":
            new_content = ft.Text(name, size=size, text_align=ft.TextAlign.CENTER)
        else:
            new_content = ft.Row(
                [
                    ft.Image(
                        width=40,
                        height=40,
                        src=image_path,
                    ),
                    currency,
                ]
            )
        
        e.control.content = new_content
        e.control.update()
        
    def hover_usd(e):
        handle_hover(e, usd, "Доллар", 45, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/USD.svg")

    def hover_euro(e):
        handle_hover(e, euro, "Евро", 45, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/EURO.svg")

    def hover_gbp(e):
        handle_hover(e, gbp, "Фунт\nстерлингов", 30, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/STERLING.svg")

    def hover_jpy(e):
        handle_hover(e, jpy, "Иен", 45, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/JEIN.svg")

    def hover_aud(e):
        handle_hover(e, aud, "Австралийский\nдоллар", 30, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/austUSD.svg")

    def hover_cad(e):
        handle_hover(e, cad, "Канадский\nдоллар", 30, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/canadaUSD.svg")

    def hover_chf(e):
        handle_hover(e, chf, "Швейцарский\nфранк", 20, "/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/FRANG.svg")

    currency_rate = ft.Container(
        content=ft.Container(
                margin=ft.margin.only(top=20, left=20),
                content=ft.Column(
                    [
                        # * горизонтальная разметка для вывода списка курс валют
                        # ! можно оптимизировать код с помощью for
                        ft.Row(
                        [
                        # * Доллар
                        ft.Container(
                            on_hover=hover_usd,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/USD.svg",
                                    ),
                                    usd,
                                    
                                ]
                            )
                        ),
                        # * Евро
                        ft.Container(
                            on_hover=hover_euro,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/EURO.svg",
                                    ),
                                    euro,
                                    
                                ]
                            )
                        ),
                        # * Доллар Стерлингов
                        ft.Container(
                            on_hover=hover_gbp,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/STERLING.svg",
                                    ),
                                    gbp
                                    
                                ]
                            )
                        ),
                        # * Японская иена
                        ft.Container(
                            on_hover=hover_jpy,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/JEIN.svg",
                                    ),
                                    jpy,
                                    
                                ]
                            )
                        ),
                        # * Австралийский доллар
                        ft.Container(
                            on_hover=hover_aud,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/austUSD.svg",
                                    ),
                                    aud
                                    
                                ]
                            )
                        ),
                        # * Канадский доллар
                        ft.Container(
                            on_hover=hover_cad,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/canadaUSD.svg",
                                    ),
                                    cad

                                    
                                ]
                            )
                        ),
                        # * Швейцарский франк
                        ft.Container(
                            on_hover=hover_chf,
                            width=200,
                            height=100,
                            padding=ft.padding.only(left=20),
                            bgcolor="#1D1D2A",
                            border_radius=15,    
                            content=ft.Row(
                                [
                                    ft.Image(
                                        width=40,
                                        height=40,
                                        src="/Users/evgenijlevin/Desktop/Диплом/assets/img/money_icons/FRANG.svg",
                                    ),
                                    chf
                                ]
                            )
                        ),
                        
                        ],
                    wrap=False, 
                    scroll="always"
                    # конец ft.Row валют
                    ),
                    ft.Text("Часовой пояс",
                            size=40,
                            color="white",
                            text_align=ft.TextAlign.CENTER
                    ),
                    # * часовой пояс
                    ft.Row(
                        [
                            # * Москва
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Москва {time_moscow}",
                                    size=35,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Нью-Йорк
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Нью-Йорк {time_ny}",
                                    size=35,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Великобритания
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Великобритания\n{time_uk}",
                                    size=25,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Германия
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Германия\n{time_ger}",
                                    size=30,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Япония
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Япония\n{time_japan}",
                                    size=30,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Китай
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Китай\n{time_china}",
                                    size=30,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                            # * Индия
                            ft.Container(
                                margin=ft.margin.only(top=20),
                                width=200,
                                height=100,
                                border_radius=15,    
                                bgcolor="#1D1D2A",
                                content=ft.Text(
                                    f"Индия\n{time_india}",
                                    size=30,
                                    color="white",
                                    text_align=ft.TextAlign.CENTER
                                )
                            ),
                        ],
                        wrap=False, 
                        scroll="always"
                    # конец ft.Row часовой пояс
                    ),
                    
                    ],
                )
            ),
    )

    # / правая часть  ==================================
    right = ft.Container(
        width=1000,
        
        margin=margin.only(left=-10),
        padding=padding.only(top=20, right=20),
        height=800,
        bgcolor="#12121F",
        content=ft.Column(
            [
                chart,
                ft.Divider(height=1.5, color="white"),
                ft.Container(
                    margin=ft.margin.only(left=30,top=40),
                    content=ft.Text("Курсы валют", size=40, color="white", text_align=ft.TextAlign.CENTER)
                ),
                currency_rate,
                
            ]
        )
    )
    
    
    
    
    
    page.add(ft.Row([left,right]))
    
    
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
    
    page.fonts = {
        "San Francisco": "/Users/evgenijlevin/Desktop/Диплом/assets/font/apple-font.ttf",
    }

    page.theme = ft.Theme(font_family="San Francisco")
    
    page.update()
    
    

if __name__ == '__main__':
    ft.app(
            target=page,
            assets_dir="assets",
    )
    
    
# ? python3 dashboard.py & python3 main.py 


