# Advanced Calculator with Extended Functionalities - Jessica San Roman 2025
from fractions import Fraction
import math as mt
import cmath
import statistics
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, optimize
import tkinter as tk

# ULTILITY FUNCTIONS

# Core logic functions for arithmetic operations
class arithmeticUtils:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
    @staticmethod
    def multiply(a, b):
        return a * b
    @staticmethod
    def divide(a, b):
        if b==0:
            raise ValueError("Cannot divide by zero")
        return a / b
    exit()
    # Core logic functions for fraction operations
    class fractionUtils:
        @staticmethod
        def add(a: Fraction, b: Fraction) -> Fraction:
            return a + b
        @staticmethod
        def subtract(a: Fraction, b: Fraction) -> Fraction:
            return a - b
        @staticmethod
        def multiply(a: Fraction, b: Fraction) -> Fraction:
            return (a * b)
        @staticmethod
        def divide(a: Fraction, b: Fraction) -> Fraction:
            if b==0:
                raise ValueError("Cannot divide by zero because it is undefined.")
            else:
                return a / b
        @staticmethod
        def simplify(fraction: Fraction) -> Fraction:
            return fraction.limit_denominator()
    exit()

# We'll use the functions from your core_logic.py
from arithmeticUtils import add, subtract, multiply, divide

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")

        # Create the display entry field
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        
        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        for button_text in buttons:
            tk.Button(self.master, text=button_text, width=7, height=2,
                      command=lambda text=button_text: self.on_button_click(text)
                     ).grid(row=row_val, column=col_val, padx=3, pady=3)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, text):
        if text == '=':
            try:
                # Get the expression from the display and use your logic
                current_expression = self.display.get()
                result = self.evaluate_expression(current_expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

    def evaluate_expression(self, expression):
        # This is a basic example. A real calculator would use a more robust
        # parser and handle operator precedence.
        parts = expression.split()
        if len(parts) == 3:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            if operator == '+': return add(num1, num2)
            if operator == '-': return subtract(num1, num2)
            if operator == '*': return multiply(num1, num2)
            if operator == '/': return divide(num1, num2)
        raise ValueError("Invalid expression")

root = tk.Tk()
my_gui = CalculatorGUI(root)
root.mainloop()


