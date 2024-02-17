"""Controller for the calculator"""
from calculator_ui import CalculatorUI
from calculator_model import CalculatorLogic
import abc


class Controller:
    """"""
    def __init__(self):
        self.state = None
        mainframe = CalculatorUI()
        self.main = mainframe
        self.logic = CalculatorLogic()
        self.display_text = mainframe.text
        mainframe.children["!keypad"].bind('<Button>', self.add_to_display)
        mainframe.children["!keypad2"].bind('<Button>', self.add_to_display)
        mainframe.children["!keypad"].bind_button('<Button>', self.delete_input, 10)
        mainframe.children["!keypad2"].bind_button('<Button>', self.clear_input,9)
        mainframe.children["!keypad2"].bind_button('<Button>',self.calculate, 10)
        mainframe.children["!keypad3"].bind('<Button>', self.add_to_display)
    def add_to_display(self, event):
        """
        Adds the input to the calculators display.
        """
        pressed_button = event.widget["text"]
        self.main.text.set(self.logic.add_to_display(pressed_button))

    def calculate(self, event):
        """
        Calculate the given characters on display using the model.
        """
        self.main.text.set(self.logic.calculate())

    def get_history(self):
        """Gets the history from the model and add it to the display"""
        pass

    def delete_input(self, event):
        """
        While the controller is in the active state delete the last,
        character in the display.
        While the controller is in the inactive state delete the entire,
        expression on display.
        """
        self.main.text.set(self.logic.delete_display())

    def clear_input(self, event):
        """Clear the user input in the display"""
        self.main.text.set(self.logic.clear_display())


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
    remote.main.run()