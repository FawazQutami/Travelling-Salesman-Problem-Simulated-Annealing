"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics - Simulated Annealing Algorithm 2 opt
-- File Name    :   SA.py
-- *********************************************
"""

# load Packages
import math
import random
import numpy as np
import datetime as dt

# load other packages
from eHandler import PrintException as EH


def distanceBetweenCities(coord1, coord2):
    """
    Distance between 2 cities
    :param coord1: list[floats]
    :param coord2: list[floats]
    :return: float
    """
    try:
        # print(coord1,coord2)
        return round(math.sqrt(math.pow(coord1[1] - coord2[1], 2)
                               + math.pow(coord1[2] - coord2[2], 2))
                     , 4)
    except:
        EH()


def getDistance(points):
    """
    Calculate distances between all cities
    :param points: list[float]
    :return: list[float]
    """
    try:
        distance = np.sqrt((np.square(points[ :, np.newaxis] - points).sum(axis=2)))
        # print(distance)
        return distance
    except:
        EH()


def greedySearchAlgorithm(d_List):
    """
    Greedy Search Algorithm
    :param d_List: list[float]
    :return: list [float]
    """
    try:
        # start from a random node
        initialNode = random.randrange(len(d_List))
        # set the solution list
        nearestNode = [initialNode]
        #print(initialNode)

        # Copy the Nodes list
        nextNodes = list(range(len(d_List)))
        # Remove the initial node from the new list
        nextNodes.remove(initialNode)
        #print(nextNodes)
        # Nearest Neighbour
        while nextNodes:
            # Choose the next node - pick min between 2 nodes
            nearestNeighbour = min([(d_List[initialNode][j], j) for j in nextNodes]
                                   , key=lambda x: x[0])
            # print(nearestNeighbour)
            initialNode = nearestNeighbour[1]
            # print(initialNode)
            nextNodes.remove(initialNode)
            nearestNode.append(initialNode)
        # print(nearestNode)
        return nearestNode

    except:
        EH()


class SimulatedAnnealing():
    """
    Simulated Annealing Algorithm
    """

    def __init__(self, coordinates
                 , initialTemperature=10
                 , alpha=0.999
                 , stoppingTemperature=1e-10
                 , stoppingIteration=1000):
        """

        :param coordinates: array
        :param initialTemperature: float
        :param alpha: float
        :param stopping_T: float
        :param stopping_iter: int
        """
        try:
            self.coordinates = coordinates
            self.sampleSize = len(coordinates)
            self.initialTemperature = initialTemperature
            self.T = initialTemperature
            self.alpha = alpha
            self.stoppingTemperature = stoppingTemperature
            self.stoppingIteration = stoppingIteration
            self.iteration = 1

            # Calculate distances
            self.arrayDistances = getDistance(coordinates)

            # Initiate Greedy Search:
            self.currentDistance = greedySearchAlgorithm(self.arrayDistances)
            # Set best distances:
            self.bestDistance = self.currentDistance
            # Set the solutions
            self.solutions = [self.currentDistance]

            # Initiate Greedy fitness:
            self.currentFitness = self.fitnessFunction(self.currentDistance)
            # Set initial Greedy fitness:
            self.greedyFitness = self.currentFitness

            # Initial Annealing best fitness:
            self.bestFitness = self.currentFitness
            # Save all fitness values in a list
            self.fitnessList = [self.bestFitness]
            # record the execution Time
            self.executionTime =0

        except:
            EH()

    def __repr__(self):
        try:
            improvement = round((self.greedyFitness - self.bestFitness)
                                / (self.greedyFitness), 3) * 100
            printStatement = (
                f"++++++++++++++++++++++++++++++++++++++++++++++++++"
                f"\n Initial Temperature                 : {self.T:.3f}"
                f"\n Learning Rate - Alpha               : {self.alpha}"
                f"\n Stopping Temperature                : {self.stoppingTemperature}"
                f"\n Stopping Iteration                  : {self.stoppingIteration:.3f}"
                f"\n Best Fitness - Greedy Search        : {self.greedyFitness:.3f} " 
                f"\n Best Fitness - Simulated Annealing  : {self.bestFitness:.3f}" 
                f"\n Annealing improvement over Greedy   : {improvement:.3f}%"
                f"\n Annealing Execution Time in seconds : {self.executionTime}"
                f"\n++++++++++++++++++++++++++++++++++++++++++++++++++")

            return printStatement

        except:
            EH()

    def fitnessFunction(self, solution):
        """
        Calculation of total distance of the current solution path.
        :param candidate: list[float]
        :return: float
        """
        try:
            current_fit = \
                round(
                    sum(
                        [self.arrayDistances[solution[i - 1]][solution[i]]
                         for i in range(1, self.sampleSize)])
                    + self.arrayDistances[solution[0]][solution[self.sampleSize - 1]]
                    , 4)
            return current_fit
        except:
            EH()

    def metropolis(self, candidate_fitness):
        """
        Metropolis:
        :param candidate_fitness: float
        :return: float
        """
        try:
            return math.exp(
                -abs(candidate_fitness - self.currentFitness) / self.initialTemperature)
        except:
            EH()

    def makeMove(self, candidate):
        """
        Acceptance of fitness
        :param candidate: list[float]
        :return: None
        """
        try:
            newFitness = self.fitnessFunction(candidate)

            if newFitness < self.currentFitness:
                # Accept candidate with probability 1 if new_fitness is better
                self.currentFitness = newFitness
                self.currentDistance = candidate
                if newFitness < self.bestFitness:
                    self.bestFitness = newFitness
                    self.bestDistance = candidate
            else:
                # Else: accept candidate with probability metropolis(..)
                if random.random() < self.metropolis(newFitness):
                    self.currentFitness = newFitness
                    self.currentDistance = candidate
        except:
            EH()

    def schedule(self):
        """
        Cooling strategy - Schedule of temperature
        :return: float
        """
        try:
             self.initialTemperature *= self.alpha
        except:
            EH()

    def run(self):
        """
        Execute Simulated Annealing Algorithm.
        :return:None
        """
        try:
            start = dt.datetime.now()
            # Monte Carlo at each temperature and iteration
            while self.initialTemperature >= self.stoppingTemperature \
                    and self.iteration < self.stoppingIteration:
                # List of candidates
                candidate = list(self.currentDistance)
                # select one city
                pos1 = random.randint(2, self.sampleSize - 1)
                # select another city, but not the same
                pos2 = random.randint(0, self.sampleSize - pos1)
                # Here we reverse a segment
                candidate[pos2: (pos2 + pos1)] = \
                    reversed(candidate[pos2: (pos2 + pos1)])
                # Make a move
                self.makeMove(candidate)
                # Change the initialTemperature:
                self.schedule()
                # Increase the iteration
                self.iteration += 1
                # Add the value the fitness list and solution list:
                self.fitnessList.append(self.bestFitness)
                self.solutions.append(self.bestDistance)

                end = dt.datetime.now()  # time.time()
                self.executionTime = (end - start).seconds
        except:
            EH()