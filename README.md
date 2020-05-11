# Travelling Salesman Problem - TSP:
“Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?”
I have chosen Simulated Annealing Algorithm to solve the TSP, because it has some parameters in which I can tweak to reach a reasonable solution - the goal of simulated annealing is to minimize the energy of a system (minimizing a cost function). 

# Simulated Annealing Algorithm in brief:
	1. Start from an initial solution, then at each iteration we generate a slightly different solution. 
	2. If the iteration is better, then we accept it. Otherwise, we accept it with a probability of metropolis.
	3. We repeat the iteration process until a stopping criterion is reached.
		Let s = s0
		For k = 0 through kmax (exclusive):
		T ? temperature( (k+1)/kmax )
		Pick a random neighbour, snew ? neighbour(s)
		If P(E(s), E(snew), T) = random(0, 1):
				 s ? snew
		Output: the final state s
		from: https://en.wikipedia.org/wiki/Simulated_annealing
		
# Parameters that I have used in this simulation are:
	1. Initial Temperature: starting temperature 
	2. Stopping Temperature: min value of the temperature where to stop
	3. Alpha - a: it is the learning rate (ranges between 0 and 1)
	4. Stopping Iteration: max iteration 
	
Something worth mentioning is that we decrease the temperature at each iteration, by multiplying the temperature by a rate (known as Cooling Schedule).
Also, in the case of decreasing the learning rate, one should consider reducing the initial and stopping temperature, as well as stopping iteration, to fine-tune the result.

# Study cases: 
In our case I used “Djibouti - 38 Cities” and “Qatar - 194 Cities” from http://www.math.uwaterloo.ca/tsp/world/countries.html
In both cases, I have repeated the simulated annealing 5 times to produce the best solution by using the same parameters at each repetition. The best solution and fitness generated was:
	
	1. Djibouti - 38 Cities:

The best solution is (6660.8366) KM for the TSP journey with a total execution time - for 5 repetitions, equals to 0 seconds.
	.............................................
	Starting Annealing ...
	Total Execution Time in seconds: 0

	-- Resulted Fitness:
	Simulated Annealing 1, best fitness is 6660.8366
	Simulated Annealing 2, best fitness is 6973.0018
	Simulated Annealing 3, best fitness is 7133.8403
	Simulated Annealing 4, best fitness is 7179.9864
	Simulated Annealing 5, best fitness is 7249.409

	Best Solution: 
	 ++++++++++++++++++++++++++++++++++++++++++++++++++
	 Initial Temperature                 : 1000.000
	 Learning Rate - Alpha               : 0.999
	 Stopping Temperature                : 1e-05
	 Stopping Iteration                  : 500000.000
	 Best Fitness - Greedy Search        : 8167.403 
	 Best Fitness - Simulated Annealing  : 6660.837
	 Annealing improvement over Greedy   : 18.400%
	 Annealing Execution Time in seconds : 0
	++++++++++++++++++++++++++++++++++++++++++++++++++


	2. Qatar - 194 Cities:
In this case, I have tweaked the learning rate (a) and both initial and stopping temperatures, hence the best solution is (9832.537) KM for the TSP journey with a total execution time - for 5 repetitions, equals to 244 seconds.
	.............................................
	Starting Annealing ...
	Total Execution Time in seconds: 244

	-- Resulted Fitness:
	Simulated Annealing 1, best fitness is 9832.5367
	Simulated Annealing 2, best fitness is 9888.1638
	Simulated Annealing 3, best fitness is 9980.0555
	Simulated Annealing 4, best fitness is 10001.9822
	Simulated Annealing 5, best fitness is 10162.5029

	Best Solution: 
	 ++++++++++++++++++++++++++++++++++++++++++++++++++
	 Initial Temperature                 : 100.000
	 Learning Rate - Alpha               : 0.99999
	 Stopping Temperature                : 0.001
	 Stopping Iteration                  : 500000.000
	 Best Fitness - Greedy Search        : 11559.790 
	 Best Fitness - Simulated Annealing  : 9832.537
	 Annealing improvement over Greedy   : 14.900%
	 Annealing Execution Time in seconds : 49
	++++++++++++++++++++++++++++++++++++++++++++++++++
