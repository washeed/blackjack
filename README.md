## Blackjack Game

This code implements a simple text-based version of the blackjack game. The game involves three players, and each player decides whether to raise their bet or stay with their current bet.

The code begins by defining a `blackjack` class that represents the game. The class has an `__init__` method that initializes the player's name (`player`) and their initial bet amount (`pot`).

There are two methods in the `blackjack` class:

1. `Raise(pot)`: This method takes the current bet amount (`pot`), adds a random number between 1 and 13 to it, and returns the updated bet amount.
2. `stay(pot)`: This method doesn't modify the bet amount (`pot`) and simply returns it.

The game starts by creating three instances of the `blackjack` class for each player and initializing their bet amounts to zero (`0`).

The code then prompts each player to decide whether to raise their bet or stay, and based on the user's input (`Y` for raise or `N` for stay), the corresponding player's bet amount is updated using the `Raise` or `stay` methods.

After the first round of betting, the code proceeds to the second and third rounds using the same logic.

Finally, the code prints the final bet amounts for each player.

Note: The code assumes that the user inputs the player's decision as either 'Y' or 'N' without any error handling.

Feel free to modify the code as needed to enhance the game or add additional functionality.
