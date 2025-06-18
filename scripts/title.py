import scripts.auto, scripts.gallery, scripts.game, scripts.settings, ui.general, ui.title

# This function handles the title screen loop.
def main(player1AI, player2AI):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(player1AI, player2AI)
        ui.title.displayMainScreen()
        
        choice = ui.general.displayUserInput()
        if choice in ["1","2","3"]:
            scripts.game.main(int(choice), player1AI, player2AI)
        elif choice == "4":
            scripts.auto.main(player1AI, player2AI)
        elif choice == "5":
            scripts.gallery.main(player1AI, player2AI)
        elif choice == "6":
            scripts.settings.main(player1AI, player2AI)
        elif choice == "7":
            break
        else:
            ui.general.displayNumberMenuInvalidInputError()
            ui.general.displayVoidUserInput()