# hola mundo con flet
from flet import Page, Text, Button, Column, Row
def main(page: Page):
    page.title = "Hola Mundo con Flet"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def on_click(e):
        text.value = "¡Hola, mundo!"
        page.update()

    text = Text(value="")
    button = Button("Haz clic aquí", on_click=on_click)

    page.add(Column([text, button], alignment="center"))
# ejecutar la aplicación
if __name__ == "__main__":
    import flet
    flet.run(main)
