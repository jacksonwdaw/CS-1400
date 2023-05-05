import subprocess
import tempfile
import textwrap
import traceback
import sys
import random
from math import sqrt
from pprint import pprint
from statistics import stdev
import turtle as turtle
t = turtle.Turtle()
turtle.tracer(0,0)


def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        t.getcanvas().postscript(file=tmp.name)
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
        except Exception as exp:
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
                # pylint: disable=E1120
                traceback.print_exception(exp)
            # python version < 3.10
            else:
                traceback.print_exception(None, exp, None)


    
def walk(walk_length, direction):
    walk_path = [[0,0]] # -> [[0,0],[0,0]]
    for i in range(walk_length):
        step = walk_path[-1].copy()
        choice = random.choice(list(direction.keys()))
        step[direction[choice][0]] = step[direction[choice][0]] + direction[choice][1]
        walk_path.append(step)
    return walk_path

def simulate(walk_lengths, num_trials, walker_type):
    walker_trial = {'Pa':{
                        'shape':'circle',
                        'color':'black'
                        },
                    'Mi-Ma':{
                        'shape':'square',
                        'color':'green'
                        },
                    'Reg':{
                        'shape':'triangle',
                        'color':'red'
                        }
                    }
    if walker_type == 'Pa' or walker_type == "all":
        direction = {'North':[1,1],'South':[1,-1],'East':[0,1],'West':[0,-1]}
        path_distances = []
        for walk_length in walk_lengths:
            walker_trial["Pa"][str(walk_length)] = {
                "paths":[],
                'statistics':{
                    'Mean':0,
                    'Max':0,
                    "Min":0,
                    "CV":0
                }
            }
            for i in range(num_trials):
                path = walk(walk_length,direction)
                path_distances.append(find_distance(path[-1]))
                walker_trial['Pa'][str(walk_length)]["paths"].append(path)
            walker_trial["Pa"][str(walk_length)]["statistics"]['Mean'] = find_avg(path_distances)
            walker_trial["Pa"][str(walk_length)]["statistics"]['CV'] = find_cv(path_distances)
            walker_trial["Pa"][str(walk_length)]["statistics"]['Max'] = find_max(path_distances)
            walker_trial["Pa"][str(walk_length)]["statistics"]['Min'] = find_min(path_distances)


    if walker_type == 'Mi-Ma' or walker_type == "all":
        direction = {'North':[1,1],'South':[1,-1],'East':[0,1],'West':[0,-1],'South_2':[1,-1]}
        path_distances = []
        for walk_length in walk_lengths:
            walker_trial["Mi-Ma"][str(walk_length)] = {
                "paths":[],
                'statistics':{
                    'Mean':0,
                    'Max':0,
                    "Min":0,
                    "CV":0
                }
            }
            for i in range(num_trials):
                path = walk(walk_length,direction)
                path_distances.append(find_distance(path[-1]))
                walker_trial['Mi-Ma'][str(walk_length)]["paths"].append(path)
            walker_trial["Mi-Ma"][str(walk_length)]["statistics"]['Mean'] = find_avg(path_distances)
            walker_trial["Mi-Ma"][str(walk_length)]["statistics"]['CV'] = find_cv(path_distances)
            walker_trial["Mi-Ma"][str(walk_length)]["statistics"]['Max'] = find_max(path_distances)
            walker_trial["Mi-Ma"][str(walk_length)]["statistics"]['Min'] = find_min(path_distances)
    

    if walker_type == 'Reg' or walker_type == "all":
        direction = {'East':[0,1],'West':[0,-1]}
        path_distances = []
        for walk_length in walk_lengths:
            walker_trial["Reg"][str(walk_length)] = {
                "paths":[],
                'statistics':{
                    'Mean':0,
                    'Max':0,
                    "Min":0,
                    "CV":0
                }
            }
            for i in range(num_trials):
                path = walk(walk_length,direction)
                path_distances.append(find_distance(path[-1]))
                walker_trial['Reg'][str(walk_length)]["paths"].append(path)
            walker_trial["Reg"][str(walk_length)]["statistics"]['Mean'] = find_avg(path_distances)
            walker_trial["Reg"][str(walk_length)]["statistics"]['CV'] = find_cv(path_distances)
            walker_trial["Reg"][str(walk_length)]["statistics"]['Max'] = find_max(path_distances)
            walker_trial["Reg"][str(walk_length)]["statistics"]['Min'] = find_min(path_distances)
    trial_output(walker_trial)
    return walker_trial

def trial_output(walker_trial):
    for walker,walker_data in walker_trial.items():
        for trial,trial_data in walker_data.items():
            print(f"{walker} random walk of {trial} steps")
            print(f"Mean = {trial_data['statistics']['Mean']:.1f} CV = {trial_data['statistics']['CV']:.1f}")
            print(f"Max = {trial_data['statistics']['Max']:.1f} Min = {trial_data['statistics']['Min']:.1f}")

def find_cv(distances):
    return stdev(distances)/find_avg(distances)

def find_min(distances):
    return min(distances)

def find_max(distances):
    return max(distances)

def find_avg(distances):
    average = sum(distances) / len(distances)
    return average
    
def find_distance(coords):
    return sqrt(coords[0]**2 + coords[1]**2)

def stamps(end_coords):
    for coord in end_coords:
        t.setpos(coord[0]*5,coord[1]*5)
        t.stamp()

def plot():
    t.screen.screensize(300,400)
    #t.screensize(300,400)
    t.speed(0)
    t.pencolor("black")
    args = sys.argv[1:]
    args = ['100','50','all']
    if len(args) != 3:
        print("Usage: python3 random_walk.py walk_lengths num_trials walker_type")
        return
    walk_lengths = [int(x) for x in args[0].split(',')]
    num_trials = int(args[1])
    walker_type = args[2]
    walks = simulate(walk_lengths, num_trials, walker_type)
    t.penup()
    t.shapesize(.5,.5,.5)
    
    for walker in walks.keys():
        end_coords = [x[-1] for x in walks[walker]['100']['paths']]
        t.shape(walks[walker]['shape'])
        t.color(walks[walker]['color'])
        stamps(end_coords)
    turtle.update()
    #save_to_image(dest='random_walk.png')
    turtle.done()


def main():

    args = sys.argv[1:]
    args = ['5,6','3','all']
    if len(args) != 3:
        print("Usage: python3 random_walk.py walk_lengths num_trials walker_type")
        return
    walk_lengths = [int(x) for x in args[0].split(',')]
    num_trials = int(args[1])
    walker_type = args[2]
    simulate(walk_lengths, num_trials, walker_type)
    plot()
t.stampItems
if __name__ == '__main__':
    main()