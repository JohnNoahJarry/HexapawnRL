from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_RESET
import re, scripts.utils, ui.gallery, ui.general

# This function handles the gallery screen loop.
def main(player1AI, player2AI):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(player1AI, player2AI)
        ui.gallery.displayMainScreen(player1AI.getName(), player2AI.getName())
        
        choice = ui.general.displayUserInput()
        if choice == "1":
            memorySelectionScreen(player1AI, player2AI)
        elif choice == "2":
            memorySelectionScreen(player2AI, player1AI)
        elif choice == "3":
            return
        else:
            ui.general.displayNumberMenuInvalidInputError()
            ui.general.displayVoidUserInput()

# This function handles the memory viewing screen.
def memoryScreen(AI1, memoryObjectID, AI2):
    ui.general.clearScreen()
    ui.general.displayAIStats(AI1, AI2)
    ui.gallery.displayMemoryScreen1(memoryObjectID)
    position = scripts.utils.getPositionFromPositionID(memoryObjectID)
    ui.general.displayPosition(position)
    memoryObject = AI1.memory[memoryObjectID]
    ui.gallery.displayMemoryScreen2(memoryObject, AI1.getName(), AI1.getNameColor())
    ui.general.displayVoidUserInput()

# This function handles the memory selection screen loop.
def memorySelectionScreen(AI1, AI2):
    memoryObjectIDPattern = re.compile(r'^[-Oo]{9}$')
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(AI1, AI2)
        ui.general.displayDynamicHeaderWithColor("{0}{1}{2}'s Memory Gallery".format(TERMINAL_FG_BLUE if AI1.getIsPlayer1() else TERMINAL_FG_RED, AI1.getName(), TERMINAL_RESET))
        ui.gallery.displayMemorySelectionScreen()
        
        choice = ui.general.displayUserInput()
        if memoryObjectIDPattern.match(choice):
            memoryObjectID = AI1.getMemoryObjectIDFromPositionID(choice)
            if memoryObjectID == "":
                ui.gallery.displayMemorySelectionNotFoundError()
                ui.general.displayVoidUserInput()
            elif memoryObjectID != "":
                memoryScreen(AI1, memoryObjectID, AI2)
        elif choice.lower() == "exit":
            return
        else:
            ui.gallery.displayMemorySelectionInvalidInputError()
            ui.general.displayVoidUserInput()