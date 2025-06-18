from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_FG_YELLOW, TERMINAL_RESET

# This function displays the gallery screen.
def displayMainScreen(player1AIName, player2AIName):
    print('''
+===================+
| AI Memory Gallery |
+===================+

[{0}1{1}] View {2}{3}{1}'s Memory
[{0}2{1}] View {4}{5}{1}'s Memory
[{0}3{1}] Return to the Title Screen
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET, TERMINAL_FG_BLUE, player1AIName, TERMINAL_FG_RED, player2AIName))

# This function displays the first part of the memory viewing screen.
def displayMemoryScreen1(memoryObjectID):
    print('''
| Now Displaying Memory ID: [{0}]'''.format(memoryObjectID))

# This function displays the second part of the memory viewing screen.
def displayMemoryScreen2(memoryObject, AIName, AINameColor):
    print('''| List of valid moves and confidence scores:
''')
    
    if len(memoryObject["validMoves"]) == 0:
        print('''| The list of valid moves is empty.
| {0}{1}{2} will resign upon seeing this position.'''.format(AINameColor, AIName, TERMINAL_RESET))
    elif len(memoryObject["validMoves"]) != 0:
        for i in range(len(memoryObject["validMoves"])):
            print("| {0} [{1}]".format(memoryObject["validMoves"][i].upper(), memoryObject["confidenceScores"][i]))
    
    print('''
| Press {0}Enter{1} to return to the Memory Selection screen.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays an error in the memory selection screen if the user enters anything other than a valid memory ID or "exit".
def displayMemorySelectionInvalidInputError():
    print('''
| Error: Invalid Input!
| Please enter a valid memory ID.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays an error in the gallery's memory selection screen if the user enters a non-existing memory ID for the selected AI.
def displayMemorySelectionNotFoundError():
    print('''
| Error: Memory ID not found!
| Please enter an existing memory ID.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the memory selection screen.
def displayMemorySelectionScreen():
    print('''| Enter a valid Memory ID to view it.
| Entering the flipped version of a Memory ID will also work.
| Enter "{0}Exit{1}" to return to the Gallery screen.

| As an example, the starting position has an ID of "{0}ooo---OOO{1}"
| A Memory ID is formatted horizontally
| from the top-left tile to the bottom-right tile of the position.

| "o" means one of Player 2's pawns.
| "-" means an empty space.
| "O" means one of Player 1's pawns.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))