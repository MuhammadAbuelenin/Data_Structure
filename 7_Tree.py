class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        print(spaces, self.data)
        if len(self.children) > 0:       # ==> if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("LapTop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Lenovo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Grundig"))
    tv.add_child(TreeNode("LG"))
    tv.add_child((TreeNode("Samsung")))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Realme"))
    cellphone.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
