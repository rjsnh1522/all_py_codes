import _DataStore

class DataStore:

    def bigMethod(self):
        state ={}
        _DataStore.bigMethod(state)
        print("I am very big method")

    def hugeMethod(self):
        state = {}
        _DataStore.hugeMethod(state)
        print("I am very Huge method")
