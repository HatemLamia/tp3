from pizza import Pizza
from cartePizzeriaException import CartePizzeriaException

class CartePizzeria:
    def __init__(self):
        self.pizzas = []
    
    def is_empty(self):
        return len(self.pizzas) == 0
    
    def nb_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise ValueError("Tu peux seulement ajouter des objets pizza au menu")
        self.pizzas.append(pizza)
    
    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"No pizza named '{name}' found in the menu") 
try:
    carte = CartePizzeria()
    print(carte.is_empty()) 
    carte.add_pizza(Pizza("Margherita", ["Tomate", "Mozzarella", "Basilic"], 8.5))
    print(carte.is_empty())
    print(carte.nb_pizzas()) 
    carte.remove_pizza("Margherita")
    print(carte.nb_pizzas()) 
    carte.remove_pizza("Margherita") 
except CartePizzeriaException as e:
    print(e)
    
"""
def main():
    # Création de quelques pizzas
    pizza_margherita = Pizza("Margherita", ["tomato", "mozzarella", "basil"], 8.99)
    pizza_pepperoni = Pizza("Pepperoni", ["tomato", "mozzarella", "pepperoni"], 9.99)
    pizza_vegetariana = Pizza("Vegetariana", ["tomato", "mozzarella", "peppers", "onions", "mushrooms"], 10.99)
    pizza_carnivore = Pizza("carnivore", ["tomato" , "chicken", "melt" , "meurgeuz"], 11.99)

    # Création de la carte de la pizzeria
    menu_pizzeria = CartePizzeria()

    # Ajout des pizzas à la carte
    menu_pizzeria.add_pizza(pizza_margherita)
    menu_pizzeria.add_pizza(pizza_pepperoni)
    menu_pizzeria.add_pizza(pizza_vegetariana)
    menu_pizzeria.add_pizza(pizza_carnivore)

    # Vérification du nombre de pizzas sur la carte
    print("Nombre de pizzas sur la carte:", menu_pizzeria.nb_pizzas())

    # Tentative d'ajout d'un objet non-Pizza à la carte
    try:
        menu_pizzeria.add_pizza("Hamburger")
    except ValueError as e:
        print("Erreur lors de l'ajout d'un hamburger à la carte:", e)

    # Suppression d'une pizza de la carte
    menu_pizzeria.remove_pizza("Pepperoni")

    # Vérification du nombre de pizzas sur la carte après la suppression
    print("Nombre de pizzas sur la carte après la suppression:", menu_pizzeria.nb_pizzas())

if __name__ == "__main__":
    main()"""
