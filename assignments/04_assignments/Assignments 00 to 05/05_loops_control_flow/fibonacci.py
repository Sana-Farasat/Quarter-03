"""
Write a program to print terms in the Fibonacci sequence up to a maximum value.

In the 13th century, the Italian mathematician Leonardo Fibonacci, as a way to explain the geometric growth of a population of rabbits, devised a mathematical sequence that now bears his name. The first two terms in this sequence, Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:

Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3

Write a program that displays the terms in the Fibonacci sequence, starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!). Thus, your program should produce the following sample run:

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
"""

MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

main()

#Or

"""
Fibonacci Sequence kya hoti hai?
Fibonacci sequence aik number series hoti hai jisme:

Har number pichlay do numbers ka jama hota hai.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10) # Output: 0 1 1 2 3 5 8 13 21 34

"""
a, b = b, a + b

Yeh line actually ek shortcut hai Python ka. Yeh ek hi line mein do cheezein update kar raha hai.
a → current number
b → next number

temp = a        # 1. pehle a ko kisi temporary variable mein lo
a = b           # 2. a ko b bana do (aage move kar gaye)
b = temp + b    # 3. b ko (old a + old b) bana do

a, b = b, a + b

a = 3
b = 5

Ab ye line chalegi:
a, b = b, a + b

Yani:

a becomes 5 (jo b tha)

b becomes 3 + 5 = 8

Ab:

a = 5

b = 8

Yani Fibonacci sequence ka next step ban gaya.

Before	After
a = 3	a = 5
b = 5	b = 8
Line a, b = b, a + b ka matlab hai:

a ko b bana do
b ko (old a + old b) bana do
"""


