##Program that enters visa and final grades and finds course passing status ##

def program(x, y):
    visa = x * 40
    final = y * 60
    total = (visa + final) / 100

    if total >= 50:
        print(f"you passed {total}")
    else:
        print(f"you stayed: {total}")
        
program(40, 60)

