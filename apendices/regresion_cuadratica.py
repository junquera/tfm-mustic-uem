from math import sqrt

xys = [
    (1.2, 4.5),
    (1.8, 5.9),
    (3.1, 7.0),
    (4.9, 7.8),
    (5.7, 7.2),
    (7.1, 6.8),
    (8.6, 4.5),
    (9.8, 2.7)
]

# finisterre
xys = [
    (1.0, 10.6), (2.0, 9.5), (3.0, 13.4), (4.0, 11.7),
    (5.0, 16.4), (6.0, 17.9), (7.0, 18.8), (8.0, 20.4),
    (9.0, 19.4), (10.0, 16.5), (11.0, 12.4), (12.0, 12.4)
]

# cabogata
xys = [
    (1.0, 12.2), (2.0, 10.8), (3.0, 14.5), (4.0, 15.6),
    (5.0, 20.4), (6.0, 24.1), (7.0, 25.8), (8.0, 26.7),
    (9.0, 23.7), (10.0, 19.3), (11.0, 16.4), (12.0, 13.5)
]

i = 0
j = 0
k = 0
l = 0

u = 0
v = 0
w = 0

n = len(xys)

for x, y in xys:
    i += x
    j += x**2
    k += x**3
    l += x**4

    u += y
    v += (x * y)
    w += ((x**2) * y)


print("i", i)
print("j", j)
print("k", k)
print("l", l)
print("u", u)
print("v", v)
print("w", w)

c = (u*l - w*j)/(l*n - j**2)
c1 = (j*k*l*v - j*(k**2)*w - i*(l**2)*v + i*k*l*w)
c2 = (j*(l**2)*n - (k**2)*l*n - (j**3)*l + (j**2)*(k**2))
c +=  c1 / c2
r1 = ((j**2)*(k**2)-2*(i*j*k*l)+(i**2)*(l**2))
r2 = (j*(l**2)*n - (k**2)*l*n - (j**3)*l + (j**2)*(k**2))
r = r1 / r2
c = c / (1 - r)

b = (v*l - k*w + c*j*k - c*i*l) / (j*l - k**2)
a = (w - b*k - c*j) / l

print("a", a)
print("b", b)
print("c", c)

print("%sx² + %sx + %s" % (a, b, c))
