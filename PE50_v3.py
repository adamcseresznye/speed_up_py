import cProfile
import pstats
import io

# import rustimport.import_hook
import rs_extension


def main():
    TARGET = 1_000_000
    primes = rs_extension.generate_primes(TARGET)
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
        ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
        ps.print_stats()

        with open("v3.txt", "w+") as f:
            f.write(s.getvalue())
