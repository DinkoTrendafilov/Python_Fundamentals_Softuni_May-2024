waiting_people = int(input())
lift = [int(num) for num in input().split()]

for i in range(len(lift)):
    if waiting_people > 3:
        current_number_people = (4 - lift[i])
        waiting_people -= current_number_people
        lift[i] += current_number_people

    else:
        lift[i] += waiting_people
        waiting_people = 0

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

elif sum(lift) != len(lift) * 4:
    print("The lift has empty spots!")

print(" ".join(map(str, lift)))
