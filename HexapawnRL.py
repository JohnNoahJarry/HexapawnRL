import objects.ai, scripts.title

# This function calls the "title" script to officially begin the program.
def main(player1AI, player2AI):
    scripts.title.main(player1AI, player2AI)

# This function sets up and loads the AIs before the program begins.
def setup():
    player1AI = objects.ai.AI(True)
    player2AI = objects.ai.AI(False)
    player1AI.loadData()
    player2AI.loadData()
    main(player1AI, player2AI)

setup()