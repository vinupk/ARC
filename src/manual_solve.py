#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
###
### Name: Vinu Padmanabhan
### Student Id: 20236062
### GitHub repository: https://github.com/vinupk/ARC
###  

###===============================================================
###  Task - 6f8cd79b
###  Input : A pattern with a colour and different colour at the bottom left hand corner
###  Output: Paint the pattern with the colour at the bottom corner
###  Solution: Get shape of input matrix and get colour to paint the pattern
###  Loop through the array for each element, IF greater than 0, 
###     again IF its target paint colour
###  IF not paint colour then paint pattern with colour picked up from bottom corner
###     Else paint with 0 (Black)
###===============================================================
def solve_aabf363d(x):
    _testdata= np.array(x)
    _row, _colum = _testdata.shape
    _getColour = _testdata[_row-1,0]
    for ir, row in enumerate(_testdata):
        for ic, element in enumerate(row):
            if _testdata[ir, ic] > 0 :
                if _testdata[ir, ic] == _getColour:
                    _testdata[ir, ic] = 0
                else:
                    _testdata[ir, ic] = _getColour
    return _testdata   

###===============================================================
###  Task - c1d99e64
###  Input : A coloured pattern with empty rows and column
###  Output: Paint the empty rows and columns with orange colour
###  Solution: Get empty rows and column
###  Paint all empty rows and column with orange colour
###===============================================================
def solve_c1d99e64(x):
    _testdata= np.array(x)
    _row, _colum = _testdata.shape
    _getColour = 2
    zero_rows = np.where(~_testdata.any(axis=1))[0]
    zero_cols = np.where(~_testdata.any(axis=0))[0]

    for row in zero_rows:
        _testdata[row:row+1] = _getColour

    for col in zero_cols:
        _testdata[0:,col:col+1] = _getColour        
    return _testdata     

###===============================================================
###  Task - c1d99e64
###  Input : An empty grid
###  Output: Paint grid border with blue
###  Solution: Get row and column size
###  Paint top row, bottom row, 1st column and last column with blue
###===============================================================
def solve_6f8cd79b(x):
    _testdata= np.array(x)
    _row, _colum = _testdata.shape
    _getColour = 8
    _testdata[0:1] =_getColour
    _testdata[_row-1:_row] =_getColour
    _testdata[:,0] = _getColour
    _testdata[:,_colum-1] = _getColour      
    return _testdata


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    # if yhat has the right shape, then (y == yhat) is a bool array
    # and we test whether it is True everywhere. if yhat has the wrong
    # shape, then y == yhat is just a single bool.
    print(np.all(y == yhat))

if __name__ == "__main__": main()

