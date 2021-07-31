def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp  # another swaping wat ==> arr[a], arr[b] = arr[b], arr[a]


def quick_sort(elements, start, end):
    if start < end:
        p = partition(elements, start, end)
        quick_sort(elements, start, p-1)
        quick_sort(elements, p+1, end)


def partition(elements, start, end):
    pivot = elements[end]
    p_index = start
    for j in range(start, end):
        if elements[j] < pivot:
            swap(p_index, j, elements)
            p_index += 1
    swap(p_index, end, elements)
    return p_index


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
