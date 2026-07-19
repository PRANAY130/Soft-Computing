import random
import math

cities = {
    "A": (0, 0), "B": (1, 5), "C": (5, 2), "D": (6, 6),
    "E": (8, 3), "F": (3, 8), "G": (7, 0), "H": (2, 4),
}

POP_SIZE      = 100
GENERATIONS   = 500
MUTATION_RATE = 0.02


def distance(route):
    total = 0
    for i in range(len(route)):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[(i + 1) % len(route)]]
        total += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total


# Create 100 random routes
population = []
for _ in range(POP_SIZE):
    population.append(random.sample(list(cities.keys()), len(cities)))

best_route = None
best_dist  = float("inf")

# print("=" * 45)
print("  TSP - Genetic Algorithm")
# print("=" * 45)

for gen in range(1, GENERATIONS + 1):

    # Selection: tournament — pick 2 random, keep shorter
    selected = []
    for _ in range(POP_SIZE):
        r1 = random.choice(population)
        r2 = random.choice(population)
        selected.append(r1 if distance(r1) < distance(r2) else r2)

    # Mutation: randomly swap two cities in a route
    population = []
    for parent in selected:
        child = parent[:]
        for i in range(len(child)):
            if random.random() < MUTATION_RATE:
                j = random.randint(0, len(child) - 1)
                child[i], child[j] = child[j], child[i]
        population.append(child)

    # Track best route
    current = min(population, key=distance)
    if distance(current) < best_dist:
        best_dist  = distance(current)
        best_route = current

    if gen % 100 == 0:
        print(f"  Gen {gen:4d} | Best Distance = {best_dist:.4f}")

# print("=" * 45)
print("RESULT:")
print("  Route    :", " -> ".join(best_route), "->", best_route[0])
print("  Distance :", round(best_dist, 4))
# print("=" * 45)
