# Top-Down RPG Basic

Welcome to the Top-Down RPG Basic game! This is a simple top-down role-playing game where you navigate through levels, fight enemies, and progress through the game.

## Features

- Navigate through levels using `W`, `A`, `S`, `D` keys.
- Fight enemies and clear levels.
- Display inventory and stats.
- Save and load game progress.
- ASCII art and rich text-based UI.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Top-Down-RPG-basic.git
    cd Top-Down-RPG-basic
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## How to Play

1. Run the game:
    ```sh
    python main.py
    ```

2. Use the following keys to navigate and interact:
    - `W`: Move up
    - `A`: Move left
    - `S`: Move down
    - `D`: Move right
    - `I`: Display inventory
    - `Q`: Quit the game

3. Clear all enemies on the level to unlock the gate and progress to the next level.

4. When you reach the gate, if all enemies are cleared, you will see a congratulations screen. Choose "continue" to proceed to the next level or "exit" to quit the game.

5. If not all enemies are cleared, you will see a wait screen with a progress bar. Clear all enemies to proceed.

## Game Structure

- `main.py`: The main entry point of the game.
- `collision.py`: Handles collision detection and interactions.
- `congratulations.py`: Displays the congratulations and wait screens.
- `essentials.py`: Contains essential game functions and variables.
- `player.py`: Manages player stats and actions.
- `stats.py`: Displays player stats.
- `inventory.py`: Manages and displays the player's inventory.
- `main_menu.py`: Displays the main menu.
- `keybinds.py`: Displays and manages key bindings.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)(there is no files for the license lol!) file for details.

## Acknowledgements

- Rich text-based UI powered by the [Rich](https://github.com/willmcgugan/rich) library.

Enjoy the game!