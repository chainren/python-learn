def calc_area_cricle(r):
    if not isinstance(r,(int, float)):
        raise TypeError('bad operation type')
    r = int(r)
    n = 3.1415926 * r*r
    return n

r = input()

print(calc_area_cricle(int(r)))
    
