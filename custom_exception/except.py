class ErrorWithCode(Exception):
    def __init__(self, message="Message", code=0):
        self.code = code
        self.message = message

    def __str__(self):
        return repr(f"{self.message, self.code}")


def caller():
    try:
        raise ErrorWithCode(message="New message", code="0000")
    except ErrorWithCode as e:
        print(f"{e.message} {e.code}")



if __name__ == '__main__':
    caller()
