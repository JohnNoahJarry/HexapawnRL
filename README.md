# HexapawnRL

HexapawnRL (Hexapawn Reinforcement Learning) is a terminal program that allows you to play Hexapawn with AIs that learn through reinforcement learning.
The program is built using Python's default libraries; no further libraries are required. All AI data is saved as a JSON file using Python's built-in `json` library in the `saves` folder.

## System Requirements

Any operating system with an accessible file system, and a terminal that can run Python 3.12.3 or higher.

It is recommended to use any terminal that supports the use of the `clear` or `cls` command to clear the screen. 
Terminals such as Command Prompt and Powershell on Windows, as well as most Mac and Linux default terminals should work fine.

## What is Hexapawn?

Hexapawn is a chess-based board game invented by Martin Gardner; created as a way to demonstrate how a heuristic AI similar to Donald Michie's MENACE (Matchbox Educable Noughts and Crosses Engine) can operate on a mechanical computer.

The game features a 3x3 board with only pawns occupying the first and third ranks, with the second rank being empty.

The pawns in Hexapawn operate similarly to chess pawns except with one difference: the pawns cannot move two spaces forward on their first turn.

To win a game of Hexapawn, a player must either get one of their pawns to the other side of the board, or render their opponent unable to make a legal move; either by capturing all of the opponent's pawns, or initiating a stalemate (in Hexapawn, a stalemate is a victory for the one who initiated it).

## About the AIs

The AIs in this program operate similarly to Donald Michie's MENACE (Matchbox Educable Noughts and Crosses Engine) but with a few changes made for more aggressive learning. Please read about MENACE to understand the following better.

In this program, the AIs create new memory objects as they discover them while playing, every position is not in memory from the start. When a new position is added to an AI's memory, all valid moves are given a weight of 1 by default regardless of how deep the position is in the game. All weights have a range between 1-100. If a move gains more than 100 points, it is set back to 100 points. Similarly, if a move goes below 1 point, it is set back to 1 point.

When an AI wins, all contributing moves will have their weights increased by 3, but the final move (the winning move) becomes the sole move in that position and its weight will be increased to 100 (meaning that the AI will always choose that move when that position appears again in the future).

When an AI loses, all contributing moves will have their weights decreased by 1, but the final move (the losing move) is removed from the AI's memory (meaning the AI will never play that move in that position in the future).
If a position in the AI's memory no longer has any valid moves, the AI resigns, the AI is treated as losing, and the move played before resigning becomes the losing move.

The AIs also have an arbitrary statistic called their "level" (similar to a role-playing game). This number increases every time a move is removed from the AI's memory, either from winning or losing.
 
## Features

The program's features include the following:

- Take over either the Player 1 or Player 2 AI as a human player. Whether you win or lose, both AIs update, with the AI you take over learning directly from your actions as if it was playing.
- Spectate an AI vs. AI match and watch how the AIs learn from each other.
- Activate Automatic Learning, allowing the AIs to battle each other over many battles very quickly. Essentially a fast-forward mode for those who want results immediately.
- A Gallery to view an AI's memory objects. Consult the program's instructions and try opening the JSON save files if you're lost.
- Settings to turn on or off an AI's learning. You can also rename the AIs and delete their save data.
- The AIs also have their levels, wins, loses, and win rate percentages displayed at the top of the program constantly for easy tracking.

## Credits

Hexapawn based on Martin Gardner's Hexapawn.

AIs based on Donald Michie's MENACE (Matchbox Educable Noughts and Crosses Engine).

Inspired by an online playable version of MENACE by Matthew Scroggs playable at https://mscroggs.co.uk/menace/.

Created in Python 3.12.3 by Noah Jarry. Any credit/acknowledgement/references of this code are very much appreciated. Feedback and bug/crash reports are also very much appreciated.

## Version 1.0.0 Changelog

- HexapawnRL Initial Commit