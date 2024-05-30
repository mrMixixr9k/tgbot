import flet as ft

def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = 'Cactus Clicker'

if __name__ == "__main__":
    ft.app(target=main, view=None, port=80)
