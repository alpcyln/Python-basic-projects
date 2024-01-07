##Program to find body mass index


def index(size, kilo):
    x = kilo / size**2
    if x < 18.5:
        print(f"You are under the required weight. your index: {x}")
    if 24.9 > x > 18.4:
        print(f"You are under the required weight. your index: {x}")
    if 29.9 > x > 25:
        print(f"You are slightly over the required weight. your index: {x}")
    if 39.9 > x > 30:
        print(f"You are over the required weight. your index: {x}")
    if  x > 40:
        print(f"You are way over your normal weight. your index: {x}")

index(1.85, 65)