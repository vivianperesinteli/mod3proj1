# Mean, Variance, and Standard Deviation Calculator

This project is a solution for the "Mean-Variance-Standard Deviation Calculator" challenge from the Data Analysis with Python course by freeCodeCamp at the computing class in Inteli.

## Description

The project consists of a Python function, `calculate()`, which uses the NumPy library to perform statistical calculations on a list of 9 numbers. The list is converted into a 3x3 matrix, and the function calculates the mean, variance, standard deviation, maximum, minimum, and sum along the axes of the matrix and for the entire matrix.

## File Structure

- `mean_var_std.py`: Contains the main logic of the `calculate()` function.
- `main.py`: Entry point to test the function and run unit tests.
- `test_module.py`: Contains unit tests to ensure the `calculate()` function works as expected.
- `requirements.txt`: Lists the project dependencies (NumPy only).
- `README.md`: This file.

## How to Run

1. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Run the program and tests:**
    ```sh
    python main.py
    ```

    This will print the result of a sample calculation and then run all unit tests defined in `test_module.py`.
