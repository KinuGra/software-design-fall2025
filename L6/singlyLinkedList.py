import time


class NodeNull:
    pass


NULL = NodeNull()


class Node:
    # ノードオブジェクトの作成
    def __init__(self, value):
        self.value = value
        self.next = NULL

    def add(self, value):
        current_node = self
        # 次のノードがNULLになるまでノードをたどる
        while not current_node.next == NULL:
            current_node = current_node.next
        current_node.next = Node(value)


start = time.perf_counter()

node = Node(1)
for i in range(2, 10000 + 1):
    node.add(i)

end = time.perf_counter()

current_node = node
print("[", end="")
while current_node.next != NULL:
    print(current_node.value, ", ", end="")
    current_node = current_node.next
print(f"{current_node.value}]")

print(f"処理時間：{end - start:.6f} 秒")
