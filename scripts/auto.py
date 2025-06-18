import scripts.game, scripts.utils, ui.auto, ui.general

# This function handles the automatic learning screen loop.
def main(player1AI, player2AI):
    while True:
        ui.general.clearScreen()
        ui.general.displayAIStats(player1AI, player2AI)
        ui.auto.displayMainScreen()

        choice = ui.general.displayUserInput().lower()
        if choice == "exit":
            return
        
        try:
            choice = int(choice)
            
            if choice > 0 and choice <= 999:
                simulationScreen(choice, player1AI, player2AI)
            else:
                ui.auto.displayInputOutOfRangeError()
                ui.general.displayVoidUserInput()
        except ValueError:
            ui.auto.displayInputNotANumberError()
            ui.general.displayVoidUserInput()

# This function handles the simulation screen.
def simulationScreen(choice, player1AI, player2AI):
    player1AILevel = player1AI.getLevel()
    player2AILevel = player2AI.getLevel()
    ui.general.clearScreen()
    ui.general.displayAIStats(player1AI, player2AI)
    ui.auto.displaySimulationScreen1(choice)
    
    for i in range(choice):
        ui.auto.displaySimulationProgress(i+1, round((i+1)/choice*100))
        scripts.game.main(4, player1AI, player2AI)
    
    scripts.utils.saveAIDatabases(player1AI, player2AI)
    ui.auto.displaySimulationScreen2(choice)
    ui.general.displayAILevelDifferences(player1AI.getLevelDifference(player1AILevel), player2AI.getLevelDifference(player2AILevel))
    ui.auto.displaySimulationScreen3()
    ui.general.displayVoidUserInput()