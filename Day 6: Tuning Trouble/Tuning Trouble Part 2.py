def check_repeated(window):
    window_sorted = sorted(window)

    # Index is in zero indexing
    for index in range(1, len(window_sorted)):
        if window_sorted[index - 1] == window_sorted[index]:
            return True

    return False


if __name__ == '__main__':
    datastream = input()

    # Index is in zero indexing
    window_length = 13
    for index in range(window_length, len(datastream)):
        window = datastream[index - window_length: index + 1]
        if not check_repeated(window):
            # Result will be in one indexing
            print(index + 1)
            break