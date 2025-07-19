from bisect import bisect_left

def binary_search(arr: list[int], target: int) -> int:
    """Performs binary search using bisect for high performance."""
    idx = bisect_left(arr, target)
    if idx != len(arr) and arr[idx] == target:
        return idx
    return -1

def get_numbers(count: int = 20) -> list[int]:
    numbers = []
    print(f"Please enter {count} integers:")
    while len(numbers) < count:
        try:
            num = int(input(f"{len(numbers)+1}: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return sorted(numbers)

def main():
    numbers = get_numbers()
    print(f"\nSorted list: {numbers}")
    try:
        target = int(input("Enter number to search: "))
        index = binary_search(numbers, target)
        if index != -1:
            print(f"\n✅ Found {target} at index {index}.")
        else:
            print("\n❌ Number not found.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
