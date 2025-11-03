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


node = Node(1)
node.add(2)
node.add(3)
node.add(4)
current_node = node
print("[", end="")
while current_node.next != NULL:
    print(current_node.value, ", ", end="")
    current_node = current_node.next
print(f"{current_node.value}]")
