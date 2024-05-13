import flet as ft
from flet import *

import json


# / «Код сложнее читать, чем писать» — Джоэль Спольски
# /Аналогично тому, как написание картины является искусством для души, так и написание программы является искусством для разума. Volnik


# Открытие и чтение JSON файла
def read_tours_data():
    with open('assets/data/tours.json', 'r') as file:
        data = json.load(file)
    return data['tours']



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
        e.page.go('/tour_info')
        
    def save_selected_tour(tour):
        with open('assets/data/selected_tour.json', 'w',encoding='utf8') as file:
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
        if index == 1:e.page.go("/tickets")
        elif index == 2: e.page.go("/settings")
        
        page.update()
    
    # def search(e):
    #     pass
    
    # / вверхняя часть
    # * сохраняем все данные в переменную
    tours_data = read_tours_data()
    # !!!
    # tour_count = len(tours_data)
    # tour_size = tour_count * 260

    #                                                                       height=1500
    list_tour = ft.ListView(expand=1,spacing=10, padding=0, auto_scroll=False)
    
    
    for tour in tours_data:
        page.update()
        # * добавление в список данных из json файла
        list_tour.controls.append(ft.Container(
            # * размер одной карточки 260 px  
            # ! в будущем поправить стили и сделать другой размер
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
                        content=ft.Text(tour['title'],size=30,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD),
                        
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
        
        
    # ! возмодно отказ
    # # * поле для поиска
    # anchor = ft.SearchBar(
    #     view_elevation=4,
    #     divider_color=ft.colors.ORANGE_100,
    #     # bar_overlay_color = "red",
    #     bar_hint_text="Поиск",
    #     # ? True на полный экран поиск, можно задуматься на счет реализации
    #     # full_screen = True,
    #     view_hint_text="Введи интересующий вас запрос..",
    #     # on_change=handle_change,
    #     # ? важная вещь , нужно реалиать с помощью "Ввод" вывод инофрмации которую пользователь ввел
    #     on_submit=search,
    #     # on_tap=handle_tap,
    #     controls=[
    #         ft.ListTile(title=ft.Text(f"Пример"))

    #     ],
        
    # )
    
    
    # todo Tabs попробовать за место navbar

    # ! продажа туров (в будущем сделать переход на продажу билетов на самолет)
    # * панель навигации
    nav_bar = ft.NavigationBar(
        # height=200,
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
                # selected_icon=ft.icons.SETTINGS,
                label="Настройки",
            ),
        ],on_change= navigate
        
    )
    
        
    
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
                # * поиск
                # anchor,
                # * контейнер с турами (можно листать)
                ft.Container(
                    width=450,
                    # ! возможно такое не реализуемо тк список привязан к размеру своей области, если указать больше, скролл не будет идти до конца
                    height=800,
                    padding=ft.padding.only(bottom=25),
                    # alignment=ft.alignment.bottom_center,
                    content=list_tour,
                ),
            ]
        )
    
    
'''
ft.Text(f"ID: {tour['id']}\n"
                          f"Название: {tour['title']}\n"
                          f"Местоположение: {tour['location']}\n"
                          f"Длительность: {tour['duration']}\n"
                          f"Цена: {tour['price']}"),
'''