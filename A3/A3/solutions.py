# solutions.py
# Manny Cassar
# 20213773 | 19mmc4
# March 26, 2023
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

'''Implement the methods from the classes in inference.py here'''

import util
from util import raiseNotDefined
import random
import busters

def normalize(self):
    """
    Normalize the distribution such that the total value of all keys sums
    to 1. The ratio of values for all keys will remain the same. In the case
    where the total value of the distribution is 0, do nothing.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> dist.normalize()
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0)]
    >>> dist['e'] = 4
    >>> list(sorted(dist.items()))
    [('a', 0.2), ('b', 0.4), ('c', 0.4), ('d', 0.0), ('e', 4)]
    >>> empty = DiscreteDistribution()
    >>> empty.normalize()
    >>> empty
    {}
    """
    "*** YOUR CODE HERE ***"

    total = self.total()
    if total == 0:
        return
    
    for key, val in self.items():
        normalizedVal = val / total
        self[key] = normalizedVal


def sample(self):
    """
    Draw a random sample from the distribution and return the key, weighted
    by the values associated with each key.

    >>> dist = DiscreteDistribution()
    >>> dist['a'] = 1
    >>> dist['b'] = 2
    >>> dist['c'] = 2
    >>> dist['d'] = 0
    >>> N = 100000.0
    >>> samples = [dist.sample() for _ in range(int(N))]
    >>> round(samples.count('a') * 1.0/N, 1)  # proportion of 'a'
    0.2
    >>> round(samples.count('b') * 1.0/N, 1)
    0.4
    >>> round(samples.count('c') * 1.0/N, 1)
    0.4
    >>> round(samples.count('d') * 1.0/N, 1)
    0.0
    """
    "*** YOUR CODE HERE ***"

    dist = self.copy()
    normalize(dist)

    # space between cum[i] and cum[i + 1] somewhere lies r
    # then return key at index i in dist
    cumTotal = [0] * (len(dist) + 1)

    for i in range(1, len(cumTotal)): # build cum table
        cumTotal[i] = cumTotal[i-1] + list(dist.values())[i - 1]
    
    r = random.randint(0, 100000) / 100000

    # Go through the cumDist and find out where r price is right (cant go over 1 tho)
    for i in range(len(cumTotal[:len(cumTotal) - 1])):
        if r >= cumTotal[i] and r < cumTotal[i + 1]:
            return list(self.keys())[i]
    return # nothing if empty dist


def getObservationProb(self, noisyDistance, pacmanPosition, ghostPosition, jailPosition):
    """
    Return the probability P(noisyDistance | pacmanPosition, ghostPosition).
    Given P(noisyDistance | trueDistance), so:
    a = noisyDistance
    b = pacmanPosition
    c = ghostPosition
    d = trueDistance

    P(d| b, c) and P(a| d) are given, must find P(a| b, c):

    P(a| b, c)
    = P(a, d| b,c) / P(d| b,c)
    = (P(a| d,b,c) * P(d| b,c)) / P(d| b,c)
    = (P(a| d) * P(d| b,c)) / P(d| b,c)
    = P(a| d)                               Factors cancel out
    = busters.getObervationProbability(noisyDistance, trueDistance)

    where trueDistance is manhattan calculated using pacmanPosition and ghostposition
    """
    "*** YOUR CODE HERE ***"

    # ghost is in jail (logic in question)
    if ghostPosition == jailPosition:
        if noisyDistance == None:
            return 1
        else:
            return 0
    if noisyDistance == None:
        return 0

    #True Distance using manhattan
    pacmanToGhostDistance = util.manhattanDistance(pacmanPosition, ghostPosition) 
    # P(a| b, c) = sensorDistribution = P(a| d) as given in question (see above comment)
    sensorDistribution = busters.getObservationProbability(noisyDistance, pacmanToGhostDistance)

    return sensorDistribution



def observeUpdate(self, observation, gameState):
    """
    Update beliefs based on the distance observation and Pacman's position.

    The observation is the noisy Manhattan distance to the ghost you are
    tracking.

    self.allPositions is a list of the possible ghost positions, including
    the jail position. You should only consider positions that are in
    self.allPositions.

    The update model is not entirely stationary: it may depend on Pacman's
    current position. However, this is not a problem, as Pacman's current
    position is known.
    """
    "*** YOUR CODE HERE ***"
    for position in self.allPositions:
        # UPDATE POSITION:
        # belif is P(ghost at position) (given reading)
        # self.beliefs is DiscreteDistribution of belif!

        jailPosition = self.getJailPosition()
        pacmanPosition = gameState.getPacmanPosition()


        # P(hearing sounding with strength S (manhattanDist)) | pacmanPosition, ghostPosition)
        pObservation = self.getObservationProb(observation, pacmanPosition, position, jailPosition)
        # apply pObservation to each position in the distribution
        self.beliefs[position] *= pObservation

    self.beliefs.normalize()
    return


def elapseTime(self, gameState):
    """
    Predict beliefs in response to a time step passing from the current
    state.

    The transition model is not entirely stationary: it may depend on
    Pacman's current position. However, this is not a problem, as Pacman's
    current position is known.
    """
    "*** YOUR CODE HERE ***"

    newBeliefs = self.beliefs.copy() # copy to replace easier 
    newPosDists = {} # Stores new position distributions at key oldPosition for fast lookup

    # Populate newPosDists with a distribution for every position
    for oldPos in self.allPositions:    
        newPosDist = self.getPositionDistribution(gameState, oldPos)
        newPosDists[oldPos] = newPosDist

    # Each position should be updated
    for newPos in self.allPositions:
        # P(newPos) = sum over legal oldPos (P(oldPos) * (1/numLegaloldPos))

        # Optimization!?!?
        # for oldPos in self.allPositions: # not all positions are possible oldPosiitons though!
            # likelihood = newPosDists[oldPos][newPos]
            # newProb += self.beliefs[oldPos] * likelihood

        newProb = 0 # Keeps track of the sum over legal oldPos(possibleOldPos) for a given newPos
        possibleOldPositions = list(newPosDists[newPos].keys())
        for possibleOldPos in possibleOldPositions:
            likelihood = newPosDists[possibleOldPos][newPos] # Likelihood is P(newPos at t+1 | oldPos)
            newProb += self.beliefs[possibleOldPos] * likelihood # P(oldPos) * likelihood

        newBeliefs[newPos] = newProb
    
    # normalize(newBeliefs)
    self.beliefs = newBeliefs # update beliefs to reflect t+1 instead of t
    normalize(self.beliefs) # not sure if this is necessary, just feels like a good idea
