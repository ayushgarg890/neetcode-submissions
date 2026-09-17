class MinStack:

    def __init__(self):
        self.st=[]
        self.min=0

    def push(self, val: int) -> None:
        if not self.st:
            self.min=val
            self.st.append(0)
        else:
            self.st.append(val-self.min)
            if val<self.min:
                self.min=val


    def pop(self) -> None:
        if not self.st:
            return
        
        pop =self.st.pop()

        if pop<0:
            self.min = self.min-pop


    def top(self) -> int:
        top = self.st[-1]

        if top > 0:
            return top + self.min
        return self.min

    def getMin(self) -> int:
        return self.min
        
