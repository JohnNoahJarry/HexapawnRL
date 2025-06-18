from scripts.constants import TERMINAL_FG_BLUE, TERMINAL_FG_RED, TERMINAL_RESET
import ui.general, ui.settings

# This function handles the settings screen loop.
def main(player1AI, player2AI):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(player1AI, player2AI)
        ui.settings.displayMainScreen(player1AI.getIsLearning(), player2AI.getIsLearning(), player1AI.getName(), player2AI.getName())
        
        choice = ui.general.displayUserInput()
        if choice == "1":
            player1AI.toggleLearning()
        elif choice == "2":
            player2AI.toggleLearning()
        elif choice == "3":
            renameScreen(player1AI, player2AI)
        elif choice == "4":
            renameScreen(player2AI, player1AI)
        elif choice == "5":
            deleteScreen(player1AI, player2AI)
        elif choice == "6":
            deleteScreen(player2AI, player1AI)
        elif choice == "7":
            return
        else:
            ui.general.displayNumberMenuInvalidInputError()
            ui.general.displayVoidUserInput()

# This function handles the delete save data screen loop.
def deleteScreen(AI1, AI2):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(AI1, AI2)
        ui.general.displayDynamicHeaderWithColor("Delete {0}{1}{2}'s Save Data".format(TERMINAL_FG_BLUE if AI1.getIsPlayer1() else TERMINAL_FG_RED, AI1.getName(), TERMINAL_RESET))
        ui.settings.displayDeleteScreen(AI1.getName())
        
        choice = ui.general.displayUserInput().lower()
        if choice == "confirm":
            AI1.deleteData()
            ui.settings.displayDeleteConfirmation()
            ui.general.displayVoidUserInput()
            return
        elif choice == "exit":
            return
        else:
            ui.settings.displayDeleteInvalidInputError()
            ui.general.displayVoidUserInput()

# This function handles the rename AI screen loop.
def renameScreen(AI1, AI2):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(AI1, AI2)
        ui.general.displayDynamicHeaderWithColor("Rename {0}{1}{2}".format(TERMINAL_FG_BLUE if AI1.getIsPlayer1() else TERMINAL_FG_RED, AI1.getName(), TERMINAL_RESET))
        ui.settings.displayRenameScreen(AI1.getName())
        
        choice = ui.general.displayUserInput()
        if choice == "":
            return
        elif len(choice) < 10:
            formerName = AI1.getName()
            AI1.setName(choice)
            ui.settings.displayRenameConfirmation(formerName, AI1.getNameColor(), choice)
            ui.general.displayVoidUserInput()
            return
        else:
            ui.settings.displayRenameNameLengthError()
            ui.general.displayVoidUserInput()
