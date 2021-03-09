# Principles and Practice of Evolutionary Computing (EECE 6046) - Bayley King
## HW Assignment Two
This assignment features the implementation of an Evolutionary Strategy from *Genetic Algorithms in Search, Optimization, and Machine Learning* by D.E.
Goldberg to solve the Himmelblau function.
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
The program main.py acts as the controller for the ES. main.py takes parameters as command lines arguments.

A possible command line call to do the default parameters for task 1

```python3 main.py 15 100 -f himmelblau -mg 1000 -cr .6 -mr .01 -s uniform -p mew_lambda```

A possible command line call to do the default parameters for task 3

```python3 main.py 100 100 -f himmelblau_task3 -mg 1000 -cr .6 -mr .01 -s uniform -p mew_lambda_bit_string -individual_size 16```


If you need help with the arguments, you can type ```python3 main.py -h``` which will display the help screen for the args parser, with the possible arguments for this system.
```
usage: main.py [-h] [-individual_size INDIVIDUAL_SIZE] [-is INDIVIDUAL_SPLIT] [-f FIT] [-mg MAX_GENS]
               [-cr CROSS_OVER_RATE] [-mr MUTATION_RATE] [-s SELECTION_TYPE] [-k K] [-p POP]
               mu_size lambda_size

General genetic framework

positional arguments:
  mu_size               Initial size of the population.
  lambda_size           Initial size of the population.

optional arguments:
  -h, --help            show this help message and exit
  -individual_size INDIVIDUAL_SIZE
                        Size of the genome of each individual. (default: 1)
  -is INDIVIDUAL_SPLIT, --individual_split INDIVIDUAL_SPLIT
                        Number of variables in the individual genome. (default: 1)
  -f FIT, --fit FIT     Pick the fitness function type. Options: rosenbrock, max_ones, himmelblau, himmelblau_task3
                        (default: max_ones)
  -mg MAX_GENS, --max_gens MAX_GENS
                        Maximum number of generations allowed (default: 2000)
  -cr CROSS_OVER_RATE, --cross_over_rate CROSS_OVER_RATE
                        Crossover rate. Options in range [0,1] (default: 0.5)
  -mr MUTATION_RATE, --mutation_rate MUTATION_RATE
                        Mutation rate. Options in range [0,1] (default: 0.001)
  -s SELECTION_TYPE, --selection_type SELECTION_TYPE
                        The type of selection function used. Options: random, uniform, roulette, tournament. (default:
                        roulette)
  -k K                  K-point crossover. Options in range [1:Genome Size - 1] (default: 1)
  -p POP, --pop POP     Population type. Options: fixed, mew_lambda, mew_lambda_bit_string (default: fixed)
  ```

___
## Files
- main.py
- - Controller for the file. Args are parsed in to control the evolution, no parameters are needed to be changed in this file. 
- task_1/
  - Results for the task 1 tests
- task_3/
  - Results for task 3
- average_performance.jpeg
  - plot of the average performance across the EA. this is auto generated
- best_performance.jpeg
  - plot of the best performance across the EA. this is auto generated
- euclidean_performance.jpeg
  - plot of the euclidean across the EA. this is auto generated
- src/
  - individual.py
    - Holds the abstract class for individual types. 
    - BitString and Floating Point types are possible
    - Crossover and mutation are methods to this class, as well as a method to generate a new individual.
  - population.py
    - Class structure for the population. Two versions of (mew , lambda) are included, mostly because I didn't allow for the two individual types for the problem scope easily in my code.
    - The fixed population is outdated, the (mew, lambda) classes can do the same where mew=lambda
  - selection.py
    - Holds the abstract class for selection. 
    - Roulette wheel, tournament, or uniform random are available
  - fitness.py
    - Holds the abstract class for fitness. 
    - There is a child class for both rosenbrock and max ones, and then two Himmelblau functions (one for floating point and one to translate the bit string into floating values)
___
## Comments
I couldn't find any parameters that found complete convergence across the full population for either task1 or task3. 
For task1, the ES would get close finding some of the minimum values of the function but wouldn't find any of the four minimas.
For task3, the CGA implementation from homework 1 would not converge to a full population of valid solutions, but it would find individuals that were valid solutions in the fixed population size. 

I think this could be due to the range available to the fixed binary encoding I had to use.
The fixed bit string for the CGA limited 3 floating points for the right hand side of the floating point number [0, .125, .25, .375, ... .875].
The ES approach has much more precision, not only due to the float type I used within python, but the range of values we could reach from using a Gaussian Mutation vs a bit flip mutation.
A mutation in the CGA for task 3 had a much different space than the ES did for task2.
This can be seen by looking at the average euclidean distances over time in the generated plots. 
For the ES, the euclidean distance converges along with the diversity of the population, but the space for the CGA never converges and there is a large variance in the euclidean distance.

The plots for each test are auto generated, I have placed my results in text files for you to view, but feel free to run any code you would like shown in the usage tab above.

For the ES, I went with a mutation strategy where the X and Y variables each had their own standard deviation variables (std_x std_y) which could be mutated in the same way the variables X and Y could be mutated.
These initial values for X and Y were picked uniformly through the max and min range of [-10  10] and the initial standard deviation values for x and y were equal to 1. 
This is the standard deviation values shown in the initial printed line of the evolution, titled in the homework write up as "mutation standard deviation".
The mutation rate is the chance that any of the given variables of an individual [x, y, std_x, std_y] could mutate.
It is possible for each variable to mutate for a given individual, but that chance would be mut_rate^4 which is quite small.


I was able to re-use lots of my code from the first assignment, this was my first time using abstract classes, but it has been great for creating variations on the EAs we have been testing.
___
## Contact
Reach out to me if there are any issues running the code, my email is `king2b3@mail.uc.edu`
