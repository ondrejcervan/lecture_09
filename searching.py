import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    # Kontrola existence souboru
    if not os.path.exists(file_path):
        print(f"File '{file_name}' does not exist.")
        return None

    try:
        # Otevření a načtení dat ze souboru
        with open(file_path, "r") as f:
            data = json.load(f)

        # Kontrola existence pole s daným názvem
        if field not in data:
            print(f"Field '{field}' not found in the file '{file_name}'.")
            return None

        # Vrácení dat pod zadaným polem
        return data[field]

    except Exception as e:
        print(f"Error reading data from '{file_name}': {e}")
        return None

def linear_search(sequence, target):

    positions = []
    count = 0
    for i, num in enumerate(sequence):
         if num == target:
            positions.append(i)
            count += 1

    return {"positions": positions, "count": count}

def pattern_search(sequence, pattern):

    positions = set()
    seq_length = len(sequence)
    pattern_length = len(pattern)

    for i in range(seq_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            positions.add((i + pattern_length)/2)

    return positions

def binary_search(numbers, target):
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None



    
def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    if sequential_data is not None:
        print(sequential_data)


if __name__ == '__main__':
    main()
