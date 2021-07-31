def bubble_sort(e, key):
    size = len(e)

    for j in range(size - 1):
        swapped = False
        for i in range(size - 1):
            if e[i][key] > e[i + 1][key]:
                tmp = e[i]
                e[i] = e[i + 1]
                e[i + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubble_sort(elements, "name")
    print(elements)
