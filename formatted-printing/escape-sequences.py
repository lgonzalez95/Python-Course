
#\n: New line
#\r: Carriage return (Beggining of same line)
#\f or \x0c: Line feed (same column of next line) 
#\t: Horizontal tab
#\v \x0b: Vertical tab
#\b: Backspace
#\a: Alert
#\o: Octal
#\x: HexaDecimal
#\u: Unicode
#\N{name}

print("Hello\f there!")
print("Hello there!\rHi")
print("Hello\v there!\b")

print(r"Hello\f there!")
print("\N{colon sign}")
print("\N{lempira sign}")