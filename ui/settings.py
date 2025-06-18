from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_FG_YELLOW, TERMINAL_RESET

# This function displays the confirmation message at the end of an AI's data being deleted.
def displayDeleteConfirmation():
    print('''
| Data has been successfully deleted.

| Press {0}Enter{1} to return to the Settings screen.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays an error message in the delete screen if the user enters an invalid input.
def displayDeleteInvalidInputError():
    print('''
| Error: Invalid Input!
| Please enter one of the options in quotations.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the delete screen.
def displayDeleteScreen(aiName):
    print('''| WARNING!

| You are attempting to delete the save data of {0}.
| Once this action is performed, the AI's data will be reset permanently.

| Enter "{1}Confirm{2}" to proceed with the deletion.
| Enter "{1}Exit{2}" to return to the Settings screen.
'''.format(aiName, TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the settings screen.
def displayMainScreen(isPlayer1Learning, isPlayer2Learning, player1AIName, player2AIName):
    print('''
+==========+
| Settings |
+==========+

[{0}1{1}] Toggle {2}{3}{1}'s Learning: {4}
[{0}2{1}] Toggle {5}{6}{1}'s Learning: {7}
[{0}3{1}] Rename {2}{3}{1}
[{0}4{1}] Rename {5}{6}{1}
[{0}5{1}] Delete {2}{3}{1}'s Save Data
[{0}6{1}] Delete {5}{6}{1}'s Save Data
[{0}7{1}] Return to the Title Screen
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET, TERMINAL_FG_BLUE, player1AIName, "ON" if isPlayer1Learning else "OFF", TERMINAL_FG_RED, player2AIName, "ON" if isPlayer2Learning else "OFF"))

# This function displays the rename screen confirmation message once a new name is chosen for an AI.
def displayRenameConfirmation(AIFormerName, AINameColor, AINewName):
    print('''
| {0}{1}{2}'s name has been changed to {0}{3}{2}!

| Press {4}Enter{2} to return to the Settings screen.
'''.format(AINameColor, AIFormerName, TERMINAL_RESET, AINewName, TERMINAL_FG_YELLOW))

# This function displays an error in the settings' rename screen if the user enters a name that exceeds 10 characters in length.
def displayRenameNameLengthError():
    print('''
| Error: Name Length Exceeded!
| Please enter a name within 10 characters.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the rename screen.
def displayRenameScreen(aiName):
    print('''| Enter a new name for {0}.
| The name must be at most 10 characters long.
| Enter nothing to return to the Settings screen.
'''.format(aiName))