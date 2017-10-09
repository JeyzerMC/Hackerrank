larousse = [
    "WESH",
    "ALORS",
    "BOI",
    "JOHN",
    "CENA",
    "ALLOE",
    "VERRA"
]

nombreDeuxieme = {}

petitRobert = []

lexilogos = {}

# print "hello"

mot = input()

# for word in larousse:
#     for letter in word:

primaries = get_primes(27)

# Generate primes
for i in range(0, 27):
    nombreDeuxieme.update({string.ascii_lowercase[i] : primaries[i]})

for word in larousse:
    for letter in word: 
        

# HELPER: PRIMES
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes
