import flet as ft
from flet import *
import json


def read_tours_info():
    with open('assets/data/selected_tour.json', 'r') as file:
        data = json.load(file)
    return data

# todo: сделать карусель фотографий для туров
# / Аналогично тому, как написание картины является искусством для души, так и написание программы является искусством для разума. Volnik
def view(page):
    
    tour_info = read_tours_info()
    
    id_tour = tour_info['id']
    title = tour_info['title']
    location = tour_info['location']
    duration = tour_info['duration']
    price = tour_info['price']
    img = tour_info['img']
    img1 = tour_info['img1'] # пока отложить идею
    main_text = tour_info['main_text']
    about = tour_info['about']
    stars = tour_info['stars']
    
    
    
    print(f"ID тура: {id_tour}")
    print(f"Название: {title}")
    print(f"Местоположение: {location}")
    print(f"Длительность: {duration}")
    print(f"Цена: {price}")
    print(f"Главное изображение: {img}")
    print(f"Изображение 1: {img1}")
    print(f"Основной текст: {main_text}")
    print(f"Описание: {about}")
    print(f"Звезды: {stars}")
    
    # / вверхняя часть экрана
    main_img = ft.Container(
        content=ft.Image(src=img,border_radius=10)
    )

    

    
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
                    f"Количество дней: ",size=20,
                    spans=[
                        ft.TextSpan(
                        f"{duration}",
                        ft.TextStyle(weight=ft.FontWeight.BOLD, size=20)),
                    ]
                ),
                ft.Container(
                    padding=ft.padding.only(top=45),
                    content=ft.ElevatedButton(
                        bgcolor = "#171F34",
                        color="white",
                        height=60,
                        width=300,
                        content=ft.Text(
                            f"Купить за {price} ₽",size=20,
                        ),
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    ),
                    alignment=ft.alignment.center,
                )
                
            ]
        )
    )
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


"""
ft.Container(
                        width=450,
                        height=450,
                        margin = ft.margin.only(top=30),
                        alignment=ft.alignment.center,
                        content=ft.Text(f"ID тура: {id_tour}\n"
                          f"Название: {title}\n"
                          f"Местоположение: {location}\n"
                          f"Длительность: {duration}\n"
                          f"Цена: {price}"
                          f"Главное изображение: {img}\n"
                          f"Изображение 1: {img1}\n"
                          f"Цена: {price}"
                          f"Основной текст: {main_text}"
                          f"Описание: {about}\n"
                          f"Звезды: {stars}\n"
                            )
                    ),
"""