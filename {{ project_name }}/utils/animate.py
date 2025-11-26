import time
import flet as ft


def animate_click(btn: ft.ElevatedButton, scale):
    default_scale = btn.scale
    btn.scale = ft.Scale(scale)
    btn.update()
    time.sleep(0.04)
    btn.scale = default_scale
    btn.update()
