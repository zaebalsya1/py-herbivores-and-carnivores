import pytest
import ast
import inspect
import io

from contextlib import redirect_stdout

from app.main import Animal, Herbivore, Carnivore


def test_animal_class():
    assert hasattr(Animal, "alive"), (
        f"Animal class should have attribute 'alive'"
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
    assert len(Animal.alive) == 1, (
        "Constructor should add created animal to 'Animal.alive'"
    )
    assert Animal.alive[0].name == "Lion King", (
        "Constructor should add created animal to 'Animal.alive'"
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


def test_carnivore_bite_not_hidden():
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    assert rabbit.health == 50, (
        "If initial health of rabbit equals 100 and rabbit is not hidden "
        "health should equal to 50 after bite."
    )


def test_carnivore_bite_hidden():
    Animal.alive = []
    lion = Carnivore("King Lion")
    rabbit = Herbivore("Susan")
    rabbit.hide()
    lion.bite(rabbit)
    assert rabbit.health == 100, (
        "Carnivore cannot bite hidden herbivore"
    )


def test_carnivore_bite_to_death():
    Animal.alive = []
    lion = Carnivore("King Lion")
    pantera = Carnivore("Bagira")
    rabbit = Herbivore("Susan")
    lion.bite(rabbit)
    pantera.bite(rabbit)
    assert len(Animal.alive) == 2, (
        f"It shouldn't be dead animals in Animals.alive"
    )


def test_herbivore_hide():
    Animal.alive = []
    rabbit = Herbivore("Susan")
    rabbit.hide()
    assert rabbit.hidden is True, (
        "Method 'hide' should change animal attribute 'hidden'"
    )
    rabbit.hide()
    assert rabbit.hidden is False, (
        "Method 'hide' should change animal attribute 'hidden'"
    )


def test_print_animal_alive():
    Animal.alive = []

    lion = Carnivore("King Lion")
    pantera = Carnivore("Bagira")
    rabbit = Herbivore("Susan")

    f = io.StringIO()

    with redirect_stdout(f):
        print(Animal.alive)

    out = f.getvalue()
    output = "[{Name: King Lion, Health: 100, Hidden: False}, " \
             "{Name: Bagira, Health: 100, Hidden: False}, " \
             "{Name: Susan, Health: 100, Hidden: False}]\n"
    assert out == output, (
        f"Output should equal to {output} when you print 'Animal.alive' with "
        f"three animals"
    )
