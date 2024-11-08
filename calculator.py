class Calculator:
    def add(self, a, b):
        return a + b

#should be a-b not b-a
    def subtract(self, a, b):
        return a - b

#for loop range should be b, not b+1
    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

#while loop should also include equal to cases and also negative cases
    def divide(self, a, b):
        negative_result = (a < 0) != (b < 0)
        a = abs(a)
        b = abs(b)
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if negative_result else result

#infinite loop, should be a >= b instead of a <= b, also covered negative cases
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        else:
            while a < 0:
                a += b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))