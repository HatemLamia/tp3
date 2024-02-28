import unittest
from unittest.mock import Mock
from pizza import Pizza 
from cartePizzeria import   CartePizzeria, CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()
        self.pizza = Mock(spec=Pizza)
        self.pizza.name = "Test Pizza"

    def test_is_empty_true_initially(self):
        self.assertTrue(self.carte.is_empty())

    def test_add_pizza_and_is_empty_false(self):
        self.carte.add_pizza(self.pizza)
        self.assertFalse(self.carte.is_empty())

    def test_nb_pizzas_after_adding_one(self):
        self.carte.add_pizza(self.pizza)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza_decreases_count(self):
        self.carte.add_pizza(self.pizza)
        self.carte.remove_pizza(self.pizza.name)
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_that_does_not_exist_raises_exception(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Nonexistent Pizza")

if __name__ == "_main_":
    unittest.main()
