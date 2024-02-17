"""Logic and units for the calculator"""
from math import *
import enum


class CalculatorLogic:
    """logic for the calculator"""
    expression = ""
    history = []

    def calculate(self):
        expression = self.format_input()
        expression = expression.replace("^", "**")
        expression = expression.replace("mod", "%")
        if expression == "":
            return ""
        try:
            total = eval(expression)
        except:
            return None
        if not isinstance(total, (int, float)):
            total = ""
        if total != "":
            self.history.append(f'{self.expression} = {self.format_output(total)}')
        self.expression = self.format_output(total)
        return self.format_output(total)

    def add_to_display(self, item):
        operators = MathOperators.return_operands()
        try:
            item = MathOperators(item).name
        except ValueError:
            pass
        if len(self.expression) <= 0:
            self.expression += item
            return self.format_input()
        operands = ["+", "-", "/", "^", "*"]
        if len(self.expression) > 0 and self.expression[-1] in operands:
            if item in operands:
                self.expression = self.expression[:-1]
                self.expression += item
            else:
                self.expression += str(item)
        else:
            if item in operators:
                if (len(self.expression) > 0 and
                        self.expression[-1] in operators):
                    self.expression += str(item)
                else:
                    self.expression = str(item) + self.expression + ")"
            else:
                self.expression += str(item)
        return self.format_input()

    def delete_display(self):
        self.expression = self.expression[:-1]
        return self.format_input()

    def clear_display(self):
        self.expression = ""
        return self.format_input()

    def format_input(self, value=0):
        index = 0
        expression = list(self.expression)
        if value:
            expression = list(value)
        for items in expression:
            if items in MathOperators.return_operands():
                expression[index] = MathOperators[items].value + "("
            index += 1
        return ''.join(expression)

    def format_output(self, value):
        if isinstance(value, int):
            return f'{value:.0f}'
        return f"{value:.8g}"

    def get_history(self, expression: str):
        equation = expression.partition("=")
        if equation[1] == "=":
            self.expression = equation[0]
            return self.expression
        return self.format_input()

    def display_history(self):
        equations = [self.format_input(x) for x in self.history]
        return equations

    def update_operations(self):
        return MathOperators.return_values()


class MathOperators(enum.Enum):
    """Class to represent math operators"""
    S = "sqrt"
    L = "log"
    T = "log2"
    E = "exp"

    @classmethod
    def return_operands(cls):
        """Returns a list of all abbreviated math operators"""
        return [x.name for x in list(MathOperators)]

    @classmethod
    def return_values(cls):
        return [x.value for x in list(MathOperators)]


if __name__ == "__main__":
    cal = CalculatorLogic()
    cal.add_to_display("4")
    cal.add_to_display("^4")
    print(cal.calculate())
    cal.clear_display()
    cal.add_to_display("4+5")
    print(cal.calculate())
    cal.clear_display()
    print(cal.calculate())
    print(cal.history)
