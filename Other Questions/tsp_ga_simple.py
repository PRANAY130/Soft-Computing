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
ELITE_SIZE    = 20

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
    # Sort by shortest distance (best first)
    population.sort(key=total_distance)

    # Collect fitness values for roulette selection
    fitnesses = []
    for route in population:
        fitnesses.append(1 / total_distance(route))

    selected = population[:ELITE_SIZE]  # keep elites
    total_fit = sum(fitnesses)

    # Fill remaining spots using roulette wheel
    while len(selected) < POP_SIZE:
        pick = random.random() * total_fit
        running = 0
        for i in range(len(population)):
            running += fitnesses[i]
            if running >= pick:
                selected.append(population[i])
                break

    return selected


def crossover(p1, p2):
    # Ordered crossover (OX): take a slice from p1, fill rest from p2
    size = len(p1)
    start = random.randint(0, size - 1)
    end   = random.randint(start + 1, size)

    child = [None] * size
    child[start:end] = p1[start:end]

    pos = 0
    for city in p2:
        if city not in child:
            while child[pos] is not None:
                pos += 1
            child[pos] = city

    return child


def mutate(route):
    for i in range(len(route)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route


def next_generation(selected):
    children = selected[:ELITE_SIZE]  # elites pass unchanged
    random.shuffle(selected)

    while len(children) < POP_SIZE:
        p1 = selected[len(children) % len(selected)]
        p2 = selected[(len(children) + 1) % len(selected)]
        child = crossover(p1, p2)
        child = mutate(child)
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
