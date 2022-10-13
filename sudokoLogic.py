class SudokoChecks:

    def __init__(self):
        pass

    def check_lane(self, num, lane, grid):
        if num in grid[lane]:
            return False #means that it did find the number, therefore is NOT usable
        return True #means that it did not find the number and IS usable

    def check_row(self, num, index, grid):
        nums = []
        for i in grid:
            if num == i[index]:
                return False #means the number does exist and is NOT usable
        return True #means that it did not find the number indicating that the number IS usable

    def find_start(self, index):
        s = 0
        if 0 <= index <= 2:
            s = 0
        elif 3 <= index <= 5:
            s = 3
        elif 6 <= index <= 8:
            s = 6
        return s

    def get_spot(self, x, y):
        return (9 * x) + (y + 1)

    def check_box(self, lane_index, index, num, grid):
        start_num = self.find_start(index)
        start_lane = self.find_start(lane_index)

        for i in range(3):
            if num in grid[start_lane + i][start_num: start_num + 3]:
                return False #means the number WAS found in the 3x3 and is NOT usable
        return True #means the number was not found and IS usable

    def find_next(self, grid):
        for j in range(len(grid)):
            for i in range(len(grid)):
                if grid[j][i] == 0:
                    return j, i
        return 'not found', 'nothing'

