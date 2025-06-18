from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_RESET
import json, random, scripts.utils

# AI Object.
class AI:
    def __init__(self, isPlayer1):
        # The AI's memory and knowledge from past games.
        self.memory = {}
        # A temporary list that stores played moves and the positions of those played moves in a match.
        self.history = []
        # The AI's display name.
        self.name = "P1 AI" if isPlayer1 else "P2 AI"
        # The AI's display name color.
        self.nameColor = TERMINAL_FG_BLUE if isPlayer1 else TERMINAL_FG_RED
        # An arbitrary number that equals the amount of moves deleted from the AI's memory.
        self.level = 1
        # The amount of times the AI lost.
        self.losses = 0
        # The amount of times the AI won.
        self.wins = 0
        # The AI's learning status.
        # When this is set to "True", the AI will update its history as it plays, and update its memory at the end of each match to learn from previous matches.
        # When this is set to "False", history updates will not occur, and memory updates will not occur at the end of each match.
        self.isLearning = True
        # An identifier for whether the AI is the Player 1 AI or not.
        self.isPlayer1 = isPlayer1
    
    # This method checks if a memory object already exists in the AI's memory.
    # If the memory object does not exist, it will create one.
    # The method returns the memory object's ID, whether it is flipped or not.
    def checkForPositionInMemory(self, originalPositionID, position, validMoves):
        if originalPositionID not in self.memory:
            position = scripts.utils.getFlippedPosition(position)
            flippedPositionID = scripts.utils.getPositionIDFromPositon(position)
            if flippedPositionID not in self.memory:
                position = scripts.utils.getFlippedPosition(position)
                self.memory[originalPositionID] = self.createMemoryObject(validMoves)
            elif flippedPositionID in self.memory:
                position = scripts.utils.getFlippedPosition(position)
                return flippedPositionID

        return originalPositionID
    
    # This method creates a history object and returns the created history object.
    def createHistoryObject(self, choice, positionID):
        # The history object itself.
        historyObject = {}
        # The move that the AI chose on this position.
        historyObject["choice"] = choice
        # The position where the AI made the chosen move.
        historyObject["positionID"] = positionID
        return historyObject
    
    # This method creates a memory object and returns the created memory object.
    def createMemoryObject(self, validMoves):
        # The memory object itself.
        memoryObject = {}
        # A list of valid moves for this position.
        memoryObject["validMoves"] = validMoves
        # A list of scores parallel to the valid moves list.
        # The scores are used for weighted random selection by the AI.
        memoryObject["confidenceScores"] = []
        for i in range(len(validMoves)):
            memoryObject["confidenceScores"].append(1)
        
        return memoryObject
    
    # This method resets the AI's memory, level, losses, and wins.
    # The method also saves the AI's data.
    def deleteData(self):
        self.memory = {}
        self.level = 1
        self.losses = 0
        self.wins = 0
        self.saveData()

    # This method returns the AI's learning status.
    def getIsLearning(self):
        return self.isLearning
    
    # This method returns the AI's player identifier.
    def getIsPlayer1(self):
        return self.isPlayer1
    
    # This method returns the AI's level.
    def getLevel(self):
        return self.level
    
    # This method returns a string that displays the level difference between the AI's former level and its current level.
    # If there is no difference in level, the method returns an empty string.
    def getLevelDifference(self, formerLevel):
        if formerLevel != self.level:
            return "| {0}{1}{2} leveled up {3} time(s)! [{4} -> {5}]".format(self.nameColor, self.name, TERMINAL_RESET, self.level-formerLevel, formerLevel, self.level)
        
        return ""
    
    # This method returns a related memory object's ID from a given position ID.
    # If the memory object does not exist, the method returns an empty string. 
    def getMemoryObjectIDFromPositionID(self, positionID):
        if positionID in self.memory:
            return positionID
        elif positionID not in self.memory:
            position = scripts.utils.getPositionFromPositionID(positionID)
            position = scripts.utils.getFlippedPosition(position)
            positionID = scripts.utils.getPositionIDFromPositon(position)
            if positionID in self.memory:
                return positionID
            elif positionID not in self.memory:
                return ""
    
    # This method returns the AI's display name.
    def getName(self):
        return self.name
    
    # This method returns the AI's display name color.
    def getNameColor(self):
        return self.nameColor
    
    # This method returns a string containing various stats about the AI.
    # To avoid a division by zero error, the method returns an alternative string if the AI has not finished any matches before.
    def getStatDisplay(self):
        if self.wins + self.losses == 0:
            return "| {0}{1:<10}{2} | LVL 1   | W: 0   L: 0   (0%)".format(self.nameColor, self.name, TERMINAL_RESET)
        else:
            return "| {0}{1:<10}{2} | LVL {3:<3} | W: {4:<3} L: {5:<3} ({6}%)".format(self.nameColor, self.name, TERMINAL_RESET, self.level, self.wins, self.losses, round(self.wins/(self.wins+self.losses)*100))
    
    # This method chooses a valid move from the memory object related to the current position.
    # The method returns the chosen move and the move's confidence score.
    # If the memory object's valid move list is empty, the method returns an empty string as the confidence score, and returns a resignation string as the valid move.
    def getValidMoveChoice(self, position, validMoves):
        originalPositionID = scripts.utils.getPositionIDFromPositon(position)
        memoryObjectPositionID = self.checkForPositionInMemory(originalPositionID, position, validMoves)
        targetMemoryObject = self.memory[memoryObjectPositionID]
        if len(targetMemoryObject["validMoves"]) == 0:
            return "", "resign"
        
        choice = random.choices(targetMemoryObject["validMoves"], targetMemoryObject["confidenceScores"])[0]
        
        if self.isLearning:
            self.history.append(self.createHistoryObject(choice, memoryObjectPositionID))

        condfidenceScore = " [{0}]".format(targetMemoryObject["confidenceScores"][targetMemoryObject["validMoves"].index(choice)])
        if memoryObjectPositionID == originalPositionID:
            return condfidenceScore, choice
        elif memoryObjectPositionID != originalPositionID:
            return condfidenceScore, scripts.utils.getFlippedChoice(choice)
    
    # This method loads data from the related JSON file saved in the "saves" folder.
    # If the related JSON file is not found, the AI's data will be saved and a new JSON file will be created.
    def loadData(self):
        saveData = {}
        saveDataID = "1" if self.isPlayer1 else "2"
        try:
            with open("saves/player"+saveDataID+"AI.json", "r") as file:
                saveData = json.load(file)
            
            self.memory = saveData["memory"]
            self.name = saveData["name"]
            self.level = saveData["level"]
            self.losses = saveData["losses"]
            self.wins = saveData["wins"]
            self.isLearning = saveData["isLearning"]
        except FileNotFoundError:
            self.saveData()
    
    # This method updates memory objects based on whether the AI won or not.
    # If the AI won, the final winning move is made to be the only move allowed in that position, and all other contributing moves will have thier confidence scores increased.
    # If the AI lost, the final losing move is removed from memory as well as its related confidence score, and all other contributing moves will have thier confidence scores decreased.
    # Level, wins, and losses, are adjusted accordingly, and the AI's history is cleared to prepare for the next match.
    def updateMemoryFromHistory(self, isRewarded):
        if self.isLearning:
            for i in range(len(self.history)):
                targetMemoryObject = self.memory[self.history[i]["positionID"]]
                if self.history[i]["choice"] not in targetMemoryObject["validMoves"]:
                    continue

                if i == len(self.history)-1:
                    if isRewarded:
                        self.level += len(targetMemoryObject["validMoves"])-1
                        targetMemoryObject["confidenceScores"] = [100]
                        targetMemoryObject["validMoves"] = [self.history[i]["choice"]]
                    elif not isRewarded:
                        self.level += 1
                        validMoveIndexToDelete = targetMemoryObject["validMoves"].index(self.history[i]["choice"])
                        del targetMemoryObject["validMoves"][validMoveIndexToDelete]
                        del targetMemoryObject["confidenceScores"][validMoveIndexToDelete]
                elif i != len(self.history)-1:
                    targetValidMovePointNumber = targetMemoryObject["confidenceScores"][targetMemoryObject["validMoves"].index(self.history[i]["choice"])]
                    if isRewarded:
                        targetValidMovePointNumber += 3
                        if targetValidMovePointNumber > 100:
                            targetValidMovePointNumber = 100
                    elif not isRewarded:
                        targetValidMovePointNumber -= 1
                        if targetValidMovePointNumber < 1:
                            targetValidMovePointNumber = 1
        
        if isRewarded:
            if self.wins != 999:
                self.wins += 1
        elif not isRewarded:
            if self.losses != 999:
                self.losses += 1
        
        self.history = []
    
    # This method saves the AI's stats as a JSON file for future use.
    def saveData(self):
        saveData = {}
        saveData["memory"] = self.memory
        saveData["name"] = self.name
        saveData["level"] = self.level
        saveData["losses"] = self.losses
        saveData["wins"] = self.wins
        saveData["isLearning"] = self.isLearning
        saveDataID = "1" if self.isPlayer1 else "2"
        with open("saves/player"+saveDataID+"AI.json", "w") as output:
            json.dump(saveData, output, indent=4)
    
    # This method changes the AI's name for a newly provided one.
    # The method also saves the AI's data.
    def setName(self, name):
        self.name = name
        self.saveData()

    # This method changes the AI's learning status.
    # The method also saves the AI's data.
    def toggleLearning(self):
        self.isLearning = not self.isLearning
        self.saveData()
    
    # This method is used to update the AI's history when the AI is being taken over by the user.
    # All of the user's moves are recoreded as the AI's own and will affect the AI when the match is completed.
    def updateHistory(self, position, validMoves, choice):
        if self.isLearning:
            originalPositionID = scripts.utils.getPositionIDFromPositon(position)
            memoryObjectPositionID = self.checkForPositionInMemory(originalPositionID, position, validMoves)
            if memoryObjectPositionID != originalPositionID:
                choice = scripts.utils.getFlippedChoice(choice)
            
            self.history.append(self.createHistoryObject(choice, memoryObjectPositionID))