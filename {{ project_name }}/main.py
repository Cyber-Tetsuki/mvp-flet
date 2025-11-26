import time
import flet as ft
from flet.core.types import MainAxisAlignment
from screeninfo import get_monitors
from factory import Factory
from dotenv import load_dotenv

load_dotenv()


def main(page: ft.Page):
    page.title = "Flet App"
    page.window.resizable = False
    page.window.maximizable = False
    page.window.minimizable = False
    screen = get_monitors()[0]
    screen_w = screen.width
    screen_h = screen.height

    win_w = 800
    win_h = 600
    left = (screen_w / 2) - (win_w / 2)
    top = (screen_h / 2) - (win_h / 2)
    page.window.width = win_w
    page.window.height = win_h
    page.window.left = left
    page.window.top = top
    page.update()

    factory = Factory(page)
    routes = {
        "/app": lambda: factory.create_app_view()
    }

    def route_change(e):
        # loading screen
        page.views.clear()
        page.views.append(
            ft.View(
                bgcolor=ft.Colors.GREY_200,
                controls=[
                    ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                ft.Text(
                                    value="Loading Resources",
                                    theme_style=ft.TextThemeStyle.TITLE_LARGE,
                                    style=ft.TextStyle(
                                        decoration_style=ft.TextDecorationStyle.WAVY,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.BLUE,
                                    )
                                ),
                                ft.ProgressRing(
                                    stroke_width=3,
                                    width=30,
                                    height=30,
                                )
                            ]
                        )
                    )
                ]
            )
        )
        page.update()
        time.sleep(0.45)

        page.views.clear()
        route = page.route

        view = routes[route]()
        page.views.append(view)
        page.update()
        factory.view_is_rendered()  # trigger the callback to let the view know that controls is rendered

    page.on_route_change = route_change
    page.go("/app")


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP_HIDDEN, assets_dir='assets')
