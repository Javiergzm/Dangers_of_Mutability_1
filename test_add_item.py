from module import add_item
import sys
from os import system
system("clear")

def run_all_tests():
    tests = [
        ([1, 2], 3, [1, 2, 3]),
        ([], 5, [5]),
    ]

    failure = False

    for i, (lst, item, expected) in enumerate(tests):
        try:
            original = lst.copy()

            result = add_item(lst, item)

            print(f"Original: {original}")
            print(f"Expected: {expected}")
            print("Running...")
            print(f"Original: {lst}")
            print(f"Result: {result}")

            assert result == expected
            assert lst == original   # checks mutation!

            print(f"Test {i}: Pass!\n")

        except AssertionError:
            print(f"Test {i}: Fail\n")
            failure = True

        except Exception as e:
            print(f"Test {i}: Error → {e}\n")
            failure = True

    print("❌ Failures" if failure else "✅ All passed")


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)