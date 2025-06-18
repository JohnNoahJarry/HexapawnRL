from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_FG_YELLOW, TERMINAL_RESET

# This function displays the first part of when it is an AI's turn.
def displayAITurnMessage1(AIName):
    print('''| {0} is thinking...
'''.format(AIName))

# This function displays the second part of when it is an AI's turn.
def displayAITurnMessage2(AIName):
    print('''| {0} has decided what to play.

| Press {1}Enter{2} to continue and see the move.
| Enter "{1}Exit{2}" to end the match early.
'''.format(AIName, TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays an error during the user's turn if the user enters anything that's not a valid move or "resign".
def displayInvalidMoveError():
    print('''
| Error: Invalid Move!
| Please enter a valid move.

| A valid move is as such:
| Entering "A1A2" moves the piece in A1 to A2, if it is valid.
| All inputs are not case-sensitive.

| Press {0}Enter{1} to try again.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the move last played.
def displayLastMoveMessage(lastMove):
    print('''| The move "{0}" was last played.
'''.format(lastMove))

# This function displays a message when a match is cancelled early by the user.
def displayMatchCancelledMessage():
    print('''| The match has been cancelled!
''')

# This function displays the first part of the end result of the match.
def displayMatchEndMessage1(gameMode, isHumanPlayerResigned, matchStatus, player1AIName, player2AIName):
    player1Name = "{0}The User{1}".format(TERMINAL_FG_BLUE, TERMINAL_RESET) if gameMode == 1 else "{0}{1}{2}".format(TERMINAL_FG_BLUE, player1AIName, TERMINAL_RESET)
    player2Name = "{0}The User{1}".format(TERMINAL_FG_RED, TERMINAL_RESET) if gameMode == 2 else "{0}{1}{2}".format(TERMINAL_FG_RED, player2AIName, TERMINAL_RESET)
    if matchStatus == 1:
        print("| {0} wins!".format(player1Name))
    elif matchStatus == 2:
        print("| {0} wins!".format(player2Name))
    elif matchStatus == 3:
        print("| {0} has resigned and {1} wins!".format(player1Name, player2Name))
    elif matchStatus == 4:
        print("| {0} has resigned and {1} wins!".format(player2Name, player1Name))
    
    if isHumanPlayerResigned:
        print('''| No AI database updates will occur.
''')
    elif not isHumanPlayerResigned:
        print("| Please wait while the AIs update their databases...")

# This function displays the second part of the end result of the match.
def displayMatchEndMessage2():
    print('''
| Data update complete!
''')

# This function displays the third part of the end result of the match.
def displayMatchEndMessage3():
    print('''| Press {0}Enter{1} to continue!
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the rematch prompt at the end of a match.
def displayRematchPrompt():
    print('''| Rematch?

| Enter "{0}Y{1}" start a new match.
| Enter anything else to return to the title screen.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays a message at the start of a rematch.
def displayRematchStartedMessage():
    print('''| A rematch has been started!

| Press {0}Enter{1} to continue.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays a notification that it is the user's turn.
def displayUserTurnMessage(isPlayer1Turn):
    userName = "{0}User{1}".format(TERMINAL_FG_BLUE, TERMINAL_RESET) if isPlayer1Turn else "{0}User{1}".format(TERMINAL_FG_RED, TERMINAL_RESET)
    print('''| It's your turn, {0}!

| Please enter a valid move.
| Enter "{1}Resign{2}" to resign and end the match early.
'''.format(userName, TERMINAL_FG_YELLOW, TERMINAL_RESET))

# This function displays the Hexapawn welcome message, as well as the current game mode.
def displayWelcomeMessage(gameMode):
    print("| Welcome to Hexapawn!")

    if gameMode == 1:
        print("| You are currently playing as {0}Player 1{1}.".format(TERMINAL_FG_BLUE, TERMINAL_RESET))
    elif gameMode == 2:
        print("| You are currently playing as {0}Player 2{1}.".format(TERMINAL_FG_RED, TERMINAL_RESET))
    elif gameMode == 3:
        print("| You are currently spectating an AI match.")

    print('''
| Press {0}Enter{1} to continue.
'''.format(TERMINAL_FG_YELLOW, TERMINAL_RESET))