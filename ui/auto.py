from scripts.constants import TERMINAL_FG_YELLOW, TERMINAL_RESET

# This function displays an error in the automatic learning screen if the user enters anything other than a number or "exit".
def displayInputNotANumberError():
    print('''
| Error: Input is not a number!
| Please enter a number within the specified range.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays an error in the automatic learning screen if the user enters a number that is out of range.
def displayInputOutOfRangeError():
    print('''
| Error: Input is out of range!
| Please enter a number within the specified range.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the automatic learning screen.
def displayMainScreen():
    print('''
+====================+
| Automatic Learning |
+====================+

| How many matches do you want to simulate?
| You can enter a number from {0}1{1} to {0}999{1}.
| You can also enter "{0}Exit{1}" to return to the title screen.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the simulation progress. 
def displaySimulationProgress(battlesCompleted, progress):
    print("| Matches Completed: {0} ({1}% Done)".format(battlesCompleted, progress),end="\r")

# This function displays the first part of the simulation screen.
def displaySimulationScreen1(choice):
    print('''
+====================+
| Automatic Learning |
+====================+

| {0} matches are currently being simulated.
| Please wait while the AIs are playing...
'''.format(choice))

# This function displays the second part of the simulation screen.
def displaySimulationScreen2(choice):
    print('''| Matches Completed: {0} (100% Done)
'''.format(choice))

# This function displays the third part of the simulation screen.
def displaySimulationScreen3():
    print('''| The simulated matches have been completed.
          
| Press {0}Enter{1} to return to the automatic learning screen.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))