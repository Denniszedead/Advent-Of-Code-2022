TAB = '\t |'

class Node:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = size
        self.dir_name = None

    def get_size(self):
        pass

    def print_dir(self):
        pass

    def get_name(self):
        if self.dir_name:
            return self.dir_name
        else:
            if self.parent and self.parent != root_dir:
                return f'{self.parent.get_name()}/{self.name}'
            elif self.parent and self.parent == root_dir:
                return f'/{self.name}'
            else:
                return '/'


class DirNode(Node):
    def __init__(self, name, parent):
        super().__init__(name, parent, None)
        self.children_nodes = []

    def add_child_node(self, node):
        self.children_nodes.append(node)

    def get_size(self):
        if not self.size:
            result = 0
            for child in self.children_nodes:
                result += child.get_size()

            return result
        else:
            return self.size

    def print_dir(self, indent):
        print(f'- {self.name} (dir, size = {self.get_size()})')

        for child in self.children_nodes:
            print((TAB * indent), end=' ')
            child.print_dir(indent + 1)

    def traverse_node(self, variable):
        if variable == '/':
            return root_dir
        elif variable == '..':
            return self.parent
        else:
            for child in self.children_nodes:
                if child.name == variable:
                    return child


class FileNode(Node):
    def __init__(self, name, size, parent):
        super().__init__(name, parent, size)

    def get_size(self):
        return self.size

    def print_dir(self, indent):

        print(f'- {self.name} (file, size = {self.size})')


def print_whole_directory():
    root_dir.print_dir(1)


def get_all_dir_size():
    return get_dir_size(root_dir)


def get_dir_size(node):
    result = {}

    if isinstance(node, DirNode):
        result = {node.get_name(): node.get_size()}

        for child_node in node.children_nodes:
            result = result | get_dir_size(child_node)

    result = dict(sorted(result.items(), key=lambda x:x[1]))

    return result


root_dir = DirNode('/', None)
