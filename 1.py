def is_prime(n: int) -> bool:
    """n が素数かどうかを判定する"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_up_to(limit: int) -> list[int]:
    """2 以上 limit 以下の素数を返す"""
    return [n for n in range(2, limit + 1) if is_prime(n)]


if __name__ == "__main__":
    try:
        limit = int(input("上限を入力してください (例: 100): "))
    except ValueError:
        print("整数を入力してください。")
        raise SystemExit(1)

    if limit < 2:
        print("2 以上の整数を入力してください。")
        raise SystemExit(1)

    result = primes_up_to(limit)
    print(f"2 から {limit} までの素数 ({len(result)} 個):")
    print(result)
