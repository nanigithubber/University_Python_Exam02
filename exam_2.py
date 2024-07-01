from pathlib import Path

def read_file(filename: str): 
    fullPath = Path(filename).resolve()
    data = []
    try: 
        with open(fullPath) as file:
            for line in file:
                line = line.strip()
                if line != '---': 
                    data.append(int(line))
        return data
    except FileNotFoundError as not_found:
        print(f'ERROR: The specified file {filename} does not exist.')
        exit(0)

def write_file(filename: str, data: list, keep_even: bool): 
  res = filter_numbers(data, keep_even)
  with open(filename, 'w') as file:
    for index, line in enumerate(res):
      if index < len(res):
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
    print(f'Percentage of numbers remembered:  {percentages[0]:.2f}%')
    print(f'  --> odd numbers remembered    :  {percentages[1]:.2f}%')
    print(f'  --> even numbers remembered   :  {percentages[2]:.2f}%')

def main():
    input_correct = input('Enter the path to the following files:\nCORRECT DATA : ')
    input_test = input('TEST DATA    : ')
    
    global correct_values
    correct_values = read_file(input_correct) # save list with correct values
    global test_values
    test_values = read_file(input_test) # saves list with test data

    name_test_even = 'output_even.txt'
    name_test_odd = 'output_odd.txt'

    write_file(name_test_even, test_values, keep_even = True)
    write_file(name_test_odd, test_values, keep_even = False)

    percentages = calc_percentages()

    print_results(percentages)
    

if __name__ == '__main__':
    main()