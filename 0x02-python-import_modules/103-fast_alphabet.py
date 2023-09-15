#!/usr/bin/python3
(lambda f, x: f(f, x))(lambda self, n: print(chr(n), end='') or (n < 90 and self(self, n + 1)), 65)
print()
