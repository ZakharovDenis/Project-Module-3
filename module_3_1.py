calls = 0


def count_calls(calls):
    calls += calls
    return calls


def string_info(string):
    i = []
    i.append(len(string))
    i.append(string.upper())
    i.append(string.lower())
    count_calls(0)
    return i


def is_contains(string, list_to_searh):
    string.lower()
    list = []
    for i in list_to_searh:
        list.append(i.lower())
    return (string.lower() in list)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
