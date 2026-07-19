import random

# Items: (name, weight, value)
items = [
    ("Book",     2, 6),
    ("Camera",   1, 5),
    ("Laptop",   4, 9),
    ("Clothes",  3, 4),
    ("Phone",    1, 7),
    ("Tablet",   2, 8),
    ("Watch",    1, 6),
    ("Headset",  2, 5),
]

MAX_WEIGHT    = 8    # knapsack capacity
POP_SIZE      = 100
GENERATIONS   = 300
MUTATION_RATE = 0.02

# A chromosome is a list of 0s and 1s (1 = item picked, 0 = not picked)
# Example: [1, 0, 1, 0, 0, 1, 1, 0] means items 0,2,5,6 are selected


def fitness(chromosome):
    total_weight = 0
    total_value  = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_weight += items[i][1]
            total_value  += items[i][2]
    if total_weight > MAX_WEIGHT:
        return 0          # invalid solution — over capacity
    return total_value


# Create random population
population = []
for _ in range(POP_SIZE):
    chromosome = []
    for _ in range(len(items)):
        chromosome.append(random.randint(0, 1))
    population.append(chromosome)

best_chromosome = None
best_value      = 0

print("=" * 45)
print("  Knapsack - Genetic Algorithm")
print("=" * 45)

for gen in range(1, GENERATIONS + 1):

    # Selection: tournament — pick 2 random, keep better fitness
    selected = []
    for _ in range(POP_SIZE):
        r1 = random.choice(population)
        r2 = random.choice(population)
        if fitness(r1) > fitness(r2):
            selected.append(r1)
        else:
            selected.append(r2)

    # Mutation: randomly flip a bit (0→1 or 1→0)
    population = []
    for parent in selected:
        child = parent[:]
        for i in range(len(child)):
            if random.random() < MUTATION_RATE:
                child[i] = 1 - child[i]   # flip the bit
        population.append(child)

    # Track best chromosome
    current = max(population, key=fitness)
    if fitness(current) > best_value:
        best_value      = fitness(current)
        best_chromosome = current

    if gen % 100 == 0:
        print(f"  Gen {gen:4d} | Best Value = {best_value}")

print("=" * 45)
print("RESULT:")
total_w = 0
for i in range(len(best_chromosome)):
    if best_chromosome[i] == 1:
        name, w, v = items[i]
        total_w += w
        print(f"  + {name:10s}  weight={w}  value={v}")
print(f"  Total Weight : {total_w} / {MAX_WEIGHT}")
print(f"  Total Value  : {best_value}")
print("=" * 45)
