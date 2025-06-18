import ui.game, ui.general, scripts.utils

# This function handles the Hexapawn game loop, as well as the rematch loop.
def main(gameMode, player1AI, player2AI):
    isGreeting = True
    isRematchGreeting = False
    isRematching = True
    while isRematching:
        position = [
            "o", "o", "o",
            "-", "-", "-",
            "O", "O", "O"
        ]
        validMoves = []
        lastMove = ""
        matchStatus = 0
        player1AILevel = player1AI.getLevel()
        player2AILevel = player2AI.getLevel()
        isFirstTurn = True
        isPlayer1Turn = True
        while True:
            if gameMode != 4:
                ui.general.clearScreen()
                ui.general.displayAIStats(player1AI, player2AI)
                ui.general.displayPosition(position)

                if not isFirstTurn and matchStatus not in [3,4,5]:
                    ui.game.displayLastMoveMessage(lastMove)

                if isGreeting:
                    ui.game.displayWelcomeMessage(gameMode)
                    ui.general.displayVoidUserInput()
                    isGreeting = False
                    continue
                
                if isRematchGreeting:
                    ui.game.displayRematchStartedMessage()
                    ui.general.displayVoidUserInput()
                    isRematchGreeting = False
                    continue

            validMoves = getValidMoves(isPlayer1Turn, position)
            if matchStatus == 0:
                matchStatus = getMatchStatus(isPlayer1Turn, position, validMoves)
            
            if matchStatus != 0:
                break

            choice = ""
            userExitChoice = ""
            AIConfidenceScore = ""
            if (gameMode == 1 and isPlayer1Turn) or (gameMode == 2 and not isPlayer1Turn):
                ui.game.displayUserTurnMessage(isPlayer1Turn)
                choice = ui.general.displayUserInput().lower()
            else:
                if gameMode != 4:
                    if isPlayer1Turn:
                        ui.game.displayAITurnMessage1(player1AI.getName())
                    else:
                        ui.game.displayAITurnMessage1(player2AI.getName())

                if isPlayer1Turn:
                    AIConfidenceScore, choice = player1AI.getValidMoveChoice(position, validMoves)
                elif not isPlayer1Turn:
                    AIConfidenceScore, choice = player2AI.getValidMoveChoice(position, validMoves)
                
                if gameMode != 4:
                    if isPlayer1Turn:
                        ui.game.displayAITurnMessage2(player1AI.getName())
                    else:
                        ui.game.displayAITurnMessage2(player2AI.getName())
                    
                    userExitChoice = ui.general.displayUserInput().lower()
                    if userExitChoice == "exit":
                        matchStatus = 5
                        continue

            if choice in validMoves:
                if gameMode == 1 and isPlayer1Turn:
                    player1AI.updateHistory(position, validMoves, choice)
                elif gameMode == 2 and not isPlayer1Turn:
                    player2AI.updateHistory(position, validMoves, choice)

                position = updatePosition(choice, isPlayer1Turn, position)
                isPlayer1Turn = not isPlayer1Turn

                if isFirstTurn:
                    isFirstTurn = False
                
                lastMove = choice.upper() + AIConfidenceScore
            elif choice == "resign":
                matchStatus = 3 if isPlayer1Turn else 4
            else:
                ui.game.displayInvalidMoveError()
                ui.general.displayVoidUserInput()

        isUserResigned = False
        if matchStatus in [1,2,3,4]:
            if gameMode in [1,2]:
                isUserResigned = ((matchStatus == 3 and gameMode == 1) or (matchStatus == 4 and gameMode == 2))

            if gameMode != 4:
                ui.game.displayMatchEndMessage1(gameMode, isUserResigned, matchStatus, player1AI.getName(), player2AI.getName())

            if matchStatus in [1,4] and not isUserResigned:
                updateAIDatabases(player1AI, player2AI)
            elif matchStatus in [2,3] and not isUserResigned:
                updateAIDatabases(player2AI, player1AI)
            
            if gameMode != 4:
                if isUserResigned:
                    ui.game.displayMatchEndMessage3()
                    ui.general.displayVoidUserInput()
                elif not isUserResigned:
                    ui.game.displayMatchEndMessage2()
                    ui.general.displayAILevelDifferences(player1AI.getLevelDifference(player1AILevel), player2AI.getLevelDifference(player2AILevel))
                    ui.game.displayMatchEndMessage3()
                    ui.general.displayVoidUserInput()
        elif matchStatus == 5:
            ui.game.displayMatchCancelledMessage()
            ui.game.displayMatchEndMessage3()
            ui.general.displayVoidUserInput()

        if gameMode != 4:
            ui.general.clearScreen()
            ui.general.displayAIStats(player1AI, player2AI)
            ui.general.displayPosition(position)
            ui.game.displayRematchPrompt()
            scripts.utils.saveAIDatabases(player1AI, player2AI)
            
            choice = ui.general.displayUserInput().lower()
            if choice == "y":
                isRematchGreeting = True
            elif choice != "y":
                isRematching = False
        elif gameMode == 4:
            isRematching = False

# This function checks for and returns the current match status.
def getMatchStatus(isPlayer1Turn, position, validMoves):
    if isPlayer1Turn:
        if len(validMoves) == 0:
            return 2
        
        for i in range(6,9):
            if position[i] == "o":
                return 2
    elif not isPlayer1Turn:
        if len(validMoves) == 0:
            return 1
        
        for i in range(0,3):
            if position[i] == "O":
                return 1
    
    return 0

# This function returns a list of valid moves for the provided position for whichever player's turn is it.
def getValidMoves(isPlayer1Turn, position):
    listIndexToUserMoveDict = {
        0 : "a3",
        1 : "b3",
        2 : "c3",
        3 : "a2",
        4 : "b2",
        5 : "c2",
        6 : "a1",
        7 : "b1",
        8 : "c1"
    }
    validMoves = []
    for i in range(9):
        if isPlayer1Turn:
            if position[i] == "O":
                if i%3 != 0 and position[i-4] == "o":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i-4])
                if position[i-3] == "-":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i-3])
                if i%3 != 2 and position[i-2] == "o":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i-2])
        elif not isPlayer1Turn:
            if position[i] == "o":
                if i%3 != 0 and position[i+2] == "O":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i+2])
                if position[i+3] == "-":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i+3])
                if i%3 != 2 and position[i+4] == "O":
                    validMoves.append(listIndexToUserMoveDict[i]+listIndexToUserMoveDict[i+4])

    return validMoves

# This function calls for the AIs to update their memories after a match has ended.
def updateAIDatabases(AI1, AI2):
    AI1.updateMemoryFromHistory(True)
    AI2.updateMemoryFromHistory(False)

# This function updates and returns the position from a provided move.
def updatePosition(choice, isPlayer1Turn, position):
    userMoveToListIndexDict = {
        "a3" : 0,
        "b3" : 1,
        "c3" : 2,
        "a2" : 3,
        "b2" : 4,
        "c2" : 5,
        "a1" : 6,
        "b1" : 7,
        "c1" : 8
    }
    position[userMoveToListIndexDict[choice[:2]]] = "-"
    if isPlayer1Turn:
        position[userMoveToListIndexDict[choice[2:]]] = "O"
    elif not isPlayer1Turn:
        position[userMoveToListIndexDict[choice[2:]]] = "o"

    return position