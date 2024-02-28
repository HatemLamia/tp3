import unittest
from unittest.mock import MagicMock
from cartePizzeria import CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):
    def test_is_empty(self):
        # Création d'une carte de pizzeria
        carte = CartePizzeria()
        # Vérification que la carte est vide initialement
        self.assertTrue(carte.is_empty())

    def test_nb_pizzas(self):
        # Création d'une carte de pizzeria
        carte = CartePizzeria()
        # Création d'une pizza mock
        pizza_mock = MagicMock()
        # Ajout de la pizza mock à la carte
        carte.add_pizza(pizza_mock)
        # Vérification que le nombre de pizzas est correct
        self.assertEqual(carte.nb_pizzas(), 1)

    def test_add_pizza(self):
        # Création d'une carte de pizzeria
        carte = CartePizzeria()
        # Création d'une pizza mock
        pizza_mock = MagicMock()
        # Ajout de la pizza mock à la carte
        carte.add_pizza(pizza_mock)
        # Vérification que la pizza a été ajoutée à la carte
        self.assertIn(pizza_mock, carte.pizzas)

    def test_remove_pizza(self):
        # Création d'une carte de pizzeria
        carte = CartePizzeria()
        # Création d'une pizza mock
        pizza_mock = MagicMock()
        # Ajout de la pizza mock à la carte
        carte.add_pizza(pizza_mock)
        # Suppression de la pizza mock de la carte
        carte.remove_pizza(pizza_mock.name)
        # Vérification que la pizza a été supprimée de la carte
        self.assertNotIn(pizza_mock, carte.pizzas)

    def test_remove_nonexistent_pizza(self):
        # Création d'une carte de pizzeria
        carte = CartePizzeria()
        # Tentative de suppression d'une pizza inexistante
        with self.assertRaises(CartePizzeriaException):
            carte.remove_pizza("NonExistentPizza")

if __name__ == "__main__":
    unittest.main()
