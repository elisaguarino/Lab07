import flet as ft
from UI.view import View
from model.model import Model
from database.museo_DAO import MuseoDAO
'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def get_opzioni_Museo(self):
        if not self._model.musei:
            self._model.carica_musei()
        return [(m.id,m.nome,m.tipologioa) for m in self._model.get_musei()]

    def get_opzioni_Epoca(self):
        if not self._model.artefatti:
            self._model.carica_artefatti()
        return self._model.get_epoche()


    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra(self):
       risultati=self.model.get_artefatti_filtrati()
       return risultati

