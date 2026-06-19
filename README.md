# Fruit-Professor-Game
This is a Fruit Professor Playoff — a turn-based elimination game for multiple players. Here's how it works:
Setup
The game starts by asking how many players are participating, then collects each player's name. There's a predefined list of 10 valid fruits: apple, banana, cherry, durian, fig, guava, mango, lemon, longan, and kiwi.
Gameplay Loop
Players take turns (cycling through the player list in order) and must type the name of a fruit on each turn. A player is eliminated if they:

Enter something that isn't in the valid fruit list, or
Enter a fruit that has already been named by a previous player

Winning
The game continues until only one player remains, who is then crowned the "Fruits Professor". The full list of correctly named fruits is also displayed at the end.
A few things worth noting about the code:

The valid fruit list is quite small (only 10 fruits), meaning the game will always end within 10 successful turns at most — players will inevitably run out of new fruits to name.
Turn order is managed with a playerCount variable and modulo (%) against the current player list length, which correctly handles players being removed mid-game.
Input is normalized to lowercase, so "Apple" and "apple" are treated the same.
There's no handling for an empty player list (e.g. if only 1 player is entered at the start, the game would skip straight to crowning them without any actual play).
