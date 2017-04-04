import unittest
from servicesRest import rechercheVille
from servicesRest import rechercheActivite


"""Fichier de tests unitaires pour le fichier qui servait à essayer les différentes fonctions qui seront dans l'API"""
class TestRecherche(unittest.TestCase):

    def test_rechercheVille(self):
        self.assertFalse(rechercheVille("Nante"))
        self.assertFalse(rechercheVille("Londre"))
        self.assertFalse(rechercheVille("Paris"))
        self.assertTrue(rechercheVille("Nantes"))
        self.assertFalse(rechercheVille("Lval"))
        self.assertTrue(rechercheVille("Laval"))

    def test_rechercheActivite(self):
        self.assertFalse(rechercheActivite("foot"))
        self.assertFalse(rechercheActivite("basket"))
        self.assertFalse(rechercheActivite("Volley"))
        self.assertTrue(rechercheActivite("Basket-Ball"))
        self.assertFalse(rechercheActivite("course"))
        self.assertTrue(rechercheActivite("Tennis"))

if __name__ == '__main__':
    unittest.main()
