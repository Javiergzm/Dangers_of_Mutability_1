from module import update_score
import sys
from os import system
system("clear")


def run_all_tests():
    tests = [
        ({"Alice": 90}, "Alice", 100, {"Alice": 100}),
        ({"Bob": 80, "Alice": 90}, "Bob", 95, {"Bob": 95, "Alice": 90}),
    ]

    failure = False

    for i, (scores, name, new_score, expected) in enumerate(tests):
        try:
            original = scores.copy()

            result = update_score(scores, name, new_score)

            print(f"Original: {original}")
            print(f"Expected: {expected}")
            print("Running...")
            print(f"Original: {scores}")
            print(f"Result: {result}")

            assert result == expected
            assert scores == original   # mutation check

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