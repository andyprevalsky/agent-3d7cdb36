#!/usr/bin/env python3
"""Compute and print the Collatz sequence starting from 27."""


def collatz(n):
    """Return the Collatz sequence from n down to 1, inclusive."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def validate(sequence, start):
    """Check that the sequence starts at start, ends at 1, and every transition follows the rule."""
    assert sequence[0] == start, "sequence must start with the starting value"
    assert sequence[-1] == 1, "sequence must end with 1"
    assert 1 not in sequence[:-1], "1 must appear only at the end"
    for a, b in zip(sequence, sequence[1:]):
        expected = a // 2 if a % 2 == 0 else 3 * a + 1
        assert b == expected, f"invalid transition {a} -> {b}, expected {expected}"


def main():
    start = 27
    sequence = collatz(start)
    validate(sequence, start)
    steps = len(sequence) - 1

    for number in sequence:
        print(number)
    print(f"Sequence length (numbers printed): {len(sequence)}")
    print(f"Total steps (transitions): {steps}")


if __name__ == "__main__":
    main()
