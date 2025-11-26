import flet as ft
from flet.core.types import MainAxisAlignment, CrossAxisAlignment
from model import EnvModel
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from presenter import AppPresenter


class AppView:
    def __init__(self, env: EnvModel):
        self._env = env
        self._presenter: Optional["AppPresenter"] = None

    def on_rendered(self):
        pass

    def build(self):
        return ft.View(
            controls=[
                ft.Column(
                    expand=True,
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="MVP Flet App",
                                    theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM
                                )
                            ]
                        )
                    ]
                )
            ]
        )
