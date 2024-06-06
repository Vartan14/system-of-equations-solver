# Linear Equation Solver

This project is a graphical user interface (GUI) application for solving systems of linear algebraic equations (SLAE) using various methods. The application is developed in Python, utilizing `tkinter` for the GUI, `numpy` for numerical computations, and `matplotlib` for plotting.

## Features

- **Matrix Input:** Users can input the coefficients of the linear equations manually or load them from a text file.
- **Random Matrix Generation:** Users can generate random matrices with specified dimensions.
- **Solution Methods:** Supports three methods for solving SLAE:
  - Gaussian Elimination
  - Gauss-Jordan Elimination
  - Rotation Method
- **Graphical Solution:** For 2x2 systems, the solution can be visualized graphically.
- **Saving Solutions:** Solutions can be saved to a text file.

## GUI Components

### Main Window

The main window consists of several frames and widgets for interaction:

- **Size Selection:** A combo box for selecting the dimension of the matrix.
- **Matrix Input Fields:** Entry widgets for entering the coefficients of the equations.
- **Method Selection:** Radio buttons for choosing the solution method.
- **Generate Button:** Generates a random matrix.
- **Solve Button:** Solves the system using the selected method and displays the solution.

### Solution Window

The solution window displays the results of the computations:

- **Solution Display:** Shows the values of the variables.
- **Iterations Count:** Displays the number of iterations taken to reach the solution.
- **Save Button:** Allows saving the solution and matrix to a file.
- **Graph Plot:** For 2x2 systems, a graphical representation of the solution.

## Classes and Files

### Main Components

- **Window:** Handles the main GUI components and user interactions.
- **Matrix:** Represents the matrix and implements the solution methods.
- **SolutionWindow:** Displays the solution and additional information.
- **Graphic:** Handles the plotting of the graphical solution.

### Supporting Files

- **config.py:** Contains configuration variables like colors and fonts.
- **Matrix.py:** Implements the matrix operations and solution algorithms.
- **SolutionWindow.py:** Implements the window for displaying the solution.
- **Graphic.py:** Implements the graphical plotting of solutions.
- **GUI.py:** Contains the main execution logic for starting the application.

## Usage

1. **Run the Application:** Execute the main script to start the GUI.
2. **Select Matrix Size:** Use the combo box to select the dimension of the matrix.
3. **Input Matrix Coefficients:** Enter the coefficients manually or load from a file.
4. **Select Solution Method:** Choose the desired method for solving the system.
5. **Generate Random Matrix (Optional):** Use the "Generate" button to create a random matrix.
6. **Solve the System:** Click the "Solve" button to find the solution.
7. **View and Save Solution:** View the solution in the solution window and save if needed.

## Dependencies

- `numpy`
- `tkinter`
- `matplotlib`

## Installation

To run this project, you need to have Python installed along with the required dependencies. You can install the dependencies using `pip`:

```bash
pip install numpy matplotlib
```

## Running the Application

Execute the following command to start the application:

```bash
python main.py
```
