population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())
flag = True

if sum(population) < len(population) * minimum_wealth:
    print("No equal distribution possible")
    flag = False
else:
    for i in range(len(population)):
        if population[i] < minimum_wealth:
            diff = minimum_wealth - population[i]
            max_index = population.index(max(population))
            population[max_index] -= diff
            population[i] += diff

if flag:
    print(population)
