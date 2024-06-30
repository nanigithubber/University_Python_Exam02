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

def print_results():
    percentages = float()
    
    overall_percent = 100
    percentages += (overall_percent,)

    odd_percent = 100
    percentages += (odd_percent,)

    even_percent = 100
    percentages += (even_percent,)

    print(f'Percentage of numbers remembered:  {percentages[0]:2f}%')
    print(f'  --> odd numbers remembered    :  {percentages[1]:2f}%')
    print(f'  --> even numbers remembered   :  {percentages[2]:2f}%')

def main():
    input_correct = input('Enter the path to the following files:\nCORRECT DATA : ')
    input_test= input('TEST DATA    : ')

    absolute_correct = read_file(input_correct)
    absolute_test = read_file(input_test)

    write_file('output_even.txt', absolute_test, True) #even
    write_file('output_odd.txt', absolute_test, False) #odd

    # print_results()

if __name__ == '__main__':
    main()