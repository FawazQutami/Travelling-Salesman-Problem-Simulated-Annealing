"""
-- *********************************************
-- Author       :	Fawaz Qutami
-- Create date  :   10th May 2020
-- Description  :   Plotting Functions
-- File Name    :   SA_Plot.py
-- *********************************************
"""

# load Packages
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap

# load other packages
from eHandler import PrintException as EH


def plotLearning(fitnessList, initFit, bestFit):
    """

    :param fitnessList: list[float]
    :param initFit: float
    :param bestFit: float
    :return: None
    """
    try:
        plt.figure(figsize=(10, 5))
        plt.grid('on')
        plt.rc('axes', axisbelow=True)
        plt.plot([i for i in range(len(fitnessList))]
                 , fitnessList)
        line_init = plt.axhline(y=initFit
                                , color='r'
                                , linestyle='--')
        line_min = plt.axhline(y=bestFit
                               , color='g'
                               , linestyle='--')

        plt.legend([line_init, line_min]
                   , ['Greedy Initial Fitness', 'Optimized Annealing Fitness'])
        plt.ylabel('Distance')
        plt.xlabel('Iteration')
        plt.show()

    except :EH()


def animateTSP(country, history, points):
    """

    :param country: string
    :param history: list[int, float, float]
    :param points: list[int, float, float]
    :return:
    """
    try:
        # Prepare the coordinates for plotting the trip
        cityName = []
        latitude = []
        longitude = []
        for city in points:
            cityName.append(city[0])
            latitude.append(city[1]/1000.)
            longitude.append(city[2]/1000.)
        cityName.append(cityName[0])
        latitude.append(latitude[0])
        longitude.append(longitude[0])

        plt.figure(figsize=(7, 7))

        # Specify tripMap width and height
        if country == "Djibouti":
            tripMap = Basemap(width=350000
                              , height=270000
                              , resolution='i'
                              , projection='tmerc'
                              , lat_0=11.572076
                              , lon_0=43.145645
                              )
        else:
            tripMap = Basemap(width=250000
                              , height=250000
                              , resolution='i'
                              , projection='tmerc'
                              , lat_0=25.286106
                              , lon_0=51.534817
                              )

        tripMap.drawmapboundary(fill_color = 'aqua')
        tripMap.fillcontinents(color = '#FFE4B5', lake_color = 'aqua')
        tripMap.drawcoastlines()
        tripMap.drawcountries()

        # Range the frames
        _frames = len(history) // 1500
        _frameRange = range(0, len(history), _frames)

        # Path is represented as line
        line = tripMap.plot([], []
                        ,'D-'
                        ,markersize=3
                        ,linewidth=1
                        ,color='r')[0]
        # initial function
        def init_func():
            # Draw node dots on graph
            x = [longitude[i] for i in history[0]]
            y = [latitude[i] for i in history[0]]
            x, y = tripMap(x, y)
            tripMap.plot(x, y, 'bo', markersize=3)

            # Empty initialization
            line.set_data([], [])

            return line,
        # animate function
        def gen_function(frame):
            # Update the graph for each frame
            x = [longitude[i] for i in history[frame] + [history[frame][0]]]
            y = [latitude[i] for i in history[frame] + [history[frame][0]]]
            x, y = tripMap(x, y)
            line.set_data(x, y)

            return line

        # Animate the graph
        _animation = FuncAnimation(plt.gcf()
                                   , func=gen_function
                                   , frames=_frameRange
                                   , init_func=init_func
                                   , interval=10
                                   , repeat=False)
        plt.show()

    except:
        EH()