# gui.py
import tkinter as tk

class CalculatorGUI:
    """
    A graphical interface for the calculator using Tkinter.
    """

    def __init__(self, calculator):
        self.calculator = calculator

        # Create the main window
        self.window = tk.Tk()
        self.window.title("Simple Calculator")
        self.window.geometry("300x400")

        # Entry widget for displaying numbers and results
        self.display = tk.Entry(
            self.window,
            width=16,
            font=("Arial", 24),
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        self.display.pack(pady=10)

        # Create all buttons
        self.create_buttons()

    def create_buttons(self):
        """
        Create calculator buttons dynamically and arrange them in a grid.
        """
        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        frame = tk.Frame(self.window)
        frame.pack()

        row = 0
        col = 0

        for button in buttons:
            if button == "=":
                action = self.calculate
            else:
                action = lambda b=button: self.add_to_display(b)

            tk.Button(
                frame,
                text=button,
                width=5,
                height=2,
                font=("Arial", 14),
                command=action
            ).grid(row=row, column=col, padx=5, pady=5)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(
            self.window,
            text="Clear",
            width=20,
            height=2,
            command=self.clear_display
        ).pack(pady=10)

    # Button actions
    def add_to_display(self, value):
        self.calculator.add(value)
        self.update_display()

    def clear_display(self):
        self.calculator.clear()
        self.update_display()

    def calculate(self):
        result = self.calculator.calculate()
        self.update_display(result)

    def update_display(self, value=None):
        """
        Update the display widget.
        """
        self.display.delete(0, tk.END)
        if value is None:
            self.display.insert(0, self.calculator.current_expression)
        else:
            self.display.insert(0, value)

    def run(self):
        """
        Start the Tkinter main loop.
        """
        self.window.mainloop()