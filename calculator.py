"""File to launch the calculator"""
from calculator_ui import CalculatorUI
from calculator_control import Controller


if __name__ == "__main__":
    interface = CalculatorUI()
    controller = Controller(interface)
    controller.main.run()
