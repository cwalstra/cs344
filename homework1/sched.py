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
    variables = Classes
    domains = {}
    for var in variables:
        domains[var] = []
        for Prof in Profs:
            for Time in Times:
                for Room in Rooms:
                    domains[var].append((Prof, Time, Room))
    neighbors = parse_neighbors('cs108: ; cs112: ; cs212: ; cs214: ; cs300: ; cs344: ', variables)
    for type in [Classes]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def schedule_constraints(A, a, B, b, recurse=0):
        same = (a == b)
        if A == B:
            return same
        if A != B:
            # if same professor
            if a[0] == b[0]:
                # if meeting at same time
                if a[1] == b[1]:
                    return False
                # No professor can teach consecutive classes
                elif a[1] == "mwf800" and b[1] == "mwf900":
                    return False
                elif b[1] == "mwf800" and a[1] == "mwf900":
                    return False
                elif a[1] == "mwf1030" and b[1] == "mwf900":
                    return False
                elif b[1] == "mwf1030" and a[1] == "mwf900":
                    return False
                elif a[1] == "mwf1030" and b[1] == "mwf1130":
                    return False
                elif b[1] == "mwf1030" and a[1] == "mwf1130":
                    return False
                else:
                    return True
            # if same time
            if a[1] == b[1]:
                # if classes have same professor or room
                if a[0] == b[0] or a[2] == b[2]:
                    return False
                else:
                    return True
            if a[2] == b[2]:
                if a[1] == b[1]:
                    return False
                else:
                    return True
            else:
                return True

        raise Exception('error')
    return CSP(variables, domains, neighbors, schedule_constraints)


def print_solution(result):
    """A CSP solution printer copied from csp.py."""
    for Class in 'cs108 cs112 cs212 cs214 cs300 cs344'.split():
        print('Class: ', Class)
        output = result[Class]
        print("Professor: ", output[0])
        print("Timeslot: ", output[1])
        print("Room: ", output[2])
        print("\n")


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