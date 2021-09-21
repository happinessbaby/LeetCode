import time

class Solution:


    def __init__(self):
        self.memo1 = {}
        self.memo2={}
        self.answer = []

    def time(func):
        def inner(self, *args, **kwargs):
            begin = time.time()
            returned_val = func(self, *args, **kwargs)
            end = time.time()
            print("time: ", end-begin)
            return returned_val
        return inner

    @time
    def addOperators(self, num, target):
        self.find1(num, '')
        self.find2(num, '')
        for exp in self.memo1.values():
            self.eval(exp, target)
        for exp in self.memo2.values():
            self.eval(exp, target)
        return list(set(self.answer))


    def find1(self, num1, first):
        if len(num1) == 1:
            return num1
        first+=num1[0]
        self.memo1[len(num1)]=first+ ';' +self.find1(num1[1:], first)[len(first):]+num1[-1]
        return self.memo1[len(num1)][:-1]

    def find2(self, num2, last):
        if len(num2) == 1:
            return num2
        last=num2[-1]+last
        self.memo2[len(num2)]= num2[0]+self.find2(num2[:-1], last)[:-len(last)]+';'+last
        return self.memo2[len(num2)][1:]

    def eval(self, exp, target):
        exp = exp.split(';')
        for i in exp:
            if len(i)>1 and i[0]=='0': return
        X = [y+exp[x] for x in range(1, len(exp)) for y in '+-*'] #[+1, -1, *1, +2, -2, *2, +3, -3, *3]
        value = [(exp[0], exp[0])]
        for n in range(0, len(X), 3):
            expression=[(value[j][0]+X[i], value[j][1]+X[i]) if '*' not in X[i] else (value[j][0]+X[i], str(eval(self.number(value[j][0])[0] + X[i]))) for j in range(len(value)) for i in range(n, n+3)]
            value = [(e[0], e[1]) for e in expression]
        for exp in expression:
            if eval(exp[1])==target:
                self.answer.append(exp[0])

    def number(self, string):
        return [string[i:] if string[i] in '+-' else string for i in range(len(string))[::-1]]


s=Solution()
print(s.addOperators("00", 0))
