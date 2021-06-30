def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    elif x % 5 != 0:
        while x % 5 != 0:
            x += 1
        return x
