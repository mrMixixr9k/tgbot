import flet as ft

def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = 'Cactus Clicker'
    btn = ft.TextButton(text="Button")
    page.add(btn)
    page.update()
    
ft.app(target=main)
