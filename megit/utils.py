import sys
import os

"""Function list:
    mk_outdir(out_dir, err_msg='Invalid output directory!'): Create an output directory for data.
    prog_print(iteration, total, prefix=str(), suffix=str()): Create a terminal progress bar for a loop.
"""


def mk_outdir(out_dir, err_msg='Invalid output directory!'):
    """Create an output directory for data.

    Args:
        out_dir (str): Output directory
        err_msg (str): Error message when creation error happens

    Returns:
        str: Created output directory
    """
    if not os.path.isdir(out_dir):    # Check if folder exists
        try:
            os.mkdir(out_dir)
        except OSError:
            print(err_msg)
            exit(-1)
    return out_dir


def prog_print(iteration, total, prefix=str(), suffix=str()):
    """Create a terminal progress bar for a loop.

    Args:
        iteration (int): Current iteration
        total (int): Total iterations
        prefix (str): Prefix string of progress bar (default: str())
        suffix (str): Suffix string of progress bar (default: str())

    Returns:
    """
    # Basic settings
    decimals = 2  # Decimals in percent completed
    length = 50  # Character length of bar
    fill = '>'  # Bar fill character
    # Create percentage bar
    iteration += 1
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / total))
    filled = int(length * iteration // total)
    bar = fill * filled + '-' * (length - filled)
    # Print session
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    if iteration == total:  # Print a new line at 100%
        print('')
