"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics - Simulated Annealing 1 opt
-- File Name    :   SA.py
-- *********************************************
"""

# load Packages
import numpy as np
import math
import random
import datetime as dt

# load other packages
from eHandler import PrintException as EH


class SimulatedAnnealing:
    """
    Simulated Annealing Class
    Metropolis Monte Carlo Algorithm.
    Heuristic methods for near-optimal solutions. “Iterative Improvements”
    """

    def __init__(self
                 ,func_name
                 ,Dimension
                 ,alpha=0.95
                 ,initialTemperature=10
                 ,stoppingTemperature=0
                 ,stoppingIteration=1000):
        """ initialize Simulated Annealing"""
        self.func_name = func_name
        self.xValues = np.linspace(-Dimension, Dimension, num=1000)
        self.interval = (-Dimension, Dimension)
        # print(self.xValues)
        self.alpha = alpha
        self.stoppingTemperature = stoppingTemperature
        self.stoppingIteration = stoppingIteration
        self.initialTemperature = initialTemperature
        self.T = initialTemperature
        self.initialEnergy = 0
        self.currentSolution = 0
        self.bestFitness = 0
        self.bestSolution = 0
        self.iteration = 1
        self.executionTime = 0
        self.fitness = []
        self.solutions = []

    def __repr__(self):
        return (
                f"\n ++++++++++++++++++++++++++++++++++++++++++++++++++"
                f"\n Initial Temperature                 : {self.T}"
                f"\n Learning Rate - Alpha               : {self.alpha}"
                f"\n Stopping Temperature                : {self.stoppingTemperature}"
                f"\n Stopping Iteration                  : {self.stoppingIteration}"
                f"\n Best Fitness                        : {self.bestFitness:.5f}" 
                f"\n Best Solution                       : {self.bestSolution:.5f}" 
                f"\n Annealing Execution Time in seconds : {self.executionTime}"
                f"\n ++++++++++++++++++++++++++++++++++++++++++++++++++")

    def run(self):

        try:
            start = dt.datetime.now()
            # Start with known configuration:
            # set a random number from the interval:
            self.currentSolution = np.random.choice(self.xValues)
            #self.solutions.append(self.currentSolution)
            # calculate the some noise (suggested by Robert and Casella):
            scale = np.sqrt(self.initialTemperature)
            self.initialEnergy = costFunction(self.func_name, len([self.currentSolution]), [self.currentSolution])
            #print([x], len([x]))
            #print(self.initialEnergy)
            # Monte Carlo at each temperature and iteration
            while self.initialTemperature >= self.stoppingTemperature \
                    and self.iteration < self.stoppingIteration:

                # Add small random displacement to x, to obtain a neighbouring vector( newX), then clip it
                # to ensure that it is within the interval:
                candidate = self.clip(self.currentSolution + np.random.normal() * scale)

                self.makeMove(candidate)
                # Change the initialTemperature:
                self.schedule()
                # Increase the iteration
                self.iteration += 1
                # Add the value to fitness list and solution list:
                self.fitness.append(self.bestFitness)
                self.solutions.append(self.bestSolution)

                end = dt.datetime.now()  # time.time()
                self.executionTime = (end - start).seconds

        except: EH()

    def makeMove(self, candidate):
        """
        Acceptance of fitness
        :param candidate: list[float]
        :return: None
        """
        try:
            newEnergy = costFunction(self.func_name, len([candidate]), [candidate])
            #print(candidate, len([candidate]))

            if newEnergy < self.initialEnergy:
                # Accept candidate with probability 1 if new_fitness is better
                self.initialEnergy = newEnergy
                self.currentSolution = candidate
                if newEnergy < self.bestFitness:
                    self.bestFitness = newEnergy
                    self.bestSolution = candidate
            else:
                # Else: accept candidate with probability metropolis(..)
                if random.random() < self.metropolis(newEnergy):
                    self.initialEnergy = newEnergy
                    self.currentSolution = candidate

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
                -abs(candidate_fitness - self.initialEnergy) / self.initialTemperature)
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

    def clip(self, x):
        """ Force x to be in the interval."""
        a, b = self.interval
        return max(min(x, b), a)
