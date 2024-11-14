import flet as ft
import random

def main(page: ft.Page):
    page.title = "Pregunta importante"
    page.window.width = 400
    page.window.height = 300
    page.window.resizable = False

    margen_inferior = 100
    margen_lateral = 120
    movimiento_minimo = 50

    def mover_boton_no(e):
        max_top = page.height - margen_inferior
        max_left = page.width - margen_lateral

        top_actual = btn_no.top
        left_actual = btn_no.left 

        nuevo_top, nuevo_left = top_actual, left_actual
    while abs(nuevo_top - top_actual) < movimiento_minimo /
    


