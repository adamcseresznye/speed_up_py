import cProfile
import pstats
import io


def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_primes(target):
    primes = [n for n in range(2, target + 1) if is_prime(n)]
    return primes


def longest_sum_of_consecutive_primes(primes, target):
    max_length = 0
    max_prime = 0

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            sum_of_primes = sum(primes[i:j])
            if sum_of_primes > target:
                break
            if is_prime(sum_of_primes) and (j - i) > max_length:
                max_length = j - i
                max_prime = sum_of_primes

    return max_prime, max_length


def main():
    TARGET = 1_000_000
    primes = generate_primes(TARGET)
    max_prime, max_length = longest_sum_of_consecutive_primes(primes, TARGET)
    print(f"Prime: {max_prime}, Length: {max_length}")


if __name__ == "__main__":
    with cProfile.Profile() as pr:

        pr = cProfile.Profile()
        pr.enable()
        main()
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats("tottime")
        ps.print_stats()

        with open("v0.txt", "w+") as f:
            f.write(s.getvalue())
