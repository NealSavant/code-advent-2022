
file = open('data.txt', 'r')
lines = file.readlines()

highest_number_list: list[int] = [0,0,0]
current_elf: list[int] = []

for line in lines:
    if line == "\n":
        sum_calories = sum(current_elf)
        current_elf: list[int] = []
        if sum_calories > highest_number_list[2]:
            highest_number_list.append(sum_calories)
            sorted_list = sorted(highest_number_list, reverse=True)
            sorted_list.pop(3)
            highest_number_list = sorted_list
            print(highest_number_list)                
        continue
    current_elf.append(int(line))

print(f"Elf carrying most calories has: {highest_number_list[0]} calories.")
print(f"The 3 Elves carrying the most calories have: {sum(highest_number_list)} calories.")
        
