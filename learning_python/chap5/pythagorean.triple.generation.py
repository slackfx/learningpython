from functions import gcd
N = 50
triples = sorted(
        ((a, b, c) for a, b, c in (
            ((m**2 - n**2), (2 * m * n), (m**2 + n**2))
            for m in range(1, int(N**.5) + 1)
            for n in range(1, m)
            if (m - n) % 2 and gcd(m, n) == 1
        ) if c <= N), key=lambda *triple: sum(*triple)
)

print(triples)
