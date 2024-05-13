import flet as ft


# ! ХУИТА !!! НЕ ТРОГАТЬ=====================================


def view(page):

            ft.Column(
                controls=[
                    ft.Container(
                        width=450,
                        height=450,
                        margin = ft.margin.only(top=30),
                        alignment=ft.alignment.center,
                        content=ft.Text("Настройки")
                    ),
                    ft.ElevatedButton(
                        "Билеты",
                        width=120,
                        height=40,
                        on_click=lambda e: e.page.go("/settings")
                    )
                ]
            )
