import flet as ft

def main(page: ft.Page):
    page.title = "My Flet app"
    page.add(ft.Text("Hello, world!"))

if __name__ == "__main__":
    ft.app(main)
