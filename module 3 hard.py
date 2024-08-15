data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    sum = 0
    if data_structure == []:
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    elif isinstance(data_structure, (tuple, set, list)):
        for i in data_structure:
            sum += calculate_structure_sum(i)
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
    return sum


result = calculate_structure_sum(data_structure)
print(result)
