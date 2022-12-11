import sys

from Node import DirNode, FileNode, root_dir, print_whole_directory, get_all_dir_size

input_file = sys.argv[1]

cur_dir = root_dir

limit = 100000
total_file_size = 70000000
required_free_file_size = 30000000

# ans = 1908462

if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        lines = fd.readlines()

        for line in lines:
            command = line.rstrip('\n').split(' ')

            if command[0] == '$' and command[1] == 'cd':
                cur_dir = cur_dir.traverse_node(command[2])
            elif command[0] == '$' and command[1] == 'ls':
                pass
            elif command[0] == 'dir':
                cur_dir.add_child_node(DirNode(command[1], cur_dir))
            else:
                size = int(command[0])
                cur_dir.add_child_node(FileNode(command[1], size, cur_dir))

    # part 1
    total_size_within_limit = 0
    for key, item in get_all_dir_size().items():
        if item <= limit:
            total_size_within_limit += item
    print(total_size_within_limit)

    # part 2
    current_free_file_size = total_file_size - root_dir.get_size()
    required_file_size_to_clear = required_free_file_size - current_free_file_size

    # get_all_dir_size is already sorted in ascending order
    for dir_name, size in get_all_dir_size().items():
        if size >= required_file_size_to_clear:
            print(size)
            break
