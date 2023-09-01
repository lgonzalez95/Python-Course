# Format specifier
# {[argument_index]:[flags]:[width][.precision]conversion}
# Argument index: 0, 1, 2, 3
# Flag: :<, :>, :=, :+, :, :,, :_
# Conversion: :b, :c, :d, :e, :E, :f, :F, :g, :G, :o, :x, :X, :n, :%


a=22
b=7
c=a/b
x=100000000

print("Division of {0} and {1} is {2}".format(a, b, c))

print("Division of {0:10} and {1:15} is {2:2.4}".format(a, b, c))

print("Division of {0:<10} and {1:^15} is {2:2.4}".format(a, b, c))
print(f"Division of {a:<10} and {b:^15} is {c:2.4}")

print("{0:20,}".format(x))