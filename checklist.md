# Сheck your code against the following points:

1. Make sure you are using double quotes everywhere.
2. When you write your code you can add comments, prints, functions to check your solution. 
   Don't forget to delete all this when you are ready to commit and push your code.
3. Use descriptive and correct variable names.

Bad example:
```python
def get_full_name(x: str, y: str):
    return f"{x} {y}"
```

Good example:

```python
def get_full_name(first_name: str, last_name: str):
    return f"{first_name} {last_name}"
```

4. Using annotation is a good practice:

Bad example:
```python
def multiply_by_2(number):
    return number * 2
```

Good example:

```python
def multiply_by_2(number: int):
    return number * 2
```

5. Use class name to get access to the class atrributes:

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

6. You can change `bool` value in a one line:

Bad example:

```python
is_married = True

if is_married:
    is_married = False
else:
    is_married = True
```

Good example:

```python
is_married = True

is_married = not is_married
```

7. Use static methods when needed.
8. Use interpolation instead of concatenation:

Bad example:

```python
def print_full_name(name: str, surname: str):
    return "{" + "Name:" + name + ", surname:" + surname + "}"
```

Good example:

```python
def print_full_name(name: str, surname: str):
    return f"{{Name: {name}, surname: {surname}}}"
```
