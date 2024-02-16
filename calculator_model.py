from math import *
import enum


class CalculatorLogic:
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
    S = "sqrt("
    L = "log"
    E = "exp("

    @classmethod
    def return_operands(cls):
        return [x.name for x in list(MathOperators)]


class DisplayLogic:
    pass


if __name__ == "__main__":
    cal = CalculatorLogic()
    print(cal.calculate("S4)"))
    print(cal.calculate("L2(2)"))
    print(cal.calculate(""))
