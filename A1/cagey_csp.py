# =============================
# Student Names: Manny Cassar 
# Group ID:
# Date:
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all variables in the given csp. If you are returning an entire grid's worth of variables
they should be arranged in a linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 20/100 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *
from itertools import permutations as permute
from itertools import product

def binary_ne_grid(cagey_grid):
    '''
    A model of a Cagey grid (without cage constraints) built using only
    binary not-equal constraints for both the row and column constraints.
    '''
    size = cagey_grid[0]
    globalDomain = list(range(1, size+1))

    # index i represents the ith row of the grid
    rowVariables = []
    # index i represents the ith col of the grid
    colVariables = []

    variables = [] 
    constraints = []
    satTuples = []

    # Name all variables based on position (assuming 3x3 board):
    # [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]) = rowVaraibles
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]] = colVariables
    variables, rowVariables, colVariables = rowsColsVars(size, globalDomain)

    # Generating binary_ne satisfying tuples for pairs of variables in the
    # same row or col:
    for sat_tuple in permute(globalDomain, 2):
        satTuples.append(sat_tuple)


    # Generate the connstraints between avriables in the save row, then col
    for row in rowVariables:
        permutes = permute(row, 2)
        for v1, v2 in permutes:
            constraintName = v1.name + "|" + v2.name
            constraint = Constraint(constraintName, [v1, v2])
            constraint.add_satisfying_tuples(satTuples)
            constraints.append(constraint)
    for col in colVariables:
        permutes = permute(col, 2)
        for v1, v2 in permutes:
            constraintName = v1.name + "|" + v2.name
            constraint = Constraint(constraintName, [v1, v2])
            constraint.add_satisfying_tuples(satTuples)
            constraints.append(constraint)

    # Now, initialize the CSP
    csp = CSP("binary_ne_grid", variables)

    # Add the constraints to the csp
    for constraint in constraints:
        csp.add_constraint(constraint)
    
    return csp, variables

def nary_ad_grid(cagey_grid):
    ## IMPLEMENT
    '''
    A model of a Cagey grid (without cage constraints) built using only
    nary allDiff constraints for both the row and column constraints.
    '''
    size = cagey_grid[0]
    globalDomain = list(range(1, size+1))

    # index i represents the ith row of the grid
    rowVariables = []
    # index i represents the ith col of the grid
    colVariables = []

    variables = [] 
    constraints = []
    satTuples = []

    # Name all variables based on position (assuming 3x3 board):
    # [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]) = rowVaraibles
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]] = colVariables
    variables, rowVariables, colVariables = rowsColsVars(size, globalDomain)

    # Generating nary_ad satisfying tuples for pairs of variables in the
    # same row or col:
    for sat_tuple in permute(globalDomain, size):
        satTuples.append(sat_tuple)

    # Generate the connstraints between avriables in the save row, then col
    for i in range(len(rowVariables)):
        row = rowVariables[i]
        constraintName = "row" + str(i)
        constraint = Constraint(constraintName, row)
        constraint.add_satisfying_tuples(satTuples)
        constraints.append(constraint)
    for i in range(len(colVariables)):
        col = colVariables[i]
        constraintName = "col" + str(i)
        constraint = Constraint(constraintName, col)
        constraint.add_satisfying_tuples(satTuples)
        constraints.append(constraint)
        

    # Now, initialize the CSP
    csp = CSP("nary_ad_grid", variables)

    # Add the constraints to the csp
    for constraint in constraints:
        csp.add_constraint(constraint)
    
    return csp, variables
    
def cagey_csp_model(cagey_grid):
    csp, variables = nary_ad_grid(cagey_grid)
    csp.name = "cagey_csp_model" # not sure if this will break uniqueness
    cageConstraints = []

    cages = cagey_grid[1]
    # Each cage will have a constraint
    for c in range(len(cages)):
        cage = cages[c]
        cageName = "cage" + str(c)
        #Cage constraint handler for easy parsing!
        currCageConstraint = generateCageConstraint(variables, cage, cageName)
        csp.add_constraint(currCageConstraint)
            
    return csp, csp.get_all_vars()

def generateCageConstraint(cspVariables, cage, cageName):
    varDomains = []
    cageSatTuples = []

    answer = cage[0]
    cageVariables = cage[1]
    op = cage[2]

    constraint = Constraint(cageName, cageVariables)

    cspVarNames = []
    for cspVar in cspVariables:
        cspVarNames.append(cspVar.name)
    
    for varTuple in cageVariables:
        x = varTuple[0]
        y = varTuple[1]
        varSearchName = str(x) + str(y)

        currVar = cspVariables[cspVarNames.index(varSearchName)]
        varDomains.append(currVar.domain())

    domainCartesianProduct = product(*varDomains)
    for variableDomain in domainCartesianProduct:
        response = opHandler(op, variableDomain, answer)
        if response != []:
            cageSatTuples.append(response)
    constraint.add_satisfying_tuples(cageSatTuples)

    return constraint

# Recursive operation handler for ?, otherwise runs once
# I would really like some style points here! :)
def opHandler(op, variableDomain, answer):
    satTuples = []
    if op == "+":
        summation = 0
        for possibleValue in variableDomain:
            summation += possibleValue
        if (summation == answer):
            satTuples.append(variableDomain)
    elif op == "-":
        for possibleValue in permute(variableDomain):
            subtractant = possibleValue[0]
            for n in range(1, len(possibleValue)):
                subtractant -= possibleValue[n]
            if(subtractant == answer):
                satTuples.append(variableDomain)
    elif op == "*":
        product = 1
        for possibleValue in variableDomain:
            product *= possibleValue
        if (product == answer):
            satTuples.append(variableDomain)
    elif op == "/":
        for possibleValue in permute(variableDomain):
            quotient = possibleValue[0]
            for n in range(1, len(possibleValue)):
                quotient = quotient/possibleValue[n]
            if(quotient == answer):
                satTuples.append(variableDomain)
    else: # ? OPERATOR
        satTuples.append(opHandler("+", variableDomain, answer))
        satTuples.append(opHandler("-", variableDomain, answer))
        satTuples.append(opHandler("*", variableDomain, answer))
        satTuples.append(opHandler("/", variableDomain, answer))
    return list(dict.fromkeys(satTuples)) # remving duplicates if 1x1 cage

def rowsColsVars(size, globalDomain):
    variables = [] 
    # index i represents the ith row of the grid
    rowVariables = []
    # index i represents the ith col of the grid
    colVariables = []

    for row in range(size):
        currRow = []
        for col in range(size):
            currVarName = str(row + 1)+str(col + 1)
            currVar = Variable(currVarName, globalDomain)

            variables.append(currVar)
            currRow.append(currVar)
        rowVariables.append(currRow)
    
    for col in range(size):
        currCol = []
        for row in rowVariables:
            currCol.append(row[col])
        colVariables.append(currCol)

    return variables, rowVariables, colVariables
    