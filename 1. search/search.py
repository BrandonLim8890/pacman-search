# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from typing import Set
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    explored = set()
    frontier = util.Stack()
    start_node = (problem.getStartState(), [])
    frontier.push(start_node)

    while not frontier.isEmpty():
        curState = frontier.pop()
        explored.add(curState[0])
        if problem.isGoalState(curState[0]):
            return curState[1]
        
        for loc, dir, cost in problem.getSuccessors(curState[0]):
            if loc in explored:
                continue
            frontier.push((loc, curState[1] + [dir]))
        
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    explored = set()
    frontier = util.Queue()
    start_node = (problem.getStartState(), [])
    frontier.push(start_node)
    explored.add(problem.getStartState())

    while not frontier.isEmpty():
        curState = frontier.pop()
        if problem.isGoalState(curState[0]):
            return curState[1]

        for loc, dir, cost in problem.getSuccessors(curState[0]):
            if loc in explored:
                continue
            explored.add(loc)
            frontier.push((loc, curState[1] + [dir]))
    
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    explored = set()
    frontier = util.PriorityQueue()
    start_node = (problem.getStartState(), [], 0)
    frontier.push(start_node, 0)

    while not frontier.isEmpty():
        # 0 index is pos, 1 is path, 2 is the cost
        curState = frontier.pop()
        if problem.isGoalState(curState[0]):
            return curState[1]

        if curState[0] not in explored:
            explored.add(curState[0])
            for loc, dir, cost in problem.getSuccessors(curState[0]):
                frontier.update((loc, curState[1] + [dir], cost + curState[2]), curState[2] + cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    explored = set()
    frontier = util.PriorityQueue()
    startNode = (problem.getStartState(), [], 0)
    frontier.push(startNode, 0 + heuristic(problem.getStartState(), problem))
    
    while not frontier.isEmpty():
        # 0 index is pos, 1 is path, 2 is the cost to get here so far
        curState = frontier.pop()
        if problem.isGoalState(curState[0]):
            return curState[1]
        
        if curState[0] not in explored:
            explored.add(curState[0])
            for loc, dir, cost in problem.getSuccessors(curState[0]):
                frontier.update((loc, curState[1] + [dir], cost + curState[2]), curState[2] + cost + heuristic(loc, problem))



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
