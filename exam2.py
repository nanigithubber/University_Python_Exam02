from pathlib import Path

def read_file(filename: str): 
    fullPath = Path(filename).resolve()
    data = []
    with open(fullPath) as file:
        for line in file:
            line = line.strip()
            if line != '---': 
                data.append(int(line))
    return data

def write_file(filename: str, data: list):
  with open(filename, 'w') as file: 
    if len(data) > 0: 
        for index, line in enumerate(data):
            if index < len(data):
                file.write(str(line) + '\n')
            else:
                file.write(str(line))

def filter_numbers(data: list, keep_even: bool): 
    if keep_even == True:
        return list(filter(lambda x: x % 2 == 0, data))
    else:
        return list(filter(lambda x: x % 2 != 0, data))

def calc_percentages():

    test_even_list = filter_numbers(test_values, True)
    test_odd_list = filter_numbers(test_values, False)

    correct_even_list = filter_numbers(correct_values, True)
    correct_odd_list = filter_numbers(correct_values, False)

    overall_percent = (len(test_values)) / (len(correct_values)) * 100
    odd_percent = (len(test_odd_list) / len(correct_odd_list)) * 100
    even_percent = (len(test_even_list) / len(correct_even_list)) * 100
    percentages = (overall_percent, odd_percent, even_percent)

    return percentages

def print_results(percentages: tuple):     
    print(f'Percentage of numbers remembered:{percentages[0]:>7.2f}%')
    print(f'  --> odd numbers remembered    :{percentages[1]:>7.2f}%')
    print(f'  --> even numbers remembered   :{percentages[2]:>7.2f}%')

def main():
    input_correct = input('Enter the path to the following files:\nCORRECT DATA : ')
    input_test = input('TEST DATA    : ')

    global test_values
    global correct_values

    try:
        correct_values = read_file(input_correct) 
    except FileNotFoundError as not_found:
        print (f"ERROR: The specified file '{input_correct}' does not exist.")
        exit(0)
    try:
        test_values = read_file(input_test)
    except FileNotFoundError as not_found:
        print(f"ERROR: The specified file '{input_test}' does not exist.")
        exit(0)

    name_test_even = 'output_even.txt'
    name_test_odd = 'output_odd.txt'

    test_even = filter_numbers(test_values, True)
    test_odd = filter_numbers(test_values, False)

    write_file(name_test_even, test_even)
    write_file(name_test_odd, test_odd)

    percentages = calc_percentages()

    print_results(percentages)
    
if __name__ == '__main__':
    main()