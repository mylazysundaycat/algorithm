import sys

class CustomStack:
    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        if not self.stack:
            print(1)
        else:
            print(0)

    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)

def main():
    n = int(input())
    stack = CustomStack()

    for _ in range(n):
        instruction = sys.stdin.readline().strip()

        if instruction.startswith("push"):
            _, value = instruction.split()
            stack.push(int(value))
        elif instruction == "pop":
            stack.pop()
        elif instruction == "size":
            stack.size()
        elif instruction == "empty":
            stack.empty()
        elif instruction == "top":
            stack.top()

if __name__ == "__main__":
    main()