def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor


if __name__ == '__main__':
    test = [
        [11, 2, 5, 9, 7, 12, 68, 36],
        [174, 875, 9685, 8574, 124],
        [14, 18, 19, 25, 36, 5],
        [7, 9, 10, 12, 13],
        [1, 2, 3],
        [5, 2],
        [7],
        []
    ]

    for e in test:
        insertion_sort(e)
        print(f"=>> {e}")
