"""
replace (old, new [, count])
join
split (sep, [, max split])
rsplit similar to split but splits from the right side
splitlines: for spliting lines
"""
email = "test@gmail.com"
string = "This is a string"

print(string.replace("i", "1", 2))
print(email.replace("gmail", "yahoo"))

s1 = "/"
s2 = "abc"
print(s1.join(s2))


a=["A", "B", "C"]
print(",".join(a))

print(string.split(" "))

lines = "aaa\nbbb\nccc\n"
print(lines.splitlines())
print(lines.split())
print(lines.splitlines(True))