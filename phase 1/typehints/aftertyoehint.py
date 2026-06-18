from collections.abc import Iterable

def calculate_discount(items: Iterable[float], discount: float) -> float:
    return sum(items) * (1-discount)


def main() -> None:
    items = [10, 20, 30]
    discount = 0.2
    total_discount = calculate_discount((x * 100 for x in items), discount)
    print(f"Total discount: {total_discount}")

if __name__ == "__main__":
    main()