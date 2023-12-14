# Kompozite Technical Test - Part II

## Introduction

This is the second part of the Kompozite technical test. In this part, you will be asked to refactor and to extend an existing python script.
You may or may not start by the second part of the test.

This folder contains:

- A `readme.md` file: this file
- An empty `data` folder
- A `requirements.txt` file: the list of the dependencies of the script.
- A `main.py` python file: the main script to run, the script contains a `main` function that can be run as a python script whose purpose is to cut an existing 
                        csv or excel file into smaller files. The script should be able to run as a python script with the following command: `python main.py`.
- A `tests.py` python file: a file containing some automated tests to check that the script is working as expected
- A `data.xlsx` excel file: used to test the script and to run the tests in `tests.py`

The purpose of this part of the test is to check your python knowledge and your ability to write clean and maintainable code.


## Instructions

Q1. In a git branch called refactoring. Refactor and clean the code in `main.py` to make it more readable and maintainable. You can add as many files as you want to the folder, but you should not modify the `tests.py` file. At the end of the refactoring the `main.py` should still contain a `main` function that can be run as a python script.

Q2. In a git branch called feature. Create a new feature that allows to do the opposite of the `main` function. More precisely, this new feature should be able to merge several csv or excel files into a single file. The new feature should be able to run as a python script with the following command: `python <feature_filename>.py`.

Q3. (Bonus) In a git branch called bonus. Reconcile the previous two branches. 

## Notes and tips

You will need to have  python 3, with `pandas` and `openpyxl` installed. 
You can install the dependencies with the following command: `pip install -r requirements.txt`

You can either run the tests in `tests.py` with the following command: `python tests.py` or run them with `pytest tests.py`.
However, to run them with pytest, you will need to have pytest installed. 
If you have previously installed the dependencies with the command `pip install -r requirements.txt`, you should already have pytest installed.
Otherwise, you can install it with the following command: `pip install pytest`.