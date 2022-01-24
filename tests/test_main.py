from app.main import Animal, Herbivore, Carnivore


def test_animal_class():
    assert hasattr(Animal, "alive"), (
        f"Animal class should have attribute 'alive'"
    )
    assert hasattr(Animal, "update_animal"), (
        f"Animal class should have attribute 'update_animal'"
    )


def test_animal_constructor():
    lion = Animal("Lion King")
    assert hasattr(lion, "name"), (
        "Animal instance should have attribute 'name'"
    )
    assert hasattr(lion, "health"), (
        "Animal instance should have attribute 'health'"
    )
    assert hasattr(lion, "hidden"), (
        "Animal instance should have attribute 'hidden'"
    )
    assert lion.name == "Lion King", (
        f"'lion.name' should equal to 'Lion King' when "
        f"'lion' created by 'Animal('Lion King')'"
    )
    assert lion.health == 100, (
        f"'lion.health' should equal to 100 when "
        f"'lion' created by 'Animal('Lion King')'"
    )
    assert lion.hidden is False, (
        f"'lion.hidden' should equal to False when "
        f"'lion' created by 'Animal('Lion King')'"
    )
    assert Animal.alive == [{"name": "Lion King", "health": 100, "hidden": False}], (
        "Constructor should add created animal to 'Animal.alive'"
    )


def test_animal_update_animal():
    Animal.alive = []
    rabbit = Animal("Susan")
    rabbit.health = 50
    rabbit.hidden = True
    rabbit.update_animal()
    assert Animal.alive == [{"name": "Susan", "health": 50, "hidden": True}], (
        "Method 'update_animal' should update information about animal in Animal.alive"
    )


def test_carnivore_is_subclass():
    assert issubclass(Carnivore, Animal), (
        f"Carnivore class should be subclass of Animal"
    )


def test_herbivore_is_subclass():
    assert issubclass(Herbivore, Animal), (
        f"Herbivore class should be subclass of Animal"
    )


def test_carnivore_bite_not_hidden():
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    assert rabbit.health == 50, (
        "If initial health of rabbit equals 100 and rabbit is not hidden "
        "health should equal to 50 after bite."
    )
    assert Animal.alive == [
        {"name": "King Lion", "health": 100, "hidden": False},
        {"name": "Susan", "health": 50, "hidden": False}
    ], "Information in Animals.alive should update after each change"


def test_carnivore_bite_hidden():
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 100, (
        "Carnivore cannot bite hidden herbivore"
    )
    assert Animal.alive == [
        {"name": "King Lion", "health": 100, "hidden": False},
        {"name": "Susan", "health": 100, "hidden": True}
    ], "Carnivore cannot bite hidden animal"


def test_carnivore_bite_to_death():
    Animal.alive = []
    lion = Carnivore("King Lion")
    pantera = Carnivore("Bagira")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    pantera.bite(rabbit)
    assert Animal.alive == [
        {"name": "King Lion", "health": 100, "hidden": False},
        {"name": "Bagira", "health": 100, "hidden": False}
    ], "There is no dead animal in Animals.alive"


def test_herbivore_hide():
    Animal.alive = []
    rabbit = Herbivore("Susan")
    rabbit.hide()
    assert Animal.alive == [{"name": "Susan", "health": 100, "hidden": True}], (
        "Information in Animals.alive should update after each change"
    )
