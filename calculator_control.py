"""Controller for the calculator"""
from calculator_ui import CalculatorUI
import abc


class Controller:
    """"""
    def __init__(self):
        self.state = None
        mainframe = CalculatorUI()
        self.main = mainframe
        self.display_text = mainframe.text
        mainframe.bind('<Button>', self.add_to_display)

    def add_to_display(self, event):
        """
        Adds the input to the calculators display.
        """
        pressed_button = event.widget["text"]
        self.display_text.set(self.display_text.get() + str(pressed_button))

    def calculate(self):
        """
        Calculate the given characters on display using the model.
        """
        pass

    def get_history(self):
        """Gets the history from the model and add it to the display"""
        pass

    def delete_input(self):
        """
        While the controller is in the active state delete the last,
        character in the display.
        While the controller is in the inactive state delete the entire,
        expression on display.
        """
        pass

    def clear_input(self):
        """Clear the user input in the display"""
        pass


class CalculatorState(abc.ABC):
    @abc.abstractmethod
    def delete_input(self):
        """Deletes the input"""
        raise NotImplementedError


class ActiveCalculator(CalculatorState):
    def delete_input(self):
        pass


class InactiveCalculator(CalculatorState):
    def delete_input(self):
        pass


if __name__ == "__main__":
    remote = Controller()