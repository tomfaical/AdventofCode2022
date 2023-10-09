print("Day 3: Rucksack Reorganization!")

file = open(
    "C:\\Users\\faica\\Documents\\VSCode\\Personal\\Advent_of_Code_2022\\day_3_input.txt",
    "r",
)
inputAoC = str(file.read())
file.close()

prioritiesLower = {
    "a" : 1, 
    "b" : 2, 
    "c" : 3, 
    "d" : 4, 
    "e" : 5, 
    "f" : 6, 
    "g" : 7, 
    "h" : 8, 
    "i" : 9, 
    "j" : 10, 
    "k" : 11, 
    "l" : 12, 
    "m" : 13, 
    "n" : 14, 
    "o" : 15, 
    "p" : 16, 
    "q" : 17, 
    "r" : 18, 
    "s" : 19, 
    "t" : 20, 
    "u" : 21, 
    "v" : 22, 
    "w" : 23, 
    "x" : 24, 
    "y" : 25, 
    "z" : 26
}

prioritiesUpper = {
    "A" : 27, 
    "B" : 28, 
    "C" : 29, 
    "D" : 30, 
    "E" : 31, 
    "F" : 32, 
    "G" : 33, 
    "H" : 34, 
    "I" : 35, 
    "J" : 36, 
    "K" : 37, 
    "L" : 38, 
    "M" : 39, 
    "N" : 40, 
    "O" : 41, 
    "P" : 42, 
    "Q" : 43, 
    "R" : 44, 
    "S" : 45, 
    "T" : 46, 
    "U" : 47, 
    "V" : 48, 
    "W" : 49, 
    "X" : 50, 
    "Y" : 51, 
    "Z" : 52
}


inputAoC = inputAoC.split("\n")
inp2 = []
inputAoC = inputAoC[:10]
for i in range(len(inputAoC)):
    r = int((len(inputAoC[i]))/2)
    inp2.append([[inputAoC[i][:r]],[inputAoC[i][r:]]])
inputAoC = inp2
#print(inputAoC)

matches = []
for i in range(len(inputAoC)):
    temp = [[],[]]
    for j in range(len(inputAoC[i])):
        for k in range(len(inputAoC[i][j])):
            for l in range(len(inputAoC[i][j][k])):
                temp[j].append(inputAoC[i][j][k][l])
       # print(temp)

    for j in range(len(temp)):
        for k in range(len(temp[j])):
            #print(f"k: {k}, temp[0][k]: {temp[0][k]}")
            if temp[0][k] in temp[1]:
                matches.append(temp[0][k])
#print(matches)
