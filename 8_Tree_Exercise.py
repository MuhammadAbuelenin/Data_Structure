class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, property_name):
        if property_name == "both":
            value = self.name + " (" + self.designation + ")"
        elif property_name == "name":
            value = self.name
        else:
            value = self.designation

        spaces = " " * self.get_level() * 3
        print(spaces, value)
        if len(self.children) >= 0:  # ==> if self.children:
            for child in self.children:
                child.print_tree(property_name)

    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count


def name():
    root = TreeNode("Nilupul", "CEO")

    chinmay = TreeNode("Chinmay", "CTO")

    vishwa = TreeNode("Vishwa", "Infrastructure Head")
    vishwa.add_child(TreeNode("Dhaval", "Cloud Manager"))
    vishwa.add_child(TreeNode("Abhijit", "App Manager"))

    aamir = TreeNode("Aamir", "Application Head")

    gels = TreeNode("Gels", "HR Head")
    gels.add_child(TreeNode("Peter", "DCC Manager"))
    gels.add_child(TreeNode("Waqas", "Admin Manager"))

    root.add_child(chinmay)
    root.add_child(gels)

    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    return root


if __name__ == '__main__':
    ali = name()
    print(ali.print_tree("name"))
    print(ali.print_tree("designation"))
    print(ali.print_tree("both"))
