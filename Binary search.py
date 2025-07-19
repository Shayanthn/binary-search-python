from bisect import bisect_left

def binary_search(arr: list[int], target: int) -> int:
    """Efficient binary search using bisect module."""
    idx = bisect_left(arr, target)
    return idx if idx < len(arr) and arr[idx] == target else -1

def get_numbers(n: int = 20) -> list[int]:
    print(f"Enter {n} integers:")
    nums = []
    while len(nums) < n:
        try:
            nums.append(int(input(f"{len(nums)+1}> ")))
        except ValueError:
            print("⚠️ Invalid input. Try again.")
    return sorted(nums)

def main():
    numbers = get_numbers()
    print(f"\n🔢 Sorted List: {numbers}")
    try:
        target = int(input("\n🎯 Enter number to search: "))
        result = binary_search(numbers, target)
        print(f"\n✅ Found at index {result}." if result != -1 else "\n❌ Not found.")
    except ValueError:
        print("⚠️ Invalid input.")

if __name__ == "__main__":
    main()
