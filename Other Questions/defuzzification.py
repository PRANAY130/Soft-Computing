n = int(input("How many elements? "))

elements = []
for i in range(n):
    elements.append(float(input(f"  Enter element {i+1}: ")))

memberships = []
for i in range(n):
    memberships.append(float(input(f"  Enter membership for {elements[i]}: ")))

print("\nElements   :", elements)
print("Memberships:", memberships)

# 1. Centroid of Area (COA)
numerator = 0
denominator = 0
for i in range(n):
    numerator = numerator + elements[i] * memberships[i]
    denominator = denominator + memberships[i]
coa = numerator / denominator

# 2. Bisector of Area (BOA)
total = sum(memberships)
cumulative = 0
boa = elements[0]
for i in range(n):
    cumulative += memberships[i]
    if cumulative >= total / 2:
        boa = elements[i]
        break

# 3. Mean of Maximum (MOM)
max_mu = max(memberships)
max_elements = []
for i in range(n):
    if memberships[i] == max_mu:
        max_elements.append(elements[i])
mom_sum = 0
for i in range(len(max_elements)):
    mom_sum = mom_sum + max_elements[i]
mom = mom_sum / len(max_elements)

# 4. Smallest of Maximum (SOM)
som = min(max_elements)

print(f"\n1. Centroid of Area      = {coa:.4f}")
print(f"2. Bisector of Area      = {boa:.4f}")
print(f"3. Mean of Maximum       = {mom:.4f}")
print(f"4. Smallest of Maximum   = {som:.4f}")