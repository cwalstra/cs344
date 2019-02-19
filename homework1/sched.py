'''
Create a mini schedule for the CS department to use for access to SB354 and SB372
'''

from csp import CSP, min_conflicts, backtracking_search, AC3, parse_neighbors
from search import depth_first_graph_search

# Schedule Problem Class
def Schedule():
    Profs = 'dschuurman adams vnorman kvlinden'.split()
    Classes = 'cs108 cs112 cs212 cs214 cs300 cs344'.split()
    Times = 'mwf800 mwf900 mwf1030 mwf1130'.split()
    Rooms = 'sb354 sb372'.split()
    variables = Profs + Times + Rooms
    domains = {}
    for var in variables:
        domains[var] = Classes

    neighbors = parse_neighbors('dschuurman: ; adams: ; vnorman: ; kvlinden: ; '
                                'mwf800: ; mwf900: ; mwf1030: ; mwf1130: ; sb354: ; sb372: ', variables)
    for type in [Profs, Times, Rooms]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)
    print(neighbors)

    def schedule_constraints(A, a, B, b, recurse=0):
        same = (a == b)

        if recurse == 0:
            return schedule_constraints(B, b, A, a, 1)
        if ((A in Profs and B in Profs) or
                (A in Times and B in Times) or
                (A in Rooms and B in Rooms)):
            return not same
        raise Exception('error')
    return CSP(variables, domains, neighbors, schedule_constraints)


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for Class in 'cs108 cs112 cs212 cs214 cs300 cs344'.split():
        print('Class', Class)
        for (var, val) in result.items():
            if val == Class: print('\t', var)


puzzle = Schedule()

# result = depth_first_graph_search(puzzle)
# result = AC3(puzzle)
result = backtracking_search(puzzle)
# result = min_conflicts(puzzle, max_steps=1000)

if puzzle.goal_test(puzzle.infer_assignment()):
    print("Solution:\n")
    print_solution(result)
else:
    print("failed...")
    print(puzzle.curr_domains)
    puzzle.display(puzzle.infer_assignment())