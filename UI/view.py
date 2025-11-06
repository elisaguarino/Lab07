import flet as ft
from UI.alert import AlertManager
from UI.controller import Controller
'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        #dropDown musei
        self.opzioni = [
            ft.dropdown.Option(key=str(id_), text=f"{nome} - {tipologia}")
            for id_, nome, tipologia in self.controller.get_opzioni_Museo()
        ]
        self.menu_musei= ft.Dropdown(
            label="Museo",
            options=self.opzioni,
            width=300
        )
        epoche = self.controller.get_opzioni_epoca()
        self.menu_epoca = ft.Dropdown(
            label="epoca",
            options=[ft.dropdown.Option(key=e, text=e) for e in epoche],
            width=300
        )

        # Sezione 3: Artefatti
        # TODO
        self.artefattiF=ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
        self.mostra_artefatti=ft.ElevatedButton("mostra artefatti",on_click=self.controller.mostra)
        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(spacing=200,
                   controls=[self.menu_musei,self.menu_epoca],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),
            # Sezione 3: Artefatti
            # TODO
            ft.Row(spacing=200,
                   controls=[self.mostra_artefatti],
                   alignment=ft.MainAxisAlignment.CENTER),
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
