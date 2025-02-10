# =============================
# Student Names: Manny Cassar
# Group ID: 92
# Date: Febuary 3, 2023
# =============================
# CISC 352 - W23
# heuristics.py
# desc: This file will contain different constraint propagators to be used within
#       the propagators
#

'''
This file will contain different constraint propagators to be used within
the propagators

var_ordering == a function with the following template:
    var_ordering(csp)
        ==> returns Variable

csp is a CSP object---the heuristic can use this to get access to the
variables and constraints of the problem. The assigned variables can be
accessed via methods, the values assigned can also be accessed.

var_ordering returns the next Variable to be assigned, as per the definition
of the heuristic it implements.
'''
import operator
def ord_dh(csp):
    ''' 
    Return variable according to the Degree Heuristic:
        Variable in CSP involved in the largest number of constraints on other
        unassigned variables.
    '''

    varDict = dict.fromkeys(csp.get_all_unasgn_vars(), 0)

    #Go through each unassigned variable
    for var in varDict.keys():
        # Check each constraint with var in CSP
        for con in csp.get_cons_with_var(var):
            conUnassignedVars = con.get_unasgn_vars()
            # Check only constraints with a different unassigned var
            if var in conUnassignedVars:
                conUnassignedVars.remove(var)
    
            if len(conUnassignedVars) > 0:
                # Var involved in constraing on other Unassigned Variable,
                # increment it in dict!
                varDict[var] += 1
    # Return key of max value in varDict
    return max(varDict, key=varDict.get)

def ord_mrv(csp):
    '''
    Return variable according to the Minimum Remaining Values heuristic:
        Variable in CSP with the smallest current domain is returned
    '''
    varList = csp.get_all_unasgn_vars()

    if len(varList) <= 0: return None # Ensure values exist (CSP not complete)    

    # Store min domain, iterate thru vars, update minimim var and its domain
    minVar = varList[0]
    minVarDomain = varList[0].cur_domain_size()
    for var in varList[1:]:
        curDom = var.cur_domain_size()
        if curDom < minVarDomain:
            minVar = var
            minVarDomain = curDom

    return minVar
