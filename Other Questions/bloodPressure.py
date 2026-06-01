# Membership functions
def trimf(x, a, b, c):
    return max(0, min((x-a)/(b-a), (c-x)/(c-b)))

def trapmf(x, a, b, c, d):
    if x <= a or x >= d: return 0.0
    if x >= b and x <= c: return 1.0
    if x < b: return (x-a)/(b-a)
    return (d-x)/(d-c)

# Blood Pressure (trapezoidal)
# Low    : full 1.0 upto 80, falls to 0 at 100
# Normal : rises 60->80, flat 80->120, falls 120->140
# High   : rises 120->140, full 1.0 after 140
def bp_low(x):
    if x <= 80: return 1.0
    return trapmf(x, 80, 80, 80, 100)

def bp_normal(x): return trapmf(x, 60, 80, 120, 140)

def bp_high(x):
    if x >= 140: return 1.0
    return trapmf(x, 120, 140, 140, 140)

# Temperature (trapezoidal)
# Normal : rises 35->36, flat 36->37.5, falls 37.5->39
# High   : rises 37.5->39, full 1.0 after 39
def temp_normal(x): return trapmf(x, 35, 36, 37.5, 39)

def temp_high(x):
    if x >= 39: return 1.0
    return trapmf(x, 37.5, 39, 39, 39)

bp   = float(input("Enter Blood Pressure (mmHg): "))
temp = float(input("Enter Temperature (°C)     : "))

mu_bp_high   = bp_high(bp)
mu_bp_normal = bp_normal(bp)
mu_bp_low    = bp_low(bp)
mu_temp_high = temp_high(temp)
mu_temp_norm = temp_normal(temp)

print(f"\nBP   -> Low: {mu_bp_low:.2f}, Normal: {mu_bp_normal:.2f}, High: {mu_bp_high:.2f}")
print(f"Temp -> Normal: {mu_temp_norm:.2f}, High: {mu_temp_high:.2f}")

# Apply rules using AND = min
rule1 = min(mu_bp_high,   mu_temp_high)
rule2 = min(mu_bp_normal, mu_temp_norm)
rule3 = min(mu_bp_low,    mu_temp_norm)

print(f"\nRule 1 (Poor)   = min({mu_bp_high:.2f}, {mu_temp_high:.2f}) = {rule1:.2f}")
print(f"Rule 2 (Good)   = min({mu_bp_normal:.2f}, {mu_temp_norm:.2f}) = {rule2:.2f}")
print(f"Rule 3 (Normal) = min({mu_bp_low:.2f}, {mu_temp_norm:.2f}) = {rule3:.2f}")

health = {"Poor": rule1, "Good": rule2, "Normal": rule3}
result = max(health, key=health.get)
print(f"\nHealth of the person is: {result} (strength = {health[result]:.2f})")