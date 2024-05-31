import flet as ft

def main(page: ft.Page):
    page.title = "My Flet app"
    page.add(ft.Text("Hello, world!"))

ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
