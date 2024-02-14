
file_path = './test.txt'
file_path = './Day3/Part1/input.txt'
#ile_path = './Day3/Part1/test.txt'

def get_number(grid, row, col):
    rStart = col
    while col < len(grid[row]) and grid[row][col].isdigit():
        col+=1
    r = range(rStart,col)
    num = ''.join(grid[row][r.start:r.stop])
    return num, r

def check_adjacent_symbol(grid,row,r):
    notsym = ['.', 0,1,2,3,4,5,6,7,8,9]

    new_range = range(r.start-1,r.stop+1)
    mlist = [[row-1, second_element] for second_element in new_range]
    mlist.extend([[row+1, second_element] for second_element in new_range])
    mlist.append([row,r.start-1])
    mlist.append([row,r.stop])
    for inner_list in mlist:
        row,col = inner_list
        if grid[row][col] not in notsym:
            return True
    return False

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
            if grid[row][col].isdigit():
                # found a number that has an adjancent symbol
                num, r = get_number(grid, row,col)

                if check_adjacent_symbol(grid,row,r):
                    sum += int(num)
                else:
                    pass
                col = r.stop
            else:
                    col+=1

    print(sum)

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")