
# / закончен=====================================================

#/ Помимо математических способностей, жизненно важным качеством программиста является исключительно хорошее владение родным языком. Edsger W. Dijkstra

# ! сделать рефакторинг кнопки


import flet as ft

def view(page):

    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    # / вверхняя часть блока
    
    # * поверх блока можно вставлять другие элементы как в css position:realitive
    # * картинка самолета
    plane_img = ft.Image(
        src="./Users/evgenijlevin/Desktop/Диплом/assets/img/plane.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    top_screen = ft.Stack(
        controls=[
            ft.Container(
                width=450,
                height=470,
                bgcolor="#171F34",
                content=plane_img
            ),
        ],
    )
    # / нижняя часть блока
    
    # * кнопка
    start_row_btn= ft.Row(
        [
            ft.ElevatedButton(
                bgcolor = "#171F34",
                width=350,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                color="white",
                height=60,
                # todo: ft.Dismissible попробовать вместо кнопки
                on_click=lambda e: (e.page.go("/auth"), hf.heavy_impact()),
                # on_click=lambda e: page.go("/auth"),
                content=ft.Text("Начать", size=20),
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    # * позицианирование кнопки
    btn_pos = ft.Container(
        content=start_row_btn,
        # * высота кнопки в своем блоке
        alignment=ft.alignment.Alignment(0, 0.60),
    )
    # * текст над кнопкой
    info_text= ft.Column(
        [
            ft.Text(
                "Исследуй мир\nИсследуй захватывающее",
                color="#171F34",
                weight=ft.FontWeight.BOLD,
                size=45,
                
                text_align = ft.TextAlign.CENTER,
                # padding = ft.padding.only(0,0.5),
            ),
            # * блок чтоб поднять текст выше
            ft.Container(height=100),
            
        ],alignment= ft.MainAxisAlignment.CENTER
        
    )
    
    # * нижний блок
    bottom_screen = ft.Stack(
        controls=[
            ft.Container(
                width=450,
                height=500,
                padding=20,
                bgcolor="white",
                content=info_text,
                alignment=ft.alignment.top_center
            ),
            btn_pos
        ],
        
        
    )
    


    return ft.Column(
                [
                ft.Container(
                    width=450,
                    height=450,
                    # margin = ft.margin.only(top=50),
                    alignment=ft.alignment.center,
                    padding= -10,
                    content = top_screen
                ),
                ft.Container(
                    width=450,
                    height=450,
                    alignment=ft.alignment.center,
                    padding= -10,
                    # padding= ft.padding.only(top=50),
                    content=bottom_screen,
                ),
                
                ],
            )
            