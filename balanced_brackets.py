# EASY


def isBalanced(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == "{":
            stack.append(char)
        elif char == "[":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                print("NO")
                return
            else:
                stack.pop()
        elif char == "}":
            if not stack or stack[-1] != "{":
                print("NO")
                return
            else:
                stack.pop()
        elif char == "]":
            if not stack or stack[-1] != "[":
                print("NO")
                return
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    isBalanced("{[()]}")
    isBalanced("{[(])}")
    isBalanced("{{[[(())]]}}")
    isBalanced("((((")
    isBalanced("(()))")
