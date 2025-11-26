import time
from typing import Callable

import flet as ft
from screeninfo import get_monitors


class Navigator:
    def __init__(self, page: ft.Page):
        self.page = page

    def _remove_all_the_subscribed_event(self):
        self.page.on_keyboard_event = None

    @property
    def window_width(self):
        return self.page.window.width

    @property
    def window_height(self):
        return self.page.window.height

    @property
    def route(self):
        return self.page.route

    def go(self, route: str):
        self._remove_all_the_subscribed_event()
        self.page.go(route)

    def exit(self):
        self.page.window.destroy()

    def open_dlg(self, control: ft.Control):
        if control not in self.page.overlay:
            self.page.overlay.append(control)
        control.open = True
        self.page.update()

    def close_dlg(self, control: ft.Control):
        if control in self.page.overlay:
            control.open = False
            self.page.update()
            self.page.overlay.remove(control)
            time.sleep(0.000001)

    def set_page_session(self, **kwargs):
        session = kwargs
        for key, value in session.items():
            self.page.session.set(key=key, value=value)

    def get_page_session(self, key: str) -> any:
        session = self.page.session.get(key=key)
        return session

    def set_window_size(self, height: int, width: int) -> None:
        screen = get_monitors()[0]
        screen_w = screen.width
        screen_h = screen.height
        top = (screen_h / 2) - (height / 2)
        left = (screen_w / 2) - (width / 2)

        self.page.window.top = top
        self.page.window.left = left
        self.page.window.width = width
        self.page.window.height = height

        self.page.update()

    def on_keydown_event(self, call_back: Callable):
        self.page.on_keyboard_event = call_back
        self.page.update()
