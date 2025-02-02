# Hokm Game (Python)
This repository contains a Python implementation of the card game Hokm, a popular trick-taking game played in Iran.

## About Hokm

Hokm is a partnership trick-taking game played with a standard 52-card deck.  Four players participate, forming two teams. The game involves bidding, trick-taking, and strategic card play.

## Rules of Hokm

Here's a summary of the rules, based on information from [this website](https://www.jahanshiri.ir/cardgames/en/hokm):

1. **Dealing:** The deck is shuffled, and each player receives 13 cards.

2. **Bidding (Trump Selection):** The first player to play (determined randomly at the start of the game) becomes the "Hakem" (ruler or trumper). The Hakem chooses the trump suit.

3. **Gameplay:**
   - The player to the Hakem's right leads the first trick by playing any card from their hand.
   - The other players must follow suit if they have a card of the led suit. If they don't have a card of the led suit, they can play any card, including a trump card.
   - The trick is won by the highest card of the led suit, or if any trumps are played, by the highest trump card played.
   - The winner of the trick leads the next trick.

4. **Scoring:**
   - The team that wins seven or more tricks in a round scores points.
   - The scoring system can vary, but a common system is:
     - Winning all 7 tricks is called "Kot," and awards 2 points to the winning team.
     - If the Hakem's team wins all 7 tricks, it's called "Hakem Kot" and awards 3 points to the winning team.
     - Otherwise, the winning team earns 1 point.

5. **Winning the Game:** The first team to reach a predetermined score (e.g., 7 points) wins the game.

## How to Run the Code

1. Make sure you have Python 3 installed on your system.
2. Clone this repository: `git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git` (Replace with your actual username and repository name).
3. Navigate to the directory: `cd YOUR_REPOSITORY_NAME`
4. Run the game: `python hokm.py`

## Perspectives for Future Development

This Hokm game implementation provides a solid foundation. Here are some perspectives for future development:

* **Graphical User Interface (GUI):** Creating a GUI using libraries like Tkinter, PyQt, or Pygame would significantly improve the user experience.  This would make the game more interactive and visually appealing.

* **Online Playability:** Implementing online multiplayer functionality would allow players to compete against each other over a network. This could be achieved using libraries like `socket` or by integrating with a game server.

* **Android Version:** Porting the game to Android would make it accessible to a wider audience. Kivy or BeeWare are potential frameworks for cross-platform development.

* **Multiplayer Enhancements:** Allowing games with 2, 3, or 4 players would add flexibility.  The current implementation is designed for one palyer ,and other playerds are played by computer.

* **Sound and Music:** Adding sound effects and background music would enhance the game's immersion.

I welcome contributions and suggestions for further development.  Feel free to open issues or submit pull requests.
