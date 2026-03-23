from module import append_to_tuple
import sys


def run_all_tests():
    tests = [
        ((1, 2), 4, (1, 2, 4)),
        ((), 5, (5,)),
        (("C","J","T"), "W", ("C","J","T", "W")),
    ]

    failure = False

    for i, (data, item, expected) in enumerate(tests):
        try:
            original = data

            result = append_to_tuple(data, item)

            print(f"Original: {original}")
            print(f"Expected: {expected}")
            print("Running...")
            print(f"Original: {original}")
            print(f"Result: {result}")

            assert result == expected
            assert data == original   # mutation check

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