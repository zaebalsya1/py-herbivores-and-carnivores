import pytest
import ast
import inspect

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


@pytest.mark.parametrize(
    "class_,method",
    [
        (Herbivore, "hide"),
        (Carnivore, "bite"),
    ],
)
def test_only_one_method_should_be_declared_in_each_of_children_classes(
    class_, method
):
    class_source = inspect.getsource(class_)
    parsed_class = ast.parse(class_source)
    assert [name.id for name in parsed_class.body[0].bases] == [
        "Animal"
    ], f"'{class_.__name__}' should be inherited from 'Animal'"
    assert (
        len(parsed_class.body[0].body) == 1
    ), f"Only one method '{method}' should be defined inside class '{class_.__name__}'"
    assert (
        parsed_class.body[0].body[0].name == method
    ), f"Only one method '{method}' should be defined inside class '{class_.__name__}'"


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
