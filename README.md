# Herbivores and carnivores

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start


Nature is well suited to reflect the principles of Object Oriented Programming. 
All instances of the `Animal` class must have health, name and hidden attribute. 
Health is 100 and hidden is false by default. Animal should have method 
`update_animal`, this method updates information about animal in class 
attribute `Animal.alive`.

All alive animals should be in the class attribute `Animal.alive`. 
It is a list with animals dicts with keys 'name', 'health', 'hidden'.
If the health of the animal reaches 0, the beast dies and it should 
be removed from `Animals.alive`.

Create a `Herbivore` class. This class should inherit from Animal. 
Herbivore has a method of `hide`, which changes 
the hidden property of the beast to the opposite value and helps to hide 
from carnivores. To update information about changed animal call his method 
`update_animal`. As you remember child classes inherits methods from parents.
```python
rabbit = Herbivore("Susan")
Animal.alive == [{"name": "Susan", "health": 100, "hidden": False}]
rabbit.hide()
Animal.alive == [{"name": "Susan", "health": 100, "hidden": True}]  #updated
```

Create a `Сarnivore` class. This class should inherit from Animal. 
Carnivore has a `bite` method, which takes a 
herbivore object and decreases the object's health by 50. The method 
does not work if it is another сarnivore, or the herbivore is currently hiding.
To update information about changed animal call his method `update_animal`.
```python
lion = Carnivore("Lion King")
rabbit = Herbivore("Susan")
rabbit.health == 100
lion.bite(rabbit)
rabbit.health == 50  # bited

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 50  # lion cannot bite hidden rabbit

rabbit.hide()
lion.bite(rabbit)
rabbit.health == 0  # rabbit is dead

Animal.alive == [{"name": "Lion King", "health": 100, "hidden": False}]
# there is no dead animals in Animal.alive
```


