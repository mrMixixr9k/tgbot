import flet as ft

def main(page: ft.Page):
    page.title = "My Flet app"
    page.add(ft.Text("Hello, world!"))

ft.app(target=main, host="0.0.0.0", port=80, view=None)
