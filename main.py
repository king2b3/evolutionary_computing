import argparse
import os

def parse_arguments(args=None) -> None:
    '''Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    '''
    parser = argparse.ArgumentParser(description='General genetic framework',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('population_size', 
            help='Initial size of the population.')
    parser.add_argument('individual_size', 
            help='Size of the genome of each individual.')
    parser.add_argument('individual_split', 
            help='Number of variables in the individual genome.')
    parser.add_argument('fitness', 
            help='Pick the fitness function type. Options: rosenbrock, max_ones')
    parser.add_argument('-cr','--cross_over_rate', default=0.5,
            help='Crossover rate. Options in range [0,1]')
    parser.add_argument('-mr','--mutation_rate', default=0.001,
            help='Mutation rate. Options in range [0,1]')
    parser.add_argument('-s','--selection', default='roulette',
            help='The type of selection function used. Options: random, roulette.')
    parser.add_argument('-k', default=1, 
            help='K-point crossover. Options in range [1:Genome Size - 1]')
    args = parser.parse_args(args=args)
    return args

def main(input_file, quiet=False, output_file='output', Print=False, name=False) -> None:
    '''Main function.

    FIX THIS FUNCTION

    Parameters
    ----------
    input_file: str:
        Path the input file.
    output_file: str
        Path to the output file. Default is 'output'
    quiet: bool
        Rather non-errors should be printed. Default is False
    Returns
    -------
    int
        The exit code.
    Raises
    ------
    FileNotFoundError
        Means that the input file was not found.
    '''
    from timer import Timer

    compiler_timer = Timer()
    
    # Error check if the file even exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError('File not found: {}'.format(input_file))
    
    if name:
        print('#######################')
        print(input_file)
        print('#######################')
    c = Compiler(input_file)
    s = Scanner(input_file,Print)
    compiler_timer.start_timer()
    s.scanFile()
    compiler_timer.end_timer()
    print(compiler_timer.__str__())

    return None


# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    import sys
    args = parse_arguments()
    try:
        main(**vars(args))
    except FileNotFoundError as exp:
        print(exp, file=sys.stderr)
        exit(-1)