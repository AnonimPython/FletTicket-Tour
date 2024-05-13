import flet as ft
from flet import *

import json




# todo при входе на данную страницу сначала показать всплывающее окно AlertDialog или BottomSheet для ввода имени в профиль. Badge использовать для уведомления человека о том, что он купил билет. CircleAvatar использовать для аватара (ЕСЛИ ПОЛУЧИТСЯ РЕАЛИЗОВАТЬ)

# / «Код сложнее читать, чем писать» — Джоэль Спольски
# / Аналогично тому, как написание картины является искусством для души, так и написание программы является искусством для разума. Volnik


# Открытие и чтение JSON файла
def read_tours_data():
    with open('assets/data/tikets.json', 'r') as file:
        data = json.load(file)
    return data['tickets']



# def show_tour_details(e, tour):
#         e.page.clean()
#         print(f"ID тура {tour['id']} нажата.")
#         if tour['id'] == 1:
#             save_selected_tour(tour)
#         e.page.update()



    
    


def view(page):

    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    
    
    def show_tour_details(e, tour):
        value = page.session.get("user_name")
        print(f'{value} сессия получена==================')
        save_selected_tour(tour)  # вызываем функцию для сохранения выбранного тура в JSON файл
        e.page.go('/airline_info')
        
    def save_selected_tour(tour):
        with open('assets/data/selected_airline.json', 'w',encoding='utf8') as file:
            json.dump(tour, file, indent=4,ensure_ascii=False)
        
    # * функция для навигации
    def navigate(e):
        hf.heavy_impact() 
        # * получение индекса из нав бара
        index = nav_bar.selected_index
        print(f'Индекс страницы: {index}') 
        # * очистка экрана для нового экрана
        
        e.page.clean()
        if index == 0: e.page.go("/tour")
        elif index == 1:e.page.go("/tickets")
        elif index == 2: e.page.go("/settings")
        
        page.update()
        
        # e.page.update()
    
    

    # / вверхняя часть
    # * сохраняем все данные в переменную
    tours_data = read_tours_data()

    list_tour = ft.ListView(expand=1,spacing=10, padding=0, auto_scroll=False)
    
    
    for tour in tours_data:
        page.update()
        # * добавление в список данных из json файла
        list_tour.controls.append(ft.Container(
            height=480,
            # bgcolor=ft.colors.WHITE,
            alignment=ft.alignment.center,
            border=ft.border.only(bottom=ft.border.BorderSide(2, ft.colors.BLACK)),
            border_radius=15,
            content=ft.Column(
                [
                    ft.Image(
                        src=tour['img'],
                        # height=250,
                        # width=500,
                        fit=ImageFit.FILL,
                    ),
                    ft.Container(
                        content=ft.Text(tour['title'],size=10,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(tour['duration'],size=15),
                                ft.Text(tour['location'],size=15),
                                ft.Icon(name=ft.icons.STAR_SHARP, color='yellow',size=15),
                                ft.Text(tour['stars'],size=15),
                            ],alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),
                    
                    
                    # * кнопка для перехода на новую страницу и просмотра доп. информации
                    ft.Container(
                        content=ElevatedButton(
                            content=ft.Text("Подробнее",size=25),
                            on_click=lambda e, tour=tour: show_tour_details(e, tour),
                            width=350,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        ),
                        alignment=ft.alignment.center,
                    )
                    
                ],alignment=ft.MainAxisAlignment.CENTER
            )
        )
        )
    
    
    
    # * панель навигации
    nav_bar = ft.NavigationBar(
        adaptive=True,
        bgcolor="transparent",
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.AIRLINE_SEAT_FLAT_OUTLINED,
                # selected_icon=ft.icons.AIRLINE_SEAT_FLAT,
                label="Туры",
            ),
            ft.NavigationDestination(
                icon=ft.icons.AIRPLANE_TICKET_OUTLINED,
                # selected_icon=ft.icons.AIRPLANE_TICKET,
                label="Билеты",
            ),
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                label="Настройки",
            ),
        ],on_change= navigate
    )
    page.update()

    
    return ft.Column(
            controls=[
                # * отступ для разных вызеров в экране
                ft.SafeArea(
                ft.Container(
                    alignment=ft.alignment.top_center,
                    content=nav_bar
                )
                ),
                # * линия
                ft.Divider(height=1, color="white"),
                # * контейнер с авиаперелетами (можно листать)
                ft.Container(
                    width=450,
                    height=730,
                    padding=ft.padding.only(bottom=25),
                    # alignment=ft.alignment.bottom_center,
                    content=list_tour,
                ),
            ]
        )
