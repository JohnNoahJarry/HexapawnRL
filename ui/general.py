from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_FG_YELLOW, TERMINAL_FGBG_BLACK, TERMINAL_RESET
import os

# This function sends a command to the terminal to clear the screen. 
# This works for most terminals on most operating systems.
def clearScreen():
    os.system("cls||clear")

# This function calls the AIs to display their level differences before and after a match or set of matches.
def displayAILevelDifferences(player1AILevelDifference, player2AILevelDifference):
    if player1AILevelDifference != "":
        print(player1AILevelDifference)
    
    if player2AILevelDifference != "":
        print(player2AILevelDifference)
    
    if player1AILevelDifference != "" or player2AILevelDifference != "":
        print()

# This function calls the AIs to display their stats in proper order of the Player 1 AI first.
def displayAIStats(AI1, AI2):
    if AI1.getIsPlayer1():
        print(AI1.getStatDisplay())
        print(AI2.getStatDisplay())
    else:
        print(AI2.getStatDisplay())
        print(AI1.getStatDisplay())

# This function displays a dynamic header that changes length depending on the provided string.
# This function accounts for exactly one instance of a color and reset terminal escape sequence.
def displayDynamicHeaderWithColor(headerText):
    print('''
+={0}=+
| {1} |
+={0}=+
'''.format("="*(len(headerText)-9), headerText))

# This function displays an error in any screen with a number menu if the user enters anything that is not a number in the number list.
def displayNumberMenuInvalidInputError():
    print('''
| Error: Invalid Input!
| Please enter one of the numbers in brackets.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the provided position.
def displayPosition(position):
    print('''
   +---+---+---+''')

    columnNumber = 3
    output = ""
    for i in range(9):
        if i%3 == 0:
            output = " {0} |".format(columnNumber)
            columnNumber -= 1
        
        tileOutput = ""
        if position[i] == "o":
            tileOutput = "{0}O".format(TERMINAL_FG_RED)
        elif position[i] == "-":
            tileOutput = " "
        elif position[i] == "O":
            tileOutput = "{0}O".format(TERMINAL_FG_BLUE)

        output = output + " {0}{1} |".format(tileOutput, TERMINAL_RESET)
        if i%3 == 2:
            print('''{0}
   +---+---+---+'''.format(output))
            output = ""
    
    print('''     A   B   C
''')

# This function displays an input field for the user to type and enter something.
def displayUserInput():
    userInput = input(">> {0}".format(TERMINAL_FG_YELLOW))
    print(TERMINAL_RESET, end="")
    return userInput

# This function displays an empty string.
def displayVoidPrint():
    print()

# This function displays an input field where the user should only press Enter to continue.
def displayVoidUserInput():
    input(">> {0}".format(TERMINAL_FGBG_BLACK))
    print(TERMINAL_RESET)