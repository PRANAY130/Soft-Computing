# ============================================================
#   Travelling Salesman Problem (TSP) - Genetic Algorithm
# ============================================================
# CONCEPT:
#   Given N cities, find the shortest route that visits every
#   city exactly once and returns to the starting city.
#
# GA STEPS:
#   1. Create a random initial population (set of routes)
#   2. Evaluate fitness (total distance of each route)
#   3. Select the best parents
#   4. Crossover  → produce children
#   5. Mutate     → small random swaps to add variety
#   6. Repeat for many generations

import random
import math

# ─────────────────────────────────────────────────────────────
# CITY DATA  (you can change these or add more)
# ─────────────────────────────────────────────────────────────
cities = {
    "A": (0,  0),
    "B": (1,  5),
    "C": (5,  2),
    "D": (6,  6),
    "E": (8,  3),
    "F": (3,  8),
    "G": (7,  0),
    "H": (2,  4),
}

# ─────────────────────────────────────────────────────────────
# PARAMETERS
# ─────────────────────────────────────────────────────────────
POPULATION_SIZE = 100   # number of routes in each generation
GENERATIONS     = 500   # how many times we evolve
MUTATION_RATE   = 0.02  # chance of mutation (2%)
ELITE_SIZE      = 20    # top routes kept unchanged each generation

# ─────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def distance(city1, city2):
    """Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def route_distance(route):
    """Total distance of a route (last city → first city included)."""
    total = 0
    for i in range(len(route)):
        total += distance(route[i], route[(i + 1) % len(route)])
    return total


def fitness(route):
    """Fitness = 1 / distance  (shorter route → higher fitness)."""
    return 1 / route_distance(route)


# ─────────────────────────────────────────────────────────────
# POPULATION FUNCTIONS
# ─────────────────────────────────────────────────────────────

def create_route():
    """Create one random route visiting all cities."""
    return random.sample(list(cities.keys()), len(cities))


def initial_population():
    """Create the starting population of random routes."""
    return [create_route() for _ in range(POPULATION_SIZE)]


def rank_routes(population):
    """Sort population by fitness (best first)."""
    return sorted(population, key=lambda r: fitness(r), reverse=True)


# ─────────────────────────────────────────────────────────────
# SELECTION
# ─────────────────────────────────────────────────────────────

def selection(ranked_pop):
    """
    Select parents using fitness-proportionate (roulette wheel) selection.
    Better routes have a higher chance of being chosen.
    """
    total_fitness = sum(fitness(r) for r in ranked_pop)
    probabilities = [fitness(r) / total_fitness for r in ranked_pop]

    # Always keep the elite (top routes) unchanged
    selected = ranked_pop[:ELITE_SIZE]

    # Fill the rest by roulette wheel
    while len(selected) < POPULATION_SIZE:
        pick = random.choices(ranked_pop, weights=probabilities, k=1)[0]
        selected.append(pick)

    return selected


# ─────────────────────────────────────────────────────────────
# CROSSOVER (Ordered Crossover — OX)
# ─────────────────────────────────────────────────────────────

def crossover(parent1, parent2):
    """
    Ordered Crossover (OX):
    - Take a slice from parent1
    - Fill remaining cities in the order they appear in parent2
    """
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))

    child = [None] * size
    child[start:end] = parent1[start:end]   # copy slice from parent1

    # Fill remaining from parent2 in order
    p2_filtered = [c for c in parent2 if c not in child]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = p2_filtered[idx]
            idx += 1

    return child


def breed_population(selected):
    """Apply crossover across the selected parents to make a new generation."""
    children = selected[:ELITE_SIZE]  # elites pass through unchanged

    pool = random.sample(selected, len(selected))
    for i in range(POPULATION_SIZE - ELITE_SIZE):
        parent1 = pool[i]
        parent2 = pool[POPULATION_SIZE - 1 - i]
        children.append(crossover(parent1, parent2))

    return children


# ─────────────────────────────────────────────────────────────
# MUTATION (Swap Mutation)
# ─────────────────────────────────────────────────────────────

def mutate(route):
    """Randomly swap two cities in the route with a small probability."""
    route = route[:]  # copy so we don't modify original
    for i in range(len(route)):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]  # swap
    return route


def mutate_population(population):
    """Apply mutation to every route in the population."""
    return [mutate(route) for route in population]


# ─────────────────────────────────────────────────────────────
# MAIN GENETIC ALGORITHM LOOP
# ─────────────────────────────────────────────────────────────

def genetic_algorithm():
    # Step 1: Create initial random population
    population = initial_population()

    print("=" * 50)
    print("  TSP - Genetic Algorithm")
    print("=" * 50)

    best_route    = None
    best_distance = float("inf")

    for gen in range(GENERATIONS):
        # Step 2: Rank by fitness
        ranked = rank_routes(population)

        # Track best overall solution
        current_best_dist = route_distance(ranked[0])
        if current_best_dist < best_distance:
            best_distance = current_best_dist
            best_route    = ranked[0]

        # Print progress every 100 generations
        if (gen + 1) % 100 == 0:
            print(f"  Generation {gen+1:4d} | Best Distance = {best_distance:.4f}")

        # Step 3: Selection
        selected = selection(ranked)

        # Step 4: Crossover
        children = breed_population(selected)

        # Step 5: Mutation
        population = mutate_population(children)

    # ── Final Results ──────────────────────────────────────
    print("=" * 50)
    print("\n>> RESULT:")
    print(f"  Best Route    : {' -> '.join(best_route)} -> {best_route[0]}")
    print(f"  Total Distance: {best_distance:.4f}")
    print("=" * 50)

    return best_route, best_distance


# ─────────────────────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    random.seed(42)   # remove this line for different results each run
    genetic_algorithm()
