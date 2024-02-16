"""Controller for the calculator"""
from calculator_ui import CalculatorUI


class Controller:
    """"""
    def __init__(self):
        mainframe = CalculatorUI()
        mainframe.run()

    def add_to_display(self):
        """
        Adds the input to the calculators display.
        """
        pass

    def calculate(self):
        """
        Calculate the given characters on display using the model.
        """
        pass

    def get_history(self):
        """Gets the history from the model and add it to the display"""
        pass

    def delete_input(self):
        pass

    def clear_input(self):
        pass


if __name__ == "__main__":
    remote = Controller()