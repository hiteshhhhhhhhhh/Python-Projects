def main():
    greet = (input("Greeting: ")).lower().strip()
    print(f"${value(greet)}")


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
from bank import value


def test_greeting():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100