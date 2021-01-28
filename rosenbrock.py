import argparse
import os

def parse_arguments(
    args=None
) -> None:
    """Returns the parsed arguments.

    Parameters
    ----------
    args: List of strings to be parsed by argparse.
        The default None results in argparse using the values passed into
        sys.args.
    """
    parser = argparse.ArgumentParser(
            description="A default template for python",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("-o", "--output_file", help="Path to the output file.",
            default="output")
    parser.add_argument("-p", "--Print", help="Prints out EVERYTHING",
            default=False, action="store_true")
    parser.add_argument("-n", "--name", help="Prints file name",
            default=False, action="store_true")
    args = parser.parse_args(args=args)
    return args

def main(
    input_file, 
    quiet=False, output_file="output",
    Print=False, name=False
) -> None:
    """Main function.

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
    """
    #from timer import Timer

    compiler_timer = Timer()
    
    # Error check if the file even exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError("File not found: {}".format(input_file))
    
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