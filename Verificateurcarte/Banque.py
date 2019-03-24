class Banque:
     def __init__(self,numerocarte):
        self.numerocarte=numerocarte

     def _get_numerocarte(self):
            print("accés au numéro de la carte")
            return self._numerocarte

     def __set__(self,numerocarte):
        "on modifie la valeur de numerocarte"
        self._numerocarte=numerocarte


