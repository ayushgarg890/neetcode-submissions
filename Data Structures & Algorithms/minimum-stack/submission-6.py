class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self, val: int) -> None:
        self.st.append(val)
        val = min(val, self.min_st[-1] if self.min_st else val)
        self.min_st.append(val)

    def pop(self) -> None:
        self.min_st.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
