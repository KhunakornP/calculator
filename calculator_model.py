"""Logic and units for the calculator"""
from math import *
import enum


class CalculatorLogic:
    """logic for the calculator"""
    expression = ""
    history = []

    def calculate(self):
        """Calculates the expression"""
        update = False
        expression = self.format_input()
        expression = expression.replace("^", "**")
        expression = expression.replace("mod", "%")
        expression = expression.replace("log", "log10")
        expression = expression.replace("ln", "log")
        expression = expression.replace("log102", "log2")
        if expression == "":
            return "", False
        try:
            total = eval(expression)
        except:
            return None, False
        if not isinstance(total, (int, float)):
            total = ""
        if total != "":
            self.history.append(f'{self.expression} ='
                                f' {self.format_output(total)}')
            update = True
        self.expression = self.format_output(total)
        return self.format_output(total), update

    def add_to_display(self, item):
        """Adds the item to the display"""
        operators = MathOperators.return_operands()
        try:
            item = MathOperators(item).name
        except ValueError:
            pass
        if len(self.expression) <= 0:
            self.expression += str(item)
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
                        self.expression[-1] in ["d"] + operators):
                    self.expression += str(item)
                else:
                    self.expression = str(item) + self.expression + ")"
            else:
                self.expression += str(item)
        return self.format_input()

    def delete_display(self):
        """Deletes the last item on display"""
        self.expression = self.expression[:-1]
        return self.format_input()

    def clear_display(self):
        """Clears the display"""
        self.expression = ""
        return self.format_input()

    def format_input(self, value=0):
        """
        Formats the display for the calculator

        :param value: a string to format instead of th expression
        :return: a formatted string
        """
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
        """Formats the output of the computation"""
        if isinstance(value, int):
            return f'{value:.12g}'
        return f"{value:.8g}"

    def get_history(self, expression: str):
        """Gets the selected history equation and add it to the display"""
        equation = expression.partition("=")
        if equation[1] == "=":
            self.expression = equation[0].rstrip(" ")
            return self.expression
        return self.format_input()

    def get_history_result(self, expression):
        """Gets the result from the history and adds it to the display"""
        equation = expression.partition("=")
        if equation[1] == "=":
            self.expression = equation[2]
            return self.expression
        return self.format_input()

    def display_history(self):
        """Formats the display for the calculator"""
        equations = [self.format_input(x) for x in self.history]
        return equations

    def update_operations(self):
        """Updates the calculator on the list of all possible MathOperators"""
        return MathOperators.return_values()


class MathOperators(enum.Enum):
    """Class to represent math operators"""
    Q = "sqrt"
    L = "log"
    W = "log2"
    N = "ln"
    E = "exp"
    S = "sin"
    C = "cos"
    T = "tan"

    @classmethod
    def return_operands(cls):
        """Returns a list of all abbreviated math operators"""
        return [x.name for x in list(MathOperators)]

    @classmethod
    def return_values(cls):
        """Returns a list of all values in the math operators"""
        return [x.value for x in list(MathOperators)]
