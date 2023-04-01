# =============================
# Student Names: Manny Cassar
# Group ID: 92
# Date: Jan 30, 2023
# =============================
# CISC 352 - W23
# propagators.py
# desc: This file will contain different constraint propagators to be used within
#       bt_search.
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   bt_search.

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

    The propagator returns True/False and a list of (Variable, Value) pairs.
    Return is False if a deadend has been detected by the propagator.
    in this case bt_search will backtrack. Return is true if we can continue.

    The list of variable values pairs are all of the values
    the propagator pruned (using the variable's prune_value method).
    bt_search NEEDS to know this in order to correctly restore these
    values when it undoes a variable assignment.

    NOTE propagator SHOULD NOT prune a value that has already been
    pruned! Nor should it prune a value twice

    PROPAGATOR called with newly_instantiated_variable = None
    PROCESSING REQUIRED:
    for plain backtracking (where we only check fully instantiated
    constraints)
    we do nothing...return true, []

    for forward checking (where we only check constraints with one
    remaining variable)
    we look for unary constraints of the csp (constraints whose scope
    contains only one variable) and we forward_check these constraints.

    for gac we establish initial GAC by initializing the GAC queue
    with all constaints of the csp


    PROPAGATOR called with newly_instantiated_variable = a variable V
    PROCESSING REQUIRED:
        for plain backtracking we check all constraints with V (see csp method
        get_cons_with_var) that are fully assigned.

        for forward checking we forward check all constraints with V
        that have one unassigned variable left

        for gac we initialize the GAC queue with all constraints containing V.
   '''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check_tuple(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''
    Do forward checking. That is check constraints with
    only one uninstantiated variable. Remember to keep
    track of all pruned variable, value pairs and return 
       
    PROPAGATOR called with newly_instantiated_variable = None:
        for forward checking (where we only check constraints with one
        remaining variable). We look for unary constraints of the csp
        (constraints whose scope contains only one variable) and we
        forward_check these constraints.

    PROPAGATOR called with newly_instantiated_variable = a variable V:
        for forward checking we forward check all constraints with V
        that have one unassigned variable left

    Implement dead end detection, use prune_value to remove
    (variable, currDomainValue) pairs. Dont prune already pruned values 
    '''
    #Propogator called with newVar = None
    if not newVar:
        cons = csp.get_all_cons()
    #Propogator called with newVar representing the most recently assigned Variable
    else:
        cons = csp.get_cons_with_var(newVar)

    myPrunes = []
    #Forward check only constraint (con) in cons that have one unassigned variable left:
    for con in cons:
        if con.get_n_unasgn() == 1: # 1 unassigned variable
            #Forward check here:
            currVar = con.get_unasgn_vars().pop() #list of one var

            for possibleVal in currVar.cur_domain():
                # Assign the first available value from variable's domain
                currVar.assign(possibleVal)

                # From prop_BT, check if con is satisfied by the new assignment
                vals = []
                vars = con.get_scope()
                for var in vars:
                    vals.append(var.get_assigned_value())
                # If con not satisfied, prune possibleVal from currVar's current domain 
                if not con.check_tuple(vals): 
                    pruneCandidate = (currVar, possibleVal)
                    #Check if it has been pruned already
                    if pruneCandidate not in myPrunes:
                        myPrunes.append(pruneCandidate)
                        currVar.prune_value(possibleVal)
                currVar.unassign()

                if currVar.cur_domain_size() == 0: #Reached a dead end!
                    return False, myPrunes
    return True, myPrunes        


def prop_GAC(csp, newVar=None):
    '''
    Do GAC propagation. If newVar is None we do initial GAC enforce
    processing all constraints. Otherwise we do GAC enforce with
    constraints containing newVar on GAC Queue

    PROPAGATOR called with newly_instantiated_variable = None:
        for gac we establish initial GAC by initializing the GAC queue
    with all constaints of the csp
    PROPAGATOR called with newly_instantiated_variable = a variable V:
        for gac we initialize the GAC queue with all constraints containing V.  

    Implement dead end detection, use prune_value to remove
    (variable, currDomainValue) pairs. Dont prune already pruned values 
    '''

    #Propogator called with newVar = None
    if not newVar:
        cons = csp.get_all_cons()
    #Propogator called with newVar representing the most recently assigned Variable
    else:
        cons = csp.get_cons_with_var(newVar)
    
    myPrunes = []
    # Forward check all constraints:
    for con in cons:
        # Go through each variable in the constraint, see if its domain can be pruned
        for currVar in con.get_scope():
            # each possible domain val is tested for pruning
            for possibleVal in currVar.cur_domain():
                pruneCandidate = (currVar, possibleVal)

                #Has a satisfying tuple in con after assignment
                if not con.check_var_val(pruneCandidate[0], pruneCandidate[1]):
                    # Check if it has been pruned already
                    if pruneCandidate not in myPrunes:
                        myPrunes.append(pruneCandidate)
                        currVar.prune_value(possibleVal)
                
                if currVar.cur_domain_size() == 0: # Reached a dead end!
                    return False, myPrunes

    return True, myPrunes
