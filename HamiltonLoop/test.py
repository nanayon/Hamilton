import sys

def reverseWord(input):
    inputWords = input.split(" ")
    print(inputWords)
    inputWords = inputWords[-1::-1]
    print(inputWords)
    output = ' '.join(inputWords)
    return output

def fibonacci(num):
    a, b = 0, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a+b

#使用yield实现斐波那契数列
def fibonacci2(num):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > num):
            return
        yield a
        a, b = b, a + b
        counter += 1
        
#实现一个迭代器    
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        try:
            if self.a <= 10:
                x = self.a
                self.a += 2
                return x
        except StopIteration:
            sys.exit()

# 使用迭代器保存计算的自然数平方的结果
def gensquares(N):
    for i in range(N):
        yield i ** 2
# 使用列表保存计算的自然数平方的结果
def gensquares2(N):
    res = []
    for i in range(N):
        res.append(i*i)
    return res

if __name__ == '__main__':


