import tkinter as tk


class Keypad(tk.Frame):
    """A keypad widget for tkinter"""

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, kwargs)
        self.keynames = keynames
        self.init_components(columns)

    @property
    def frame(self):
        """Getter for the keypad's frame"""
        return super()

    def init_components(self, columns) -> None:
        """Create a keypad of keys using the keynames list.
        The first keyname is at the top left of the keypad and
        fills the available columns left-to-right, adding as many
        rows as needed.
        :param columns: number of columns to use
        """
        settings = {"padx": 2, "pady": 2, "sticky": tk.NSEW}
        column = 0
        row = 0
        for key in self.keynames:
            button = tk.Button(self, text=key)
            button.grid(column=column % columns, row=row // columns, **settings)
            self.rowconfigure(row // columns, weight=1)
            self.columnconfigure(column % columns, weight=1)
            column += 1
            row += 1

    def bind(self, sequence, func, add=''):
        """Bind an event handler to an event sequence."""
        for button in self.children.values():
            button.bind(sequence, func, add)

    def __setitem__(self, key, value) -> None:
        """Overrides __setitem__ to allow configuration of all buttons
        using dictionary syntax.

        Example: keypad['foreground'] = 'red'
        sets the font color on all buttons to red.
        """
        for button in self.children.values():
            button[key] = value

    def __getitem__(self, key):
        """Overrides __getitem__ to allow reading of configuration values
        from buttons.
        Example: keypad['foreground'] would return 'red' if the button
        foreground color is 'red'.
        """
        for button in self.children.values():
            return button.__getitem__(key)

    def configure(self, cnf=None, **kwargs):
        """Apply configuration settings to all buttons.

        To configure properties of the frame that contains the buttons,
        use `keypad.frame.configure()`.
        """
        for button in self.children.values():
            button.configure(cnf, **kwargs)

    def set_button(self, index, key, value):
        """Configures a specific button in the keypad"""
        if index == 1:
            index = ""
        for button in self.children.keys():
            if button == f"!button{index}":
                self.children[button][key] = value
                return

    def bind_button(self, sequence, function, index, add=''):
        """Binds a specific button to an event"""
        if index == 1:
            index = ""
        for button in self.children.keys():
            if button == f"!button{index}":
                self.children[button].bind(sequence, function, add)
                return


# test cases to be removed
if __name__ == "__main__":
    root = tk.Tk()
    def hahahhaha(*args):
        print("hahahhahahah")
    keypad = Keypad(root, list('789456123'), 3)
    keypad.set_button(1, "fg", "red")
    keypad.bind_button('<Button>', hahahhaha, 1)
    keypad.pack()
    root.mainloop()