from module import remove_item
import sys
from os import system
system("clear")

def run_all_tests():
    tests = [
        ([1, 2, 3], 2, [1, 3]),
        ([5, 5, 6], 5, [5, 6]),  # only first occurrence removed
        ([1], 1, []),
    ]

    failure = False

    for i, (lst, item, expected) in enumerate(tests):
        try:
            original = lst.copy()

            result = remove_item(lst, item)

            print(f"Original: {original}")
            print(f"Expected: {expected}")
            print("Running...")
            print(f"Original: {lst}")
            print(f"Result: {result}")

            assert result == expected
            assert lst == original   # mutation check

            print(f"Test {i}: Pass!\n")

        except AssertionError:
            print(f"Test {i}: Fail\n")
            failure = True

        except Exception as e:
            print(f"Test {i}: Error → {type(e).__name__}: {e}\n")
            failure = True

    print("❌ Some tests failed." if failure else "✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
    sys.exit(0)