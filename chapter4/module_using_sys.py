import sys
import os

from math import sqrt

print('The command line arguments are:')

for i in sys.argv:
    print(i)

print('the python path is ', sys.path,'\n')


print(os.getcwd())

print(sqrt(16))