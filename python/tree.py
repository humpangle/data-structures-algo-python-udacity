from typing import Generic, TypeVar, List, Callable, Type, Optional

DataT = TypeVar('DataT')


class Queue(Generic[DataT]):
    def __init__(self):
        self.store, self.head, self.tail = {}, 0, 0

    def enqueue(self, data: DataT):
        self.store[self.head] = data
        self.head += 1

    def dequeue(self):
        tail = self.tail

        if tail < self.head:
            data = self.store[tail]
            self.tail = tail + 1
            return data
        return None

    def size(self):
        return self.head - self.tail


class Tree(Generic[DataT]):
    def __init__(self, data: DataT):
        self.data = data
        self.children: List[Type[Tree]] = []
        self.parent: Optional[Type[Tree]] = None

    def dfs_in_order(self, callback: Callable[[Type['Tree']], None]):
        children = self.children

        for c in children:
            c.dfs_in_order(Callable)

        Callable(self)
