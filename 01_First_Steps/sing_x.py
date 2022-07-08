# In mathematics, the function `sign(x)` (the sign of a number)
# is defined like this:
# sign(x) = 1, if x > 0,
# sign(x) = -1, if x < 0,
# sign(x) = 0, if x = 0.
# For the given number, print the value of sign(x). It is desirable to solve
# this problem using cascading if... elif... else... statements.

x = float(input('Enter Your "x" number here: '))

# Variant # 1
if x > 0:
    print("sign(x) = 1")
elif x < 0:
    print("sign(x) = -1")
else:
    print("sign(x) = 0")

# Variant # 2
print("sign(x) = 1") if x > 0 else print("sign(x) = -1") if x < 0 else \
    print("sign(x) = 0")
