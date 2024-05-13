import flet as ft




def view(page):
    page.update()

    return ft.Column(
                controls=[
                    ft.Container(
                        width=450,
                        height=450,
                        margin = ft.margin.only(top=30),
                        alignment=ft.alignment.center,
                        content=ft.Text("Добавить банковскую карту")
                    ),
                    ft.ElevatedButton(
                        "Настройки",
                        width=120,
                        height=40,
                        on_click=lambda e: e.page.go("/settings")
                    )
                ]
            )
