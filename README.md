# Principles and Practice of Evolutionary Computing (EECE 6046) - Bayley King
## HW Assignment One
This assignment features the implementation of a Canonical Genetic Algorithm (CGA) from *Genetic Algorithms in Search, Optimization, and Machine Learning* by D.E.
Goldberg.
___
## Development
The system uses Python 3.8.5, with **ONE** outside library used for printing purposes only. 
- Tabulate

Tabulate can be installed with the command

```pip3 install tabulate```

The base-python libraries used in the programs are
- ABC - Library to allow the use of abstract classes within python
- OS - I use this to clear the terminal screen before the start of a program
- Math - To use the ceiling function
- Random - To call pseudo random numbers for various stochastic functions
- Collections - Allows to set a default result for a dictionary call. Its basically is a cleaner way to do a try except if the key isn't in the dictionary 
___
## Usage
The program main.py acts as the controller for the CGA. main.py takes parameters as command lines arguments.

A possible command line call to do the default parameters for part two would 

```python3 main.py 100 32 -mr 0.01 -cr 0.5 -mg 4000 -f max_ones```

The commands used for the submitted Rosenbrock results are 

```python3 main.py 100 10 -mr 0.001 -cr 0.3 -mg 4000 -is 2 -f rosenbrock```

If you need help with the arguments, you can type ```python3 main.py -h``` which will display the help screen for the args parser, with the possible arguments for this system.
```
usage: main.py [-h] [-is INDIVIDUAL_SPLIT] [-f FIT] [-mg MAX_GENS] [-cr CROSS_OVER_RATE] [-mr MUTATION_RATE]
               [-s SELECTION] [-k K]
               population_size individual_size

General genetic framework

positional arguments:
  population_size       Initial size of the population.
  individual_size       Size of the genome of each individual.

optional arguments:
  -h, --help            show this help message and exit
  -is INDIVIDUAL_SPLIT, --individual_split INDIVIDUAL_SPLIT
                        Number of variables in the individual genome. (default: 1)
  -f FIT, --fit FIT     Pick the fitness function type. Options: rosenbrock, max_ones (default: max_ones)
  -mg MAX_GENS, --max_gens MAX_GENS
                        Maximum number of generations allowed (default: 2000)
  -cr CROSS_OVER_RATE, --cross_over_rate CROSS_OVER_RATE
                        Crossover rate. Options in range [0,1] (default: 0.5)
  -mr MUTATION_RATE, --mutation_rate MUTATION_RATE
                        Mutation rate. Options in range [0,1] (default: 0.001)
  -s SELECTION, --selection SELECTION
                        The type of selection function used. Options: random, roulette. (default: roulette)
  -k K                  K-point crossover. Options in range [1:Genome Size - 1] (default: 1)
  ```

Notice the inclusion of `-is 2` for the rosenbrock problem, this lets the system know that two variables are taken from the bitstring. I didn't want to hard code this, just in case we use this network again for other multivariable cases.
___
## Files
- main.py
- - Controller for the file. Args are parsed in to control the evolution, no parameters are needed to be changed in this file. 
- max_ones.txt
- - Piped results for the Max_Ones problem with the given parameters
- rosenbrock.txt
- - Piped results for the Rosenbrock problem
- individual.py
- - Holds the abstract class for individual types. Bitstring type is the only type at the moment. Crossover and mutation are methods to this class, as well as a method to generate a new individual.
- population.py
- - Class structure for the population. Holds some methods, like generating a population and returning statistics.
- selection.py
- - Holds the abstract class for selection. Roulette wheel is the only selection type at the moment. New selection types can be created here as child classes.
- fitness.py
- - Holds the abstract class for fitness. There is a child class for both rosenbrock and max ones. I chose this was so that I could add a new class for whatever fitness function we want to test
___
## Comments
I wasn't able to get the network to complete the max_ones problem with the given parameters, but if I decreased the bit length it would work with the set parameters. The population converges on a single individual very fast, between 5 and 10 generations, which I think could be due to the high crossover rate and low mutation rate, but I think the selection function plays a bigger role in this. 

The roulette wheel seemed to force the convergence pretty quickly, I added a tournament selection function just to test my hypothesis and the results didn't improve. In fact, the population converged even quicker for both low and high K values. 

This leads me to believe that either the given parameters can't allow for proper convergence, or there is something else in my code causing this improper convergence.

I didn't have tons of issues with the Rosenbrock function, expect when I went higher than a bit size of 12 (giving a range of -7.5 to 7.5). I tried using IEEE 745 for the floating point representation, but soon found that was too large of a range of values. A fixed point system was much better, and allowed for convergence.
___
## Contact
Reach out to me if there are any issues running the code, my email is `king2b3@mail.uc.edu`
