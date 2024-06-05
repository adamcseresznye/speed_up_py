// rustimport:pyo3

use pyo3::prelude::*;

#[pyfunction]
fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    let mut i = 2;
    while i * i <= n {
        if n % i == 0 {
            return false;
        }
        i += 1;
    }
    true
}

#[pyfunction]
fn longest_sum_of_consecutive_primes(primes: Vec<u32>, target: u32) -> (u32, usize) {
    let mut max_length: usize = 0;
    let mut max_prime: u32 = 0;

    for i in 0..primes.len() {
        for j in i + max_length..primes.len() {
            let sum_of_primes: u32 = primes[i..j].iter().sum();
            if sum_of_primes > target {
                break;
            }
            if is_prime(sum_of_primes) && (j - i) > max_length {
                max_length = j - i;
                max_prime = sum_of_primes;
            }
        }
    }
    (max_prime, max_length)
}

#[pyfunction]
fn generate_primes(target: u32) -> Vec<u32> {
    (2..=target).filter(|&n| is_prime(n)).collect::<Vec<u32>>()
}
