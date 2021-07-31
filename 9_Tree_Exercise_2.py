class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, lvl):
        if self.get_level() > lvl:
            return
        spaces = " " * self.get_level() * 3
        print(spaces, self.data)
        if len(self.children) > 0:  # ==> if self.children:
            for child in self.children:
                child.print_tree(lvl)

    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count


def world_countries():
    root = TreeNode("Global")

    egypt = TreeNode("Egypt")
    delta = TreeNode("Delta")
    sahel = TreeNode("Sahel")
    sena = TreeNode("Sena")
    sa3ed = TreeNode("Sa3ed Masr")

    delta.add_child(TreeNode("Cairo"))
    delta.add_child(TreeNode("Giza"))
    sahel.add_child(TreeNode("Alex"))
    sena.add_child(TreeNode("Sharm El-Shikh"))
    sa3ed.add_child(TreeNode("Aswan"))

    turkey = TreeNode("Turkey")
    ege = TreeNode("Ege")
    marmara = TreeNode("Marmara")
    blacksea = TreeNode("Black Sea")
    anadol = TreeNode("Anadol")

    ege.add_child(TreeNode("Izmir"))
    ege.add_child(TreeNode("Denizli"))
    marmara.add_child(TreeNode("Istanbul"))
    blacksea.add_child(TreeNode("Trabzon"))
    anadol.add_child(TreeNode("Ankara"))

    egypt.add_child(delta)
    egypt.add_child(sahel)
    egypt.add_child(sena)
    egypt.add_child(sa3ed)

    turkey.add_child(ege)
    turkey.add_child(marmara)
    turkey.add_child(blacksea)
    turkey.add_child(anadol)

    root.add_child(egypt)
    root.add_child(turkey)

    return root


if __name__ == '__main__':
    world = world_countries()
    print(world.print_tree(2))
