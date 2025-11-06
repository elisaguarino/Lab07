from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
import flet as ft
'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self.musei=[]
        self.artefatto=[]
    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        id = museo.id
        artefatti = self._model.get_artefatti()
        for a in artefatti:
            if a.id_museo == id and a.epoca == epoca:
                self.view.artefattiF.append(ft.Text(a))
            print(self.view.artefattiF)
            self.view.update()


    def carica_artefatti(self):
        self.artefatti=self._artefatto_dao.read_artefatto()

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        return(list(set(a.epoca for a in self.artefatti)))

    # --- MUSEI ---
    def carica_musei(self):
        self.musei = self._museo_dao.read_museum()  # aggiorna il dato interno

    def get_musei(self):
        return self.musei  # metodo che restituisce la lista

