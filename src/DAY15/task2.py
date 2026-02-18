import random


p_heads = 1/2
p_six = 1/6
p_independent = p_heads * p_six

print("Independent (Math) P(Heads AND 6) =", p_independent)

trials = 100000
success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        success += 1

print("Independent (Simulation) ≈", success / trials)

p_dependent = (5/10) * (4/9)
print("\nDependent (Math) P(Both Red) =", p_dependent)


# Simulation for Dependent Case
trials = 100000
success = 0

for _ in range(trials):
    bag = ["R"]*5 + ["B"]*5
    first = random.choice(bag)
    bag.remove(first)  # without replacement
    second = random.choice(bag)

    if first == "R" and second == "R":
        success += 1

print("Dependent (Simulation) ≈", success / trials)

print("\nWhy denominator changed?")
print("Because after picking the first marble, total marbles reduce from 10 to 9 (no replacement).")
print("So the second probability depends on the first event → Dependent probability.")
