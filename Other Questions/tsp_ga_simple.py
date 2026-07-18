import random
import math

# ── Cities (name: x, y coordinates) ──────────────────────────
cities = {
    "A": (0, 0), "B": (1, 5), "C": (5, 2), "D": (6, 6),
    "E": (8, 3), "F": (3, 8), "G": (7, 0), "H": (2, 4),
}

# ── Parameters ────────────────────────────────────────────────
POP_SIZE      = 100
GENERATIONS   = 500
MUTATION_RATE = 0.02

# ─────────────────────────────────────────────────────────────

def total_distance(route):
    total = 0
    for i in range(len(route)):
        c1 = route[i]
        c2 = route[(i + 1) % len(route)]
        x1, y1 = cities[c1]
        x2, y2 = cities[c2]
        total += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return total


def create_population():
    population = []
    for _ in range(POP_SIZE):
        route = random.sample(list(cities.keys()), len(cities))
        population.append(route)
    return population


def select_parents(population):
    selected = []

    while len(selected) < POP_SIZE:
        # Pick 2 random routes, keep the shorter one
        r1 = random.choice(population)
        r2 = random.choice(population)
        if total_distance(r1) < total_distance(r2):
            selected.append(r1)
        else:
            selected.append(r2)

    return selected



def mutate(route):
    for i in range(len(route)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route


def next_generation(selected):
    children = []

    while len(children) < POP_SIZE:
        parent = selected[len(children) % len(selected)]
        child = mutate(parent[:])
        children.append(child)

    return children


# ── Main GA Loop ──────────────────────────────────────────────

def run():
    population = create_population()
    best_route = None
    best_dist  = float("inf")

    print("=" * 45)
    print("  TSP - Genetic Algorithm (Simple Version)")
    print("=" * 45)

    for gen in range(1, GENERATIONS + 1):
        selected   = select_parents(population)
        population = next_generation(selected)

        # Check best in current generation
        current_best = min(population, key=total_distance)
        current_dist = total_distance(current_best)

        if current_dist < best_dist:
            best_dist  = current_dist
            best_route = current_best

        if gen % 100 == 0:
            print(f"  Gen {gen:4d} | Best Distance = {best_dist:.4f}")

    print("=" * 45)
    print("RESULT:")
    print("  Route    :", " -> ".join(best_route), "->", best_route[0])
    print("  Distance :", round(best_dist, 4))
    print("=" * 45)


random.seed(42)
run()
