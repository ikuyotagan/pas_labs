import timeit
import itertools
import string

def brute_force_password(target):
    chars = string.ascii_lowercase
    attempts = 0
    for length in range(1, len(target) + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target:
                return attempts

def measure_time(target):
    return timeit.timeit(lambda: brute_force_password(target), number=1)

passwords = {
    5: "aaaaa",
}

for length, password in passwords.items():
    time_taken = measure_time(password)
    print(f"Время подбора пароля длиной {length} символов: {time_taken:.4f} секунд")

def analyze_security(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    least_secure_password = 'a' * length
    most_secure_password = ''.join(itertools.islice(itertools.cycle(chars), length))
    
    time_least_secure = measure_time(least_secure_password)
    time_most_secure = measure_time(most_secure_password)
    
    return (least_secure_password, time_least_secure), (most_secure_password, time_most_secure)

for length in [5, 10, 15]:
    (least_secure, time_least), (most_secure, time_most) = analyze_security(length)
    print(f"\nДлина пароля: {length}")
    print(f"Наименее безопасный пароль: {least_secure}, время подбора: {time_least:.4f} секунд")
    print(f"Наиболее безопасный пароль: {most_secure}, время подбора: {time_most:.4f} секунд")
