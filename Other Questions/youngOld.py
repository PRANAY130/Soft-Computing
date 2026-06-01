def bell(x, a, b, c):
    return 1 / (1 + abs((x - c) / a) ** (2 * b))

x = int(input("Enter age: "))

y = bell(x, 20, 2, 0)
o = bell(x, 30, 3, 100)

print(f"\nmu_young = {y:.4f}")
print(f"mu_old   = {o:.4f}")

print(f"\n1. More or less young    = {y**0.5:.4f}")
print(f"2. Not young and not old = {min(1-y, 1-o):.4f}")
print(f"3. Young but not too young = {min(y, 1-y**2):.4f}")
print(f"4. Extremely old         = {o**2:.4f}")