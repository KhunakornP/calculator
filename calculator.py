"""File to launch the calculator"""
from calculator_ui import CalculatorUI
from calculator_control import Controller
from calculator_model import CalculatorLogic


if __name__ == "__main__":
    interface = CalculatorUI()
    model = CalculatorLogic()
    controller = Controller(interface, model)
    controller.main.run()
