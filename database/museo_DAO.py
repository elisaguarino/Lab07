from database import DB_connect
from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass
    @staticmethod
    def read_museum():
        print("Executing read from database using SQL query")
        resultsM = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Connection failed")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            # Una sola query, con cui si leggono tutte le righe
            query = """SELECT * 
                       FROM Museo"""
            cursor.execute(query)
            for row in cursor:
                #creo oggetti di tipo Museo
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                resultsM.append(museo)

            cursor.close()
            cnx.close()
            return resultsM
    # TODO
