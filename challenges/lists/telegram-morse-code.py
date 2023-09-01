codes = ['._', '_…', '_._.', '_..', '.', '.._.', '__.', '….', '..', '.___']
short = '.'
long = "_"

text = "deface"
message = ""

for x in text:
    code_position = ord(x) - ord('a')
    message+= codes[code_position]+ " "

print(message)