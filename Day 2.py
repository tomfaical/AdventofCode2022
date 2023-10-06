print("Day 2: Rock, Paper, Scissors!")

file = open("C:\\Users\\faica\\Documents\\VSCode\\Personal\\Advent_of_Code_2022\\day2Input.txt", "r")
inputAoC = str(file.read())
file.close()

losses = [["A", "Z"], ["B", "X"], ["C", "Y"]]
draws = [["A", "X"], ["C", "Z"], ["B", "Y"]]
wins = [["A", "Y"], ["B", "Z"], ["C", "X"]]

inputAoC = inputAoC.split("\n")
round = []

for i in range(len(inputAoC)):
    inputAoC[i] = inputAoC[i].split(" ")
    round.append([None,None])

score = []
for i in range(len(inputAoC)):
    if inputAoC[i] in losses:
        round[i][1] = 0

    if inputAoC[i] in draws:
        round[i][1] = 3

    if inputAoC[i] in wins:
        round[i][1] = 6

    if inputAoC[i][1] == "X":
        round[i][0] = 1

    if inputAoC[i][1] == "Y":
        round[i][0] = 2

    if inputAoC[i][1] == "Z":
        round[i][0] = 3
    
    score.append(round[i][0]+round[i][1])

# Star 1 - check
score = sum(score)
print(score)
