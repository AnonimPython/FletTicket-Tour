"""
Создание цифровой платформы для управления и анализа данных в сфере туризма и гостеприимства в компании "".
"""


import flet as ft
from flet import *

from pages.start import view as start_view
from pages.register import view as auth_view
from pages.settings import view as settings_view
from pages.tickets import view as tickets_view
from pages.verification import view as verification_view
from pages.login import view as login_view
from pages.tours import view as tour_view
from pages.tour_info import view as tour_info
from pages.airline_info import view as airline_info
from pages.add_card import view as add_card

# / Ада Лавлейс. «Если ваша работа не документирована, значит вы не работали».

# TODO: Исправить баг регистрации с пустыми полями и давать случайный индетификатор пользователю (буквы-цифры), ResponsiveRow использовать для адаптации разных размеров телефонов

def page(page:ft.Page):
    page.title = "ТурГостеприимство"
    page.window_control_allow_resize = False
    

    # держить окно приложения выше всех окон
    # page.window_always_on_top = True
    # audio1 = ft.Audio(
    #     src="./Users/evgenijlevin/Desktop/Диплом/assets/videoplayback.mp3", autoplay=True
    # )
    # page.overlay.append(audio1)


    # расположение окна на экране для тестирования
    page.window_left = 400
    page.window_top = 50
    # скрытие вверхней части окна (закрыть, свернуть)
    page.window_frameless = True
    # тема
    page.theme_mode = "dark"
    
    # ! размер айфон 15 про макс
    page.window_width = 450
    page.window_height = 900
    # page.window_max_height = 1500

    # скрытие ползунка скролла
    page.scroll = ft.ScrollMode.HIDDEN


    

    def route_change(route):
        page.views.clear()
            
        page.views.append(
            ft.View(
                "/start",
                [
                start_view(page),
                ]
            )
        )
        # page.views.append(
        #     ft.View(
        #         "/tour",
        #         [
        #         tour_view(page),
        #         ]
        #     )
        # )
        
        if page.route == "/auth":
            page.views.append(
                ft.View(
                    "/auth",
                    
                    [
                    auth_view(page)
                    ],bgcolor="#171F34"
                )
            )
        if page.route == "/login":
            page.views.append(
                ft.View(
                    "/login",
                    
                    [
                        login_view(page)
                    ],bgcolor="#171F34"
                )
            )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        settings_view(page)
                    ]
                )
            )
        if page.route == "/tour":
            page.views.append(
                ft.View(
                    "/tour",
                    [
                        tour_view(page)
                    ]
                )
            )
        if page.route == "/tickets":
            page.views.append(
                ft.View(
                "/tickets",
                    [
                        tickets_view(page)
                    ]
                )   
            )
        if page.route == "/tour_info":
            page.views.append(
                ft.View(
                "/tour_info",
                    [
                        tour_info(page)
                    ]
                )   
            )
        if page.route == "/airline_info":
            page.views.append(
                ft.View(
                "/airline_info",
                    [
                        airline_info(page)
                    ]
                )   
            )
        if page.route == "/add_card":
            page.views.append(
                ft.View(
                "/add_card",
                    [
                        add_card(page)
                    ]
                )   
            )
            
            
        

        page.update()
        
    
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    
    
    # * шрифт
    page.fonts = {
        "San Francisco": "/Users/evgenijlevin/Desktop/Диплом/assets/font/apple-font.ttf",
    }
    # * установка шрифта
    page.theme = ft.Theme(font_family="San Francisco")
    
    

    page.update()

if __name__ == '__main__':
    ft.app(
            target=page,
            assets_dir="assets",
            # view=ft.AppView.WEB_BROWSER
    )
    
    
    
    
    

# ? ============flet build apk | flet build ipa
