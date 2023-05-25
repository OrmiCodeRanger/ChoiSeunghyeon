"""
https://leetcode.com/problems/design-hashmap/
"""


class MyHashMap:
    """
    무지성 10 ** 6 크기의 배열 선언!
    """

    def __init__(self):
        self.bins = [-1] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        self.bins[key] = value

    def get(self, key: int) -> int:
        return self.bins[key]

    def remove(self, key: int) -> None:
        self.bins[key] = -1


class MyHashMap2:
    """
    10 ** 4 와 근접한 소수인 10007를 사용한 크기만큼의 버킷을 활용,
    해시충돌시 체이닝 기법 사용.
    """
    BUCKET_COUNT = 10007

    @classmethod
    def get_bin(cls, bins, key):
        return bins[key % cls.BUCKET_COUNT]

    def __init__(self):
        """bins: list[ ----> bucket
            list[ ---------> hash chaining
                tuple[
                    int, --> key
                    int  --> value
                ]
            ]
        ]
        """
        self.bins: list[list[tuple[int, int]]] = \
            [[] for _ in range(self.BUCKET_COUNT)]

    def put(self, key: int, value: int) -> None:

        bin = MyHashMap2.get_bin(self.bins, key)

        for idx, tup in enumerate(bin):
            if tup[0] == key:
                # same key found
                bin[idx] = key, value
                return

        # no key exist
        bin.append((key, value))

    def get(self, key: int) -> int:

        bin = MyHashMap2.get_bin(self.bins, key)

        for idx, tup in enumerate(bin):
            if tup[0] == key:
                return tup[1]

        return -1

    def remove(self, key: int) -> None:

        bin = MyHashMap2.get_bin(self.bins, key)

        for idx, tup in enumerate(bin):
            if tup[0] == key:
                bin.pop(idx)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
