# Primes

![Handwritten](https://img.shields.io/badge/provenance-handwritten-brightgreen)

A small, self-guessed prime number generator in Python.

## How it works

Every prime greater than 3 leaves a remainder of 1, 5, 7, or 11 when divided by 12. `primes_rows` walks these four number lines at once (`row = [1, 5, 7, 11]`, each stepping by 12), and for each candidate checks it against a running list of known primes' future multiples — rather than testing divisibility directly. If a candidate matches one of those tracked "not-prime" values, it's composite and the tracker jumps ahead by `12 * prime`; otherwise it's prime, and it gets its own tracker seeded from its square.

## Usage

```bash
python primes.py
```

Prints all primes up to the limit set by `primes_rows(1020)` at the bottom of the file. Change that number to adjust the range.
