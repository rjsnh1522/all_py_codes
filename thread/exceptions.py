class MyException(Exception):
    def __init__(self, message="", code=1):
        super().__init__(message="dscsdcsd")


class MySecondException(Exception):
    pass


class Demo:
    dic = {
        MyException: "this is an exception",
        MySecondException: "second exception"
    }

    def ab(self):
        try:
            raise MyException('dfvdfv', 2)
        except MyException as e:
            return e
            # print(self.dic[MyException])


if __name__ == '__main__':
    print(Demo().ab())
