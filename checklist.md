# Сheck Your Code Against the Following Points:

## Code Efficiency

1. Use the class name to get access to the class attributes:

Good example:

```python
class Person:
    city = "Kyiv"

    def __init__(self, name: str):
        self.name = name
        
    @staticmethod    
    def print_city():
        print(Person.city)

liz = Person("Liz")
liz.print_city()
```

Bad example:

```python
class Person:
    city = "Kyiv"

    def __init__(self, name: str):
        self.name = name
        
    def print_city(self):
        print(self.city)

liz = Person("Liz")
liz.print_city()
```

2. You can change the `bool` value in one line:

Good example:

```python
is_married = True

is_married = not is_married
```

Bad example:

```python
is_married = True

if is_married:
    is_married = False
else:
    is_married = True
```

3. Use the static method when needed.

## Code Style

4. Use annotation, it is a good practice:

Good example:

```python
def multiply_by_2(number: int):
    return number * 2
```

Bad example:
```python
def multiply_by_2(number):
    return number * 2
```

5. Make sure you use the double quotes everywhere.

6. Use interpolation instead of concatenation:

Good example:

```python
def print_full_name(name: str, surname: str):
    return f"{{Name: {name}, surname: {surname}}}"
```

Bad example:

```python
def print_full_name(name: str, surname: str):
    return "{" + "Name:" + name + ", surname:" + surname + "}"
```

7. Use descriptive and correct variable names:

Good example:

```python
def get_full_name(first_name: str, last_name: str):
    return f"{first_name} {last_name}"
```

Bad example:
```python
def get_full_name(x: str, y: str):
    return f"{x} {y}"
```

## Clean Code

8. Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
