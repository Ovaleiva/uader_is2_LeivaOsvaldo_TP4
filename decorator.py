class Number:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Valor:", self.value)

    def add_two(self):
        self.value += 2

    def multiply_by_two(self):
        self.value *= 2

    def divide_by_three(self):
        self.value /= 3


class Decorator:
    def __init__(self, number):
        self.number = number

    def print_and_apply_operation(self, operation):
        self.number.print_value()
        operation()
        self.number.print_value()


number = Number(10)
decorated_number = Decorator(number)

# Sin agregados
number.print_value()

# Con las operaciones aplicadas usando el decorador
print("Sumar 2:")
decorated_number.print_and_apply_operation(number.add_two)
print("Multiplicar por 2:")
decorated_number.print_and_apply_operation(number.multiply_by_two)
print("Dividir por 3:")
decorated_number.print_and_apply_operation(number.divide_by_three)

