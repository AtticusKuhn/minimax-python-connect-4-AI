# Minimax Connect 4

If you want to learn about the mini-max
algorithm from computer science,
I have created this python project
which uses mini-max to design
an algorithm to play the
popular children's game
`Connect 4`.

To run this program, do
`python main.py`

# Known Weaknesses of my AI
If you want to improve this AI, here are a few
known weakness that you could use
* The AI does not have an opening book of strong first moves. Giving it an opening book would cut down on search time
* The AI does not use parity strategy to look far into the future. For example, many games of connect-4 end with "there are 20 remaining spots, so by a parity argument, I will be forced to go in that column and lose".