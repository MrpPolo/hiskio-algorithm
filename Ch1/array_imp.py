import array

class ArrayImpl3:
    def __init__(self,size):
        self.array = [None] * size
        self.i_end = -1

    def add_by_index(self, i_add, val):

        if self.i_end + 1 == len(self.array):
            self.expand_space()

        # 判斷加入的 index 要為目前的結尾 index + 1
        if i_add > self.i_end + 1 | i_add <0:
            return

        # 空出 i_add 的位置，往右移 , 起點是最後一個 index , 到 i_add 自己那格
        for i in range(self.i_end, i_add - 1, -1):
            # 往右移一格
            self.array[i + 1] = self.array[i]
            # 清空原本那一格
            self.array[i] = None

        self.array[i_add] = val
        self.i_end += 1

    def add_by_val(self, val):
        self.add_by_index(self.i_end + 1, val)

    def expand_space(self):

        # expand list size
        array_new = [None] * (len(self.array)) * 2

        for i in range(len(self.array)):
            array_new[i] = self.array[i]

        self.array = array_new

    def search_by_index(self,idx):
        if idx > self.i_end | idx < 0:
            return None

        return self.array[idx]

    def search_by_val(self,val):
        for i in range(self.i_end):
            if self.array[i] == val:
                return self.array[i]

        return None

    def remove_by_index(self,idx):
        if idx > self.i_end | idx < 0:
            return None

        self.array[idx] == None

        for i in range(idx + 1, self.i_end+1 ,1):
            # 往左移一格
            self.array[i - 1] = self.array[i]
            # 清空原本那一格
            self.array[i] = None

        self.i_end -= 1

    def remove_by_val(self,val):
        for i in range(self.i_end):
            if self.array[i] == val:
                self.remove_by_index(i)
                return

if __name__ == "__main__":
    myarray = ArrayImpl3(5)

    myarray.add_by_val(9)
    myarray.add_by_val(1)
    myarray.add_by_val(2)
    myarray.add_by_val(3)
    myarray.add_by_val(4)

    myarray.add_by_val(99)

    myarray.add_by_index(1,50)

    print(myarray.search_by_val(9))

    print(myarray.search_by_index(4))

    myarray.remove_by_val(2)
    myarray.remove_by_index(3)