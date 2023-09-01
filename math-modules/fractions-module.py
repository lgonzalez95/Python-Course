import fractions

f1 = fractions.Fraction(5, 2)
print('{}'.format(f1))

f2 = fractions.Fraction(4, 9)
print('{}'.format(f2))

f3 = fractions.Fraction(3 / 10)
f3 = f3.limit_denominator(3)
print(f3)

print('{}'.format(f2 + f1 + f3))
print('{}'.format(f1 - f2))
print('{}'.format(f1 * f2))
print('{}'.format(f3 / f2))
print(f3.numerator)
print(f3.denominator)
