def quadratic_roots(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                raise ValueError("معادله بینهایت جواب دارد")
            else:
                return []
        else:
            return [-c / b]
    else:
        delta = b*b - 4*a*c
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return [root1, root2]

# تست تابع با چند مثال
print(" rishehaye moadale x^2 - 3x + 2 = 0:")
print(quadratic_roots(1, -3, 2))

print("\n rishehaye moadale x^2 - 4x + 4 = 0:")
print(quadratic_roots(1, -4, 4))

print("\n rishehaye moadale x^2 + 1 = 0:")
print(quadratic_roots(1, 0, 1))

print("\n rishehaye moadale 2x + 4 = 0:")
print(quadratic_roots(0, 2, 4))

print("\n rishehaye moadale 0x^2 + 0x + 5 = 0:")
print(quadratic_roots(0, 0, 5))