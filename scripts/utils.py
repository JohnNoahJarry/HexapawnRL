# This function returns the flipped version of a provided valid move.
def getFlippedChoice(choice):
    flippedChoice = ""
    for char in choice:
        if char == "a":
            flippedChoice = flippedChoice + "c"
        elif char == "c":
            flippedChoice = flippedChoice + "a"
        else:
            flippedChoice = flippedChoice + char
    
    return flippedChoice

# This function returns the flipped version of a provided position.
def getFlippedPosition(position):
    for i in range(0,7,3):
        temp = position[i]
        position[i] = position[i+2]
        position[i+2] = temp
    
    return position

# This function returns the position list of a provided position ID string.
def getPositionFromPositionID(positionID):
    position = []
    for char in positionID:
        position.append(char)
    
    return position

# This function returns the position ID string of a provided position list.
def getPositionIDFromPositon(position):
        positionID = ""
        for i in position:
            positionID = positionID + i
        
        return positionID

# This function calls for the AIs to save their data.
def saveAIDatabases(player1AI, player2AI):
    player1AI.saveData()
    player2AI.saveData()