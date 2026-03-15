# main.py

from calculator import Calculator
from gui import CalculatorGUI

def main():
    # Create the calculator logic object
    calc = Calculator()

    # Pass it to the GUI
    app = CalculatorGUI(calc)

    # Run the GUI
    app.run()

if __name__ == "__main__":
    main()