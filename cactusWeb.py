import flet as ft

def main(page: ft.Page):
    page.theme_mode = 'dark'
    page.title = 'Cactus Clicker'
    btn = ft.TextButton(text="Button")
    page.add(btn)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=80)
