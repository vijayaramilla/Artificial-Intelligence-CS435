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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Initialize the stateStack, path, and visited list
    nodeStack = util.Stack()
    visited = []
    pathList = []
    startNode = problem.getStartState()
    
    # If the maze only consists of a single square, there is no 
    #  action to take 
    if problem.isGoalState(startNode):
        return pathList
    
    # Push the start state onto the stack and mark it as visited
    nodeStack.push((startNode, pathList))
    visited += [startNode]

    # Perform a DFS, searching until the solution is found
	#  or there are no more nodes to check
    while not nodeStack.isEmpty():
        currNode, path = nodeStack.pop()

        # Get the node coordinate and action to take for each successor
        for successor in problem.getSuccessors(currNode):
            node = successor[0]
            action = successor[1]
            
            if not node in visited:
                visited += [node]
                
                if problem.isGoalState(node):
                    path += [action]
                    return path
                
                # Since the current node is not the solution, 
                #  push it onto the stack so that its successors
                #  can be checked
                nodeStack.push((node, path + [action]))

    # If there is somehow no solution or no agent to search the maze,
    #  just return an empty list
    return []
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Initialize the stateQueue, path, and visited list
    nodeQueue = util.Queue()
    visited = []
    pathList = []
    startNode = problem.getStartState()
    
    # If the maze only consists of a single square, there is no 
    #  action to take 
    if problem.isGoalState(startNode):
        return pathList
    
    # Push the start state into the queue and mark it as visited
    nodeQueue.push((startNode, pathList))
    visited += [startNode]

    # Perform a BFS, searching until the solution is found
	#  or there are no more nodes to check
    while not nodeQueue.isEmpty():
        currNode, path = nodeQueue.pop()

        # Get the node coordinate and action to take for each successor
        for successor in problem.getSuccessors(currNode):
            node = successor[0]
            action = successor[1]
            
            if not node in visited:
                visited += [node]
                
                if problem.isGoalState(node):
                    path += [action]
                    return path
                
                # Since the current node is not the solution, 
                #  push it into the queue so that its successors
                #  can be checked
                nodeQueue.push((node, path + [action]))

    # If there is somehow no solution or no agent to search the maze,
    #  just return an empty list
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    # Initialize the PriorityQueue, path, and visited list
    nodeQueue = util.PriorityQueue()
    visited = []
    pathList = []
    startNode = problem.getStartState()

    # If the maze only consists of a single square, there is no
    #  action to take
    if problem.isGoalState(startNode):
        return pathList

    # Push the start state into the queue and mark it as visited
    nodeQueue.push((startNode, pathList), nullHeuristic(startNode, pathList))
    visited += [startNode]

    # Perform a uniform search, searching until the solution is found
    while not nodeQueue.isEmpty():
        currNode, path = nodeQueue.pop()

        # Get the node coordinate and action to take for each successor
        for successor in problem.getSuccessors(currNode):
            node = successor[0]
            action = successor[1]
            
            if not node in visited:
                visited += [node]
                newPath = path + [action]
                
                if problem.isGoalState(node):
                    return newPath
                
                # Since the current node is not the solution, 
                #  push it into the queue so that its successors
                #  can be checked
                nodeQueue.push((node, newPath), problem.getCostOfActions(newPath))

    # If there is somehow no solution or no agent to search the maze,
    #  just return an empty list
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Initialize the PriorityQueue, path, and visited list
    nodeQueue = util.PriorityQueue()
    visited = []
    pathList = []
    startNode = problem.getStartState()

    # If the maze only consists of a single square, there is no
    #  action to take
    if problem.isGoalState(startNode):
        return pathList

    # Push the start state into the queue and mark it as visited
    nodeQueue.push((startNode, pathList), nullHeuristic(startNode, pathList))
    visited += [startNode]

    # Perform a uniform search, searching until the solution is found
    while not nodeQueue.isEmpty():
        currNode, path = nodeQueue.pop()

        # Get the node coordinate and action to take for each successor
        for successor in problem.getSuccessors(currNode):
            node = successor[0]
            action = successor[1]
            
            if not node in visited:
                visited += [node]
                newPath = path + [action]
                
                if problem.isGoalState(node):
                    return newPath
                
                # Calculate the priority cost, based on the inputted heuristic
                bwdCost = problem.getCostOfActions(newPath)
                fwdCost = heuristic(node, problem)
                priority = bwdCost + fwdCost
                
                # Since the current node is not the solution, 
                #  push it into the queue so that its successors
                #  can be checked
                nodeQueue.push((node, newPath), priority)

    # If there is somehow no solution or no agent to search the maze,
    #  just return an empty list
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
