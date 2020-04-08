import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('--file',
                    help='File to save to',
                    action='store',
                    dest='file',
                    type=str,
                    required=True,
                    metavar='FILE')
parser.add_argument('--calculate',
                    type=int,
                    required=True,
                    metavar='N')
args = parser.parse_args()

def fib(n, p=False):
    x = 0
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fib(n-1, p) + fib(n-2)
    if p:
        p.write(str(x) + "\n")
    return x

#Check to see if the file exists
if os.path.isfile(args.file):
        message = input("File already exists, would you like to overwrite? Y or N? ")
        if len(message) <=0 or message[0] not in ['Y', 'y']:
            exit()

with open(args.file, 'w') as file:
    fib(args.calculate, file)
    
    
