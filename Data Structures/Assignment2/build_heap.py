# python3

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
      n = int(input())
      self._data = [int(s) for s in input().split()]
      assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def parent(self, i):
        return int((i - 1) / 2)

    def left_child(self, i):
        return int((i * 2 + 1))

    def right_child(self, i):
        return int((i * 2 + 2))

    def shift_down(self, i):
        left_chi = self.left_child(i)
        right_chi = self.right_child(i)
        j = i
        if (left_chi < len(self._data) and self._data[left_chi] < self._data[j]):
            j = left_chi
        if (right_chi < len(self._data) and self._data[right_chi] < self._data[j]):
            j = right_chi
        if (i != j):
            self._swaps.append((i, j))
            self._data[i], self._data[j] = self._data[j], self._data[i]
            self.shift_down(j)

    def GenerateSwaps(self):
        N = len(self._data)
        for i in range(N//2, -1, -1):
            self.shift_down(i)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
