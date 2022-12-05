score_dictionary = { "A X": 3, "A Y" : 4, "A Z" : 8, "B X" : 1, "B Y" : 5, "B Z": 9, "C X" : 2, "C Y" : 6, "C Z" : 7 }
score = 0
f = open("Day2-input.txt", "r")
for score_line in f:
    score += score_dictionary[score_line.strip()]
print(score)