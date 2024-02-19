"""Controller for the calculator"""


from calculator_ui import CalculatorUI
from calculator_model import CalculatorLogic


class Controller:
    """"""
    def __init__(self, ui):
        self.state = None
        self.main = ui
        self.logic = CalculatorLogic()
        self.display_text = self.main.text
        self.main.operands["values"] = self.logic.update_operations()
        self.bind_components()

    def bind_components(self):
        """Binds the components in the ui to their respective handlers"""
        keypad1 = self.main.children["!keypad"]
        keypad2 = self.main.children["!keypad2"]
        frame2 = self.main.children["!frame2"]
        keypad1.bind('<Button>', self.add_to_display)
        keypad2.bind('<Button>', self.add_to_display)
        keypad1.bind_button('<Button>', self.delete_input, 10)
        keypad2.bind_button('<Button>', self.clear_input, 7)
        keypad2.bind_button('<Button>', self.calculate, 8)
        frame2.children["!combobox"].bind('<<ComboboxSelected>>',
                                          lambda event: self.add_to_display(
                                              event, 1))
        frame2.children["!keypad"].bind('<Button>', self.add_to_display)
        self.main.children["!frame3"].children["!listbox"].bind(
            '<Button-1>', lambda event: self.add_to_display(event, 2))
        self.main.children["!frame3"].children["!listbox"].bind(
            '<Button-3>', lambda event: self.add_to_display(event, 4))

    def add_to_display(self, event, event_type=3):
        """
        Adds the input to the calculators display depending on the event_type.
        """
        if event_type == 1:
            self.main.text.set(self.logic.add_to_display(
                                self.main.special.get()))
        elif event_type == 2:
            if event.widget.curselection() != ():
                selection = event.widget.curselection()
                self.main.text.set(self.logic.get_history(
                    event.widget.get(selection)))
        elif event_type == 3:
            pressed_button = event.widget["text"]
            self.main.text.set(self.logic.add_to_display(pressed_button))
        elif event_type == 4:
            if event.widget.curselection() != ():
                selection = event.widget.curselection()
                self.main.text.set(self.logic.get_history_result(
                    event.widget.get(selection)))

    def calculate(self, event):
        """
        Calculate the given characters on display using the model.
        """
        calculation = self.logic.calculate()
        self.main.clear_notification()
        if calculation[0] is None:
            self.main.notify_invalid_input()
        else:
            self.main.text.set(calculation[0])
        if calculation[1]:
            self.get_history()

    def get_history(self):
        """Gets the history from the model and add it to the display"""
        self.main.history_info.set(self.logic.display_history())

    def delete_input(self, event):
        """
        Deletes the last character in the display.
        """
        self.main.text.set(self.logic.delete_display())

    def clear_input(self, event):
        """Clear the user input in the display"""
        self.main.text.set(self.logic.clear_display())
        self.main.clear_notification()



if __name__ == "__main__":
    remote = Controller(CalculatorUI())
    remote.main.run()
