import cProfile
import pstats
import io

# import rustimport.import_hook
import rs_extension


def generate_primes(target):
    primes = [n for n in range(2, target + 1) if rs_extension.is_prime(n)]
    return primes


def main():
    TARGET = 1_000_000
    primes = generate_primes(TARGET)
    max_prime, max_length = rs_extension.longest_sum_of_consecutive_primes(
        primes, TARGET
    )
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

        with open("v2.txt", "w+") as f:
            f.write(s.getvalue())
