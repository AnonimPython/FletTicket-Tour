import flet as ft
from flet import *
import json

from io import BytesIO
import os
import time
from barcode import EAN13
from barcode.writer import ImageWriter

from random import randint

def read_tours_info():
    with open('assets/data/selected_airline.json', 'r') as file:
        data = json.load(file)
    return data

# todo: сделать карусель фотографий для туров
# / Аналогично тому, как написание картины является искусством для души, так и написание программы является искусством для разума. Volnik
def view(page):
    
    airline_info = read_tours_info()
    
    id_tour = airline_info['id']
    title = airline_info['title']
    # ! дописать код
    from_ = airline_info['from_city']
    to = airline_info['to']
    
    
    duration = airline_info['duration']
    location = airline_info['location']
    price = airline_info['price']
    img = airline_info['img']
    stars = airline_info['stars']
    main_text = airline_info['main_text']
    about = airline_info['about']
    
    
    # / вверхняя часть экрана
    main_img = ft.Container(
        content=ft.Image(src=img,border_radius=10)
    )

    
    def generate_barcode(e):        
        filename = f"somefile_{int(time.time())}.jpeg"
        filepath = os.path.join("assets/img", filename)

        rand_num = randint(000000000000,999999999999)
        
        rv = BytesIO()
        
        EAN13(str(rand_num), writer=ImageWriter()).write(rv)

        # Or to an actual file:
        with open("/Users/evgenijlevin/Desktop/Диплом/assets/img/somefile.jpeg", "wb") as f:
            EAN13(f"{rand_num}", writer=ImageWriter()).write(f)
            page.update()
            
        
            
        
        bs.open = True
        
        bs.update()
        page.update()
            
    user_place = 1
    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                [
                    ft.Text(
                        "Ваш билет\nСохраните его для быстрого получения", 
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(
                        border_radius=2000,
                        content=ft.Image(
                            src="/Users/evgenijlevin/Desktop/Диплом/assets/img/somefile.jpeg",
                            width=500,height=250,
                        ),
                    ),
                    # ! сделать чтоб писал номер самолета и номер места и класс
                    ft.Container(
                        alignment=ft.alignment.bottom_center,
                        
                        margin=ft.margin.only(left=40),
                        content=ft.Row(
                            [
                                ft.Text(
                                    f"Место {user_place}",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Text(
                                    "Самолет: Boeing 737",
                                    text_align=ft.TextAlign.CENTER,
                                    
                                ),
                            ]
                        )
                    ),
                    
                ],
                tight=True,
            ),
            margin=40,
        ),
        open=False,
    )
    page.overlay.append(bs)
    page.update()
           
    
    # / нижняя часть
    bottom = ft.Container(
        # bgcolor="white",
        # border_radius=30,
        # padding=ft.padding.only(top=50),
        content=ft.Column(
            [
                ft.Row(
                    [  
                        ft.Text(title , size=50,weight=ft.FontWeight.BOLD),
                        ft.Text(f"{location}",size=20),   
                        ft.Icon(name=ft.icons.STAR_SHARP, color='yellow'),
                        ft.Text(f"{stars}",weight=ft.FontWeight.BOLD,size=20), 
                        
                    ]
                ),
                ft.Container(content=ft.Text(main_text,size=30),padding=ft.padding.only(top=10),),

                ft.Text(f"{about}" , size=25),
                
                ft.Text(
                    f"Время в полете: ",size=20,
                    spans=[
                        ft.TextSpan(
                        f"{duration}",
                        ft.TextStyle(weight=ft.FontWeight.BOLD, size=20)),
                    ]
                ),
                ft.Container(
                    padding=ft.padding.only(top=45),
                    content=ft.ElevatedButton(
                        bgcolor="#171F34",
                        color="white",
                        height=60,
                        width=300,
                        content=ft.Text(
                            f"Купить за {price} ₽",size=20,
                        ),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        on_click=generate_barcode
                    ),
                    alignment=ft.alignment.center,
                )
            ],page.update()
        )
    )
    page.update()
    
    back_btn = ft.Container(
        margin = ft.margin.only(bottom=1),
        content=ft.IconButton(
            icon=icons.ARROW_BACK_IOS_ROUNDED,
            on_click=lambda e: e.page.go("/tour")
        )
    )

    return ft.Column(
                controls=[
                    ft.SafeArea(back_btn),
                    main_img,
                    bottom,
                ]
            )
