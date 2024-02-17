"""Controller for the calculator"""


from calculator_ui import CalculatorUI
from calculator_model import CalculatorLogic


class Controller:
    """"""
    def __init__(self):
        self.state = None
        mainframe = CalculatorUI()
        self.main = mainframe
        self.logic = CalculatorLogic()
        self.display_text = self.main.text
        self.main.operands["values"] = self.logic.update_operations()
        self.main.children["!keypad"].bind('<Button>', self.add_to_display)
        self.main.children["!keypad2"].bind('<Button>', self.add_to_display)
        self.main.children["!keypad"].bind_button('<Button>', self.delete_input, 10)
        self.main.children["!keypad2"].bind_button('<Button>', self.clear_input,7)
        self.main.children["!keypad2"].bind_button('<Button>',self.calculate, 8)
        self.main.children["!frame2"].children["!combobox"].bind('<<ComboboxSelected>>',lambda event:self.add_to_display(event, 1))
        self.main.children["!frame2"].children["!keypad"].bind('<Button>',self.add_to_display)
        self.main.children["!frame3"].children["!listbox"].bind('<<ListboxSelect>>',lambda event: self.add_to_display(event,2))

    def add_to_display(self, event, event_type=3):
        """
        Adds the input to the calculators display.
        """
        if event_type == 1:
            self.main.text.set(self.logic.add_to_display(
                                self.main.special.get()))
        elif event_type == 2:
            if event.widget.curselection() != ():
                selection = event.widget.curselection()
                self.main.text.set(self.logic.get_history(event.widget.get(selection)))
        elif event_type == 3:
            pressed_button = event.widget["text"]
            self.main.text.set(self.logic.add_to_display(pressed_button))

    def calculate(self, event):
        """
        Calculate the given characters on display using the model.
        """
        self.main.text.set(self.logic.calculate())
        self.get_history()

    def get_history(self):
        """Gets the history from the model and add it to the display"""
        self.main.history_info.set(self.logic.display_history())

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


if __name__ == "__main__":
    remote = Controller()
    remote.main.run()
