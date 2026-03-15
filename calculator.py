# calculator.py

class Calculator:
    """
    A simple calculator class that handles arithmetic operations.
    """

    def __init__(self):
        self.current_expression = ""  # store the current input

    def add(self, value):
        """
        Add a number or operator to the current expression.
        """
        self.current_expression += str(value)

    def clear(self):
        """
        Clear the current expression.
        """
        self.current_expression = ""

    def calculate(self):
        """
        Evaluate the current expression and return the result.
        """
        try:
            result = eval(self.current_expression)  # calculate the result
            self.current_expression = str(result)   # update expression with result
            return result
        except Exception:
            self.current_expression = ""            # reset if error
            return "Error"