# Principles and Practice of Evolutionary Computing (EECE 6046)
## HW Assignment One
This assignment features the implementation of a Canonical Genetic Algorithm (CGA) from *Genetic Algorithms in Search, Optimization, and Machine Learning* by D.E.
Goldberg.
---
## Usage
The program main.py acts as the controller for teh CGA. main.py takes parameters as command lines arguments.

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
A possible command line call to do the default parameters for part two would 

```python3 main.py 100 32 -mr 0.01 -cr 0.5 -mg 4000 -f max_ones```

The commands used for the submitted Rosenbrock results are 

```python3 main.py 100 10 -mr 0.001 -cr 0.3 -mg 4000 -is 2 -f rosenbrock```

Notice the inclusion of `-is 2` in this class, this lets the system know that two variables are taken from the bitstring.
___
## Files
- LICENSE
- main.py
- - Controller for the file. Args are parsed in to control the evolution
- max_ones.txt
- - Piped results for the Max_Ones problem with the given parameters
- rosenbrock.txt
- - Piped results for the Rosenbrock problem
- individual.py
- - Holds the abstract class for individual types. Bitstring type is the only type at the moment.
- population.py
- selection.py
- - Holds the abstract class for selection. Roulette wheel is the only selection type at the moment.
  
---
## Development
The system uses Python 3.8.5, with no outside libraries. The only libraries called in the programs are
- ABC - Library to allow the use of abstract classes within python
- OS - I use this to clear the terminal screen before the start of a program
- Math - To use the ceiling function
- Random - To call pseudo random numbers for various stochastic functions