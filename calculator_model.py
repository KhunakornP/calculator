from math import *
import enum


class CalculatorLogic:
    """Computation logic for the calculator"""
    def calculate(self, expression):
        expression = self.format_input(expression)
        try:
            total = eval(expression)
        except:
            return None
        return total

    def format_input(self, expression):
        index = 0
        expression = list(expression)
        for items in expression:
            if items in MathOperators.return_operands():
                expression[index] = MathOperators[items].value
            index += 1
        return "".join(expression)


class MathOperators(enum.Enum):
    """Class to represent math operators"""
    S = "sqrt("
    L = "log"
    E = "exp("

    @classmethod
    def return_operands(cls):
        """Returns a list of all abbreviated math operators"""
        return [x.name for x in list(MathOperators)]


class DisplayLogic:
    """A class to handle the display"""
    pass


if __name__ == "__main__":
    cal = CalculatorLogic()
    print(cal.calculate("S4)"))
    print(cal.calculate("L2(2)"))
    print(cal.calculate("E()"))
