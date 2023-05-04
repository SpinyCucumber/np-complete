# Spring 2023 CS 470 Final Project

This project is a foray into the world of NP-Complete problems. It provides a brute-force solver for the **Subset Sum Problem** and some variations which add optimizations.
Reductions from the Subset Sum Problem to the **Boolean Satisfiability Problem** and from the **Partition Problem** to the Subset Sum Problem are also provided.
To facilitate sharing problem instances, the project provides a method for saving/loading problem data. We use the format defined in Yessick's Spring 2023 CS 470 course.

This project is written in Python and uses the [Sympy](https://www.sympy.org/en/index.html) library.

## Setting up Development Environment

First, ensure the "virtualenv" Python module is installed globally, and your Python version is 3.7 or greater.
Initialize a new virtual environment and enter it using:

```
python -m virtual .venv
./.venv/Scripts/activate
```

Install required packages using:

```
pip install -r requirements.txt
```

## Using the Project

This project is meant to be interacted with via the Python shell. To enter a Python shell with all project definitions already imported, the module can be executed like so:

```
python -i -m np_complete
```

For a comprehensive list of definitions, consult the [documentation](https://spinycucumber.github.io/np-complete/).

A [test](tests.py) file is also provided, which is a command-line interface to compare the speed of several subset sum algorithms.
To run the tests, use the following syntax:

```
python ./tests.py ./data/subset_sum_ethilty.dat 10000
```

where the first argument is the problem definition file and the second argument is the number of test iterations to run for each algorithm.