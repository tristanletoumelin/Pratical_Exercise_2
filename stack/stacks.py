from pythonds.basic.stack import Stack

def dec_in_bin(dec_number):
    remstack = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def bracketsChecker(symbolString):
    """The function bracketsChecker checks whether a given string has balanced parentheses,
    curly braces, and square brackets using a stack."""
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "({[":
            s.push(symbol)
        elif symbol in ")}]":   # We check that the closing bracket has his opening equivalent in the stack.
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if (symbol == ")" and top != "(") or \
                   (symbol == "}" and top != "{") or \
                   (symbol == "]" and top != "["):  # Equivalent to the matches function is the lecture.
                    balanced = False

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    print(dec_in_bin(89))   # Output: 1011001
    print(dec_in_bin(999))  # Output: 1111100111
    print("\n")
    print(parChecker("(())"))   # Output: True
    print(parChecker("())"))    # Output: False
    print("\n")
    print(bracketsChecker("({[()]})"))  # Output: True
    print(bracketsChecker("({[()]}"))   # Output: False
    print(bracketsChecker("({[()})"))   # Output: False
    print("\n")
