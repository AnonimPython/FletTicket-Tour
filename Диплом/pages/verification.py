import flet as ft

# ! ХУИТА !!! НЕ ТРОГАТЬ=====================================


def view():

    panel = ft.Column(
        [
            ft.Text("Регистрация прошла успешно!")
        ]
    )


    return ft.View(
        "/verification",
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        width=450,
                        height=450,
                        bgcolor="red",
                        margin = ft.margin.only(top=30),
                        alignment=ft.alignment.center,
                        content=panel
                    ),
                    ft.ElevatedButton(
                        "назад",
                        width=120,
                        height=40,
                        on_click=lambda e: e.page.go("/auth")
                    ),
                    
                ]
            )
        ]
    )
