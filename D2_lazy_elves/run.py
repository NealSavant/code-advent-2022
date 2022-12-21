"""
Enemy Hands:
A = Rock
B = Paper
C = Scissors

My Hands:
X = Rock
Y = Paper
Z = Scissors

Points: Sum of outcome and chosen hand
Rock = 1
Paper = 2
Scissors = 3
Loss = 0
Draw = 3
Win = 6
"""

file = open('data.txt', 'r')
lines = file.readlines()
part_1_map: dict[str,int] = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}
part_2_map: dict[str,int] = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}


def calculate() -> tuple[int,int]:
    part_1_score: int = 0
    part_2_score: int = 0
    for line in lines:
        part_1_score += part_1_map.get(line.strip())
        part_2_score += part_2_map.get(line.strip())
    return (part_1_score, part_2_score)

part_1, part_2 = calculate()

print(f"Part 1 solution: {part_1}")
print(f"Part 2 solution: {part_2}")
