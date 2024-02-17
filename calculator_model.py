from math import *
import enum


class CalculatorLogic:
    """logic for the calculator"""
    expression = ""

    def calculate(self):
        expression = self.format_input()
        if expression == "":
            return ""
        expression = expression.replace("^", "**")
        try:
            total = eval(expression)
        except:
            return None
        if isinstance(total, object):
            total = ""
        self.expression = str(total)
        return total

    def add_to_display(self, item):
        try:
            item = MathOperators(item).name
        except ValueError:
            pass
        self.expression += str(item)
        return self.format_input()

    def delete_display(self):
        self.expression = self.expression[:-1]
        return self.format_input()

    def clear_display(self):
        self.expression = ""
        return self.format_input()

    def format_input(self):
        index = 0
        expression = list(self.expression)
        for items in expression:
            if items in MathOperators.return_operands():
                expression[index] = MathOperators[items].value
            index += 1
        return ''.join(expression)



class MathOperators(enum.Enum):
    """Class to represent math operators"""
    S = "sqrt("
    L = "log"
    E = "exp("

    @classmethod
    def return_operands(cls):
        """Returns a list of all abbreviated math operators"""
        return [x.name for x in list(MathOperators)]


if __name__ == "__main__":
    cal = CalculatorLogic()
    cal.add_to_display("4")
    cal.add_to_display("^4")
    print(cal.calculate())