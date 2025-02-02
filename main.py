class Pizza:
    def __str__(self):
        return self.__class__.__name__
    
    def prepare(self):
        return f"{self} is preparing."
    
    def bake(self):
        return f"{self} is baking."
    
    def cut(self):
        return f"{self} is cutting."
    
    def box(self):
        return f"{self} is boxing."

class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()

class GreekPizza(Pizza):
    def __init__(self):
        super().__init__()


class PizzaStore:
    def __init__(self, name):
        self.name = name

    def order(self, pizza_order):
        for pizza_class in Pizza.__subclasses__():              # All classes in python know their subclasses.
            if pizza_order in pizza_class.__name__.lower():     # Check if the pizza order is in the pizza class name.
                pizza = pizza_class()                           # Create a pizza object.
                                                                # "pizza_class" is the class name, not the instance.

                                                                # If pizza_order is "cheese", 
                                                                # then pizza_class is CheesePizza.
                break
        else:                   # Else is called when the for loop doesn't break.
            pizza = Pizza()     # Therefore, must be a custom pizza.

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


def main():
    
    print(PizzaStore("Pizza Hut").order(input("Enter pizza type: ")))

    import sys
    if "--debug" in sys.argv:
        from pprint import pprint

        print()
        print("Debug".center(100, "-"))

        print("All Pizza subclasses:".ljust(30))
        pprint(Pizza.__subclasses__())
        print()

        pizza_subclass = Pizza.__subclasses__()[0]
        print("First Pizza subclass:".ljust(30),            pizza_subclass)
        print("First Pizza subclass type:".ljust(30),       type(pizza_subclass))
        print("First Pizza subclass instance:".ljust(30),   pizza_subclass())


if __name__ == "__main__":
    main()
