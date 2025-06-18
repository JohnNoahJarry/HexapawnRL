from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_FG_YELLOW, TERMINAL_RESET

# This function displays the title screen.
def displayMainScreen():
    print('''
+===================+
| HexapawnRL v1.0.0 |
+===================+

[{0}1{1}] Play as {2}P1{1}
[{0}2{1}] Play as {3}P2{1}
[{0}3{1}] Spectate AI Match
[{0}4{1}] Auto-learning
[{0}5{1}] View AI Memory Gallery
[{0}6{1}] Settings
[{0}7{1}] Exit
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET, TERMINAL_FG_BLUE, TERMINAL_FG_RED))