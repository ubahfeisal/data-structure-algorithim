def remove_duplicates(sequence):
    input_list = []
    encountered = set()

    for element in sequence:

        if element not in encountered:
            input_list.append(element)
            encountered.add(element)
    return input_list

# test
input_sequence = [1,1,1,1,2,2,2,2]
result = remove_duplicates(input_sequence)
print(result)