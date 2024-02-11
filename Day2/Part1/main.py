def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            count = 1 
            for line in file:
                split_line(count, line)
                count += 1
                print("LINE:" + line.strip())  # strip() removes leading and trailing whitespaces
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def split_line(line_num, line):
   
    # Split each line by ';'
    try:
        parts = line.strip().split(';')
        print(f'Line: {line_num}: ')
        for part in parts:
            print(f'Part {part}')
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = "./input.txt"
read_file_line_by_line(file_path)