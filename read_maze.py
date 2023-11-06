def read_maze(file_name): 
    '''
    Reads a maze stored in a text file and returns a 2d list containing the maze representation. 
    '''
    try: 
        with open(file_name) as file:
            maze = [[char for char in line.strip("\n")] for line in file]
            number_of_columns_in_top_row = len(maze[0])
            for row in maze:
                if len(row) != number_of_columns_in_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit 
            return maze
    except OSError:
        print("There is a problem with the file you have selected.")
        raise SystemExit
    
    
if __name__ == "__main__":
    maze = read_maze("mazes/modest_maze.txt")
    for row in maze:
        print(row)