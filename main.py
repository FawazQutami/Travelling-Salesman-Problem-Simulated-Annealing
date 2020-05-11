"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Metaheuristics
-- File Name    :   main.py
-- *********************************************
"""

# load Packages
import argparse
import datetime as dt
import numpy as np
import subprocess
import sys

# load other packages
from eHandler import PrintException as EH
from SA_Plot import animateTSP, plotLearning
from SA import SimulatedAnnealing as sa

marks = '==' * 30 + '\n'


def install_required_Packages():
    """
    Install the required PACKAGES
    :return: Nothing
    """

    try:
        # List all the required packages
        required_packages = [
            'matplotlib',
            'basemap',
            'numpy',
        ]

        # Check and retrieve the installed packages info
        installed = subprocess.check_output(
            [
                sys.executable
                ,'-m'
                ,'pip'
                ,'freeze'
            ]
        )
        # Split and strip the returned info to get the
        # installed packages names list
        installed_packages = [r.decode().split('==')[0]
                              for r in installed.split()]
        # Loop over the required packages
        for package in required_packages:
            # If the package is not in the installed packages
            if package not in installed_packages:
                # print informative message
                print(marks)
                print("Installing {}! Please wait ...")
                print(marks)
                # Send a check call and install the package
                subprocess.check_call(
                    [
                        sys.executable
                        ,"-m"
                        ,"pip"
                        ,"install"
                        ,package
                    ]
                )

    except:EH()


def coordinates(fileName):
    """
    Coordinates
    :param fileName: string
    :return: list[int, float, float]
    """
    try:
        city, latitude, longitude = [], [], []
        with open(fileName, "r") as f:
            for line in f.readlines():
                line = [float(x.strip()) for x in line.split(" ")]
                city.append(int(line[0]))
                latitude.append(float(line[1]))
                longitude.append(float(line[2]))

            cities = np.column_stack((city, latitude, longitude))
        return cities

    except:
        EH()


def repeatSA(repetition, Nodes):
    """"""
    try:
        print("Starting Annealing ...")
        _results = []
        _totalExecutionTime =0
        # repeat Annealing few times and store the result:
        for i in range(1, repetition):
            start = dt.datetime.now()
            s = runAnnealing(Nodes)
            s.run()
            _results.append(s)
            end = dt.datetime.now()
            _totalExecutionTime += (end - start).seconds

        print(f'Total Execution Time in seconds: {_totalExecutionTime}')

        # Sort the resulted array:
        sortedList = sorted(_results, key=lambda sa: sa.bestFitness)

        # Rotate through the results and choose the best one:
        print("\n-- Resulted Fitness:")
        for i, s in enumerate(sortedList):
            print(f"Simulated Annealing {i+1}, best fitness is {s.bestFitness}")

        # Print the best fitness details
        print()
        bestAnnealing = sortedList[0]
        print("Best Solution: \n", bestAnnealing)

        # List of City Coordinates:
        _points = bestAnnealing.coordinates
        #print(f"City Coordinates :\n {_points}")

        # List of Best Solution Path:
        _solution = bestAnnealing.solutions
        #print(f"Best Solution:\n {_solution}")

        # List of Best Fitted Distances:
        _fitness = bestAnnealing.fitnessList
        #print(f"Best Fitness:\n {_fitness}")

        initFit, bestFit = bestAnnealing.greedyFitness, bestAnnealing.bestFitness

        return _solution, _points, _fitness, initFit, bestFit
    except :EH()


def runAnnealing(Nodes):
    try:
        # Run Annealing:
        s = sa(Nodes
               , initialTemperature=1e2
               , stoppingTemperature=1e-3
               , alpha=0.99999
               , stoppingIteration=500000)
        #s.run()

        return s

    except :EH()


def main():
    """ """
    try:
        print()
        print("1. Djibouti - 38 Cities.")
        print("2. Qatar - 194 Cities.\n")
        choice = int(input("Your choice? "))

        """
        Traveling salesman problem: is, given a set of cities, to find the shortest 
        path to visit all of the cities exactly once.
        """
        parser = argparse.ArgumentParser(description="Metaheuristics")

        fileList = ["data/dj38_tsp.txt", "data/qa194_tsp.txt"]
        regList = ["SA", "GA"]
        parser.add_argument("--filename"
                            ,choices=fileList
                            ,default=fileList[choice-1]
                            ,help='A string represents a dataset'
                            )

        args = parser.parse_args()

        # load and read data ----------------------------------------------------
        print("..." * 15)
        _Nodes = coordinates(args.filename)
        solutionObj, coordinatesObj, _fitnessObj, initFit, bestFit = repeatSA(6, _Nodes)

        # Visualize
        if choice == 1:
            animateTSP("Djibouti", solutionObj, coordinatesObj)
            plotLearning(_fitnessObj, initFit, bestFit)
        else:
            animateTSP("Qatar", solutionObj, coordinatesObj)
            plotLearning(_fitnessObj, initFit, bestFit)
    except:
        EH()


if __name__ == "__main__":
    try:
        # Install Required packages
        install_required_Packages()
        main()

    except:
        EH()
