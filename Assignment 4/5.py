# 5. Print the characters in a string in reverse order.
# Example: s = "python" should print n, o, h, t, y, p
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
print("\n")