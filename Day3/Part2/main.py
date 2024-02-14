file_path = './test.txt'
file_path = './Day3/Part1/input.txt'
#file_path = './Day3/Part1/test.txt'

def get_number(grid, row, col):
    start = col
    while grid[row][start].isdigit():
        start-=1
    start+=1
    end = col+1
    while grid[row][end].isdigit():
        end+=1
    return''.join(grid[row][start:end])

def check_adjacent_digit(grid,row,col):

    mlist = [[row-1,col-1], [row-1, col], [row-1,col+1],
        [row,col-1], [row,col+1],
        [row+1,col-1], [row+1, col], [row+1,col+1]]
    my_set = set()
    for inner_list in mlist:
        row,col = inner_list
        if grid[row][col].isdigit():
           my_set.add(get_number(grid, row, col))        
    if len(my_set) == 2:
        return int(my_set.pop()) * int(my_set.pop())
    return 0

try:
    with open(file_path, 'r') as file:
            grid = [list(line.strip()) for line in file.readlines()]
    
    
    #pad the outside so we don;t have to deal with numbers on the edge
    for x in range(0,len(grid)):
        (grid[x]).append('.')
        (grid[x]).insert(0,'.')
    grid.insert(0,['.'] * len(grid[0]))
    grid.append(['.'] * len(grid[0]))

    sum = 0
    for row in range(0,len(grid)):
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == '*':
                num = check_adjacent_digit(grid,row,col)
                sum += int(num)
            col+=1
    print(sum)

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")