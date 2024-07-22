import matplotlib.pyplot as plt

class GameOfLife(object):  
    
    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]
    
    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
       
        """
    Prints the grid in a human-readable format.

    This method displays the grid with each cell's state represented by its value.
    Live cells are marked with '1' and dead cells with '0'. The grid is
    printed with borders around each cell for clarity.
         """
       
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                print("|",end="")  #add "|" before each cell
                print(self.grid[i][j],end="") #print cell value
            print("|")  #add "|" at the end of the row
            print("-"*((self.y_dim*2)+1)) #add "-" enough after each column
            

    def populate_grid(self, coord):
        #Given a list of 2D coordinates (represented as tuples/lists with 2 elements each)
        #set the corresponding elements in your grid to 1.
        #Populate the grid based on the provided coordinates
        
        for (row, col) in coord:
            # Ensure the coordinates are within the grid bounds
            if 0 <= row < self.x_dim and 0 <= col < self.y_dim:
                self.grid[row][col] = 1
        return self.grid


    def make_step(self):
        #Initialize a sum_grid with zeros
        sum_grid = [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]

        #Calculate the sum of neighbors for each cell
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                neighbor_sum = 0
                
                #Check all possible neighbors without using directions
                if i > 0 and j > 0:
                    neighbor_sum += self.grid[i-1][j-1]  #Top-left
                if i > 0:
                    neighbor_sum += self.grid[i-1][j]  #Top
                if i > 0 and j < self.y_dim - 1:
                    neighbor_sum += self.grid[i-1][j+1]  #Top-right
                if j > 0:
                    neighbor_sum += self.grid[i][j-1]  #Left
                if j < self.y_dim - 1:
                    neighbor_sum += self.grid[i][j+1]  #Right
                if i < self.x_dim - 1 and j > 0:
                    neighbor_sum += self.grid[i+1][j-1]  #Bottom-left
                if i < self.x_dim - 1:
                    neighbor_sum += self.grid[i+1][j]  #Bottom
                if i < self.x_dim - 1 and j < self.y_dim - 1:
                    neighbor_sum += self.grid[i+1][j+1]  #Bottom-right

                sum_grid[i][j] = neighbor_sum

        #Update the grid based on the rules of Game of Life
        new_grid= [[0 for _ in range(self.y_dim)] for _ in range(self.x_dim)]
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                if self.grid[i][j] == 1:  #Live cell
                    if sum_grid[i][j] < 2 or sum_grid[i][j] > 3:
                        new_grid[i][j] = 0  #Dies
                    else:
                        new_grid[i][j] = 1  #Lives
                else:  # Dead cell
                    if sum_grid[i][j] == 3:
                        new_grid[i][j] = 1  #Becomes alive

        #Update the grid
        self.grid = new_grid

    def make_n_steps(self,n):
        #Implement a method that applies the make_step method n times.
        for _ in range(n):
            self.make_step()
            
    def draw_grid(self):
        #Initialize lists to hold coordinates
        x = []
        y = []
        colors = []

        #Fill the lists with coordinates and colors based on cell states
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                x.append(j)
                y.append(i)
                # Color cells: 'black' for live, 'white' for dead
                colors.append('black' if self.grid[i][j] == 1 else 'yellow')

        #Set up the plot
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.scatter(x, y, c=colors, s=100, edgecolor='black', marker='s')  #Square markers

        #Set plot limits
        ax.set_xlim(-0.5, self.y_dim - 0.5)
        ax.set_ylim(self.x_dim - 0.5, -0.5)  #Invert y-axis to match grid layout

        #Remove axes for better visualization
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect('equal')

        plt.title('Game of Life')
        plt.show()

game = GameOfLife(30, 30)
coords = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
"""
#Get cell values from the user
coords = []
a=0
while a != -1:
    row=int(input("Enter the row of the live cell (0, 1, 2, ...): "))
    col=int(input("Enter the column of the live cell (0, 1, 2, ...): "))
    print("")
    print("Enter '-1' to finish or press Enter to continue: ", end="")
    a=int(input("") or 0)
    coords.append((row, col))
"""
game.populate_grid(coords)
game.get_grid()
game.print_grid()
game.make_n_steps(16)
game.draw_grid()