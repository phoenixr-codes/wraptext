# (Un)comment the lines below to see the difference.

from wraptext import indent, fill
#from textwrap import indent, fill

text = f"Hello {"\x1b[1m" * 200}World\x1b[0m\nLorem Ipsum\n\n{"Yo" * 200}"
print(indent("\n".join(fill(line) for line in text.splitlines()), "  "))

