num_red = 12
num_green = 13
num_blue = 14

def read_file_line_by_line(file_path):
    try:
 #       file = open(file_path, 'r')
 #       lines = file.readlines()
 
        with open(file_path, 'r') as file:
            sum = 0
            for line in file:
                id = int(line.split(':')[0].split(' ')[1].strip())
                print(f'Id = {id}')
                ret = split_line(line.split(':')[1].strip())
                sum = sum + ret
            print(f'Sum = {sum}')
           
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def split_line(game):
    sum = 0
    red = 0
    green = 0
    blue = 0
    red_min = 1
    green_min = 1
    blue_min = 1
    # Split each line by ';'
    try:
        print(f'{game}')
        role = game.strip().split(';')
        for role in role:
#            print(f'Grab {grab}')
            color_counts = role.strip().split(',')
            for color_count in color_counts:
#                print(f'Color Count {color_count}')
                color_count_split = color_count.strip().split(' ')
 #              print(f'Color Split {color_count_split}')
                color = color_count_split[1].lower()  # Convert to lowercase for case-insensitivity
                if color == "red":
                    red = int(color_count_split[0])
                    if red > red_min:
                        red_min = red                
                elif color == "green":
                    green = int(color_count_split[0])
                    if green > green_min:
                        green_min = green
                elif color == "blue":
                    blue = int(color_count_split[0])
                    if blue > blue_min:
                        blue_min = blue
                else:
                    print(f"Index 1 has an unrecognized color: {color}, {grabs}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    print("Valid")
    sum = red_min*green_min*blue_min
    print(f'Game: {game}  Sum {sum} ')
    return sum

# Example usage:
file_path = "../input.txt"
read_file_line_by_line(file_path)