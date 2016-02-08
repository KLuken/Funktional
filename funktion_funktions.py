from funktion_decorators import *
from typ import *

#@take_parameters(int, str)
@define_kind([Innt, Innt, Innt])
@define_class_constraint('Eq')
def addMe(*int):
    return sum(int)

@define_kind('(Bool Char)', '(Char Bool)')
def flip(tuple):
    return (tuple[0], tuple[2], tuple[1])

flip('Tupl(b Fals')

# print(addMe(3, 6))
# print(addMe._kind)