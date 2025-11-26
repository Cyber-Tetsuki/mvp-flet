import flet as ft
from flet.core.page import Page
from db import Database
from presenter import AppPresenter
from views import AppView
from model import EnvModel
from navigator import Navigator


class Factory:
    def __init__(self, page: Page):
        self._navigator = Navigator(page)
        self._env = EnvModel()
        self._db = Database(self._env.db_setting_path)

    def view_is_rendered(self) -> None:
        pass

    def create_app_view(self) -> ft.View:
        app_view = AppView(self._env)
        app_presenter = AppPresenter(app_view)
        app_view.presenter = app_presenter
        return app_view.build()
