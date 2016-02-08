import typecheck as tc


class Funktion:
    @tc.typecheck
    def __call__(self, x):
        fn = tc.typecheck(self.function)
        return fn(x)

    @staticmethod
    def function(x):
        pass


class Succ(Funktion):
    @staticmethod
    def function(a: int)->int:
        return a+1

s = Succ()

print(s(4))

print(s(5))
