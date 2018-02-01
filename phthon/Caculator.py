class Caculator:

    def __init__(self, args):
        self.result = 0
        self.args = args

    def sum(self, args):
        result = 0
        for i in args:
            result += i

        return result

    def avg(self, args):
        result = 0
        total = sum(args)
        result = total/len(args)

        return result

args = [1, 2, 3, 4, 5 ]
a = Caculator(args)

print(a.sum(args))
print(a.avg(args))

args = [6, 7, 8, 9, 10]

b = Caculator(args)
print(b.sum(args))
print(b.avg(args))



