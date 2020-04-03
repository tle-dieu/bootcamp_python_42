import sys
import re
import string

if (
    len(sys.argv) != 3
    or sys.argv[1].isdigit()
    or sys.argv[1].isdecimal()
    or not sys.argv[2].isdigit()
   ):
    exit('ERROR')
print([word for word in re.split(rf'[{string.punctuation}\s+]', sys.argv[1])
       if len(word) > int(sys.argv[2])])
