# Python Projects

Two command-line programs built for the Introductory Programming and Problem Solving module at the University of Wolverhampton (Year 1, 2025).

## Caesar Cipher (`caesar-cipher/`)

Encrypts and decrypts text with a Caesar cipher, from typed input or from a text file.

- Validates every input: mode, file name and a shift between 1 and 25.
- Processes files line by line and writes the result to `results.txt`, leaving punctuation, numbers and spacing intact.
- Encryption and decryption are separate, reusable functions.

```
cd caesar-cipher
python caesar.py
```

Try it with the included `messages.txt`.

## Noughts and Crosses (`noughts-and-crosses/`)

Play noughts and crosses against a rule-based computer opponent, with scores saved to a leaderboard.

- The computer checks moves in priority order: win, block, set up a fork, block a fork, take the centre, opposite corner, any corner, any edge.
- Running scores can be saved under a name and are stored as JSON in `leaderboard.txt`.

```
cd noughts-and-crosses
python play_game.py
```

**Can it be beaten?** I tested every possible game against it: it wins or draws 583 of the 585 possible game lines. The two losses come from the player taking two adjacent edges (e.g. squares 6 and 8), which creates a fork the fork-blocking rule doesn't cover. Fixing it means also blocking edge-edge forks by taking the corner between them.

Requires Python 3.8 or later. No external libraries.
