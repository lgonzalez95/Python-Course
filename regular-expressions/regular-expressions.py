"""

+: 1 or more repetitions
*: 0 or more repetitions
?: 0 or 1
{m}: Exactly m occurrences
{m,n}: From m to n.m defaults to 0.n infinity

\:
.: Matches any character except new line
^: Matches begining of a string
$: Matches ending of a string
[...]: Denotates a set of possible characters
[^...]: Matches character except the ones inside brackets
R|S: Matches either regex R or regex S


\d: Digits (0-9)
\D Non Digits
\s: Whithe space. Ex: \t \n \r \f \v
S: Non - White space
\w: Alphanumeric (A to Z, a to z, 0 to 9)
\W: Non Alphanumeric
\b: Space around words
\A: Start of the string
\Z: Ending of the string

compile(patterns, flags=0)
search(patterns, string, flags=0)
match(patterns, string, flags=0)
findall(patterns, string, flags=0)
sub(patterns, rep, string, count=0, flags=0)
"""

from re import *

test = search("^Hell.*!$", "Hello World!")

print(test)

print(search('[abc]+', 'bccbbaaac'))


print(search('[abc]{5}', 'abcabacbaaa'))