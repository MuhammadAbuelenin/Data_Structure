def multilevel_selection_sort(elemnts, sort_by_list):
    size = len(elemnts)
    for sort_by in sort_by_list[-1::-1]:
        for i in range(size-1):
            min_index = i
            for j in range(min_index + 1, size):
                if elemnts[j][sort_by] < elemnts[min_index][sort_by]:
                    min_index = j

            if i != min_index:
                elemnts[i], elemnts[min_index] = elemnts[min_index], elemnts[i]


if __name__ == '__main__':
    tests = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    multilevel_selection_sort(tests, ['First Name', 'Last Name'])
    print(tests)
