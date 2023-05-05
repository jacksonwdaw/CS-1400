'''
A runner for the turtle project.
'''

import argparse
import Turtle_2_Project as doodles
import subprocess
import sys
import tempfile
import textwrap
import traceback
import turtle
'''lol'''
def save_to_image(dest='doodle.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='doodle',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        command = ['gs',
                   '-dSAFER',
                   '-o',
                   dest,
                   '-r200',
                   '-dEPSCrop',
                   '-sDEVICE=png16m',
                   tmp.name]
        try:
            subprocess.run(command,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           check=True)
        except Exception as e:
            message = f'''\
            There was an error running ghostscript.

            If you are seeing this error in Codio, please report it to your instructor.
            If you are seeing this error elsewhere, consider installing ghostscript or
            replacing the call to `save_to_image()' with `turtle.done()' in your local
            copy. Be sure not to change run_doodles.py in Codio!

            The system was attempting to run the following command:
            {' '.join(command)}

            Error details:
            '''
            print(textwrap.dedent(message), file=sys.stderr)
            [_, minor, _] = sys.version.split()[0].split('.')
            minor = int(minor)
            # python version >= 3.10
            if minor >= 10:
                traceback.print_exception(e)
            # python version < 3.10
            else:
                traceback.print_exception(None, e, None)


def main():
    parser = argparse.ArgumentParser(
        prog = 'Turtle Patterns II',
        description = 'A driver for the Turtle Patterns II project'
    )
    parser.add_argument('-s', '--save',
                        action='store_true',
                        help='Save the image (requires GhostScript)')
    parser.add_argument('-o', '--open',
                        action='store_true',
                        help='Keep the image open when done')
    parser.add_argument('arguments',
                        metavar='A',
                        type=str,
                        nargs='+',
                        help='One or more arguments to change your drawing')
    args = parser.parse_args()
    doodles.draw(args.arguments)
    if args.save:
        save_to_image()
    if args.open:
        turtle.done()


if __name__ == '__main__':
    main()
