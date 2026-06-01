T = {16:0.4, 18:0.8, 20:1.0, 22:1.0, 24:0.8, 26:0.5}
H = {0:0.2, 20:0.8, 40:1.0, 60:0.6, 80:0.2}



alpha_t = float(input("Enter threshold for Temperature (alpha_T): "))
alpha_h = float(input("Enter threshold for Humidity    (alpha_H): "))

print(f"\nAlpha cut (T>={alpha_t}, H>={alpha_h}) result:\n")

for t in T:
    for h in H:
        if T[t] >= alpha_t and H[h] >= alpha_h:
            print(f"({t},{h}) = {max(T[t], H[h])}")