from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import bs4

def check_lane(num, lane, grid):
    if num in grid[lane]:
        return False #means that it did find the number, therefore is NOT usable
    else:
        return True #means that it did not find the number and IS usable

def check_row(num, index, grid):
    nums = []
    for i in grid:
        if num == i[index]:
            return False #means the number does exist and is NOT usable
    return True #means that it did not find the number indicating that the number IS usable

def find_start(index):
    s = 0
    if 0 <= index <= 2:
        s = 0
    elif 3 <= index <= 5:
        s = 3
    elif 6 <= index <= 8:
        s = 6
    return s

def get_spot(x, y):

    return (9 * x) + (y + 1) 


def check_box(lane_index, index, num, grid):
    start_num = find_start(index)
    start_lane = find_start(lane_index)

    for i in range(3):
        if num in grid[start_lane + i][start_num: start_num + 3]:
            return False #means the number WAS found in the 3x3 and is NOT usable
    return True #means the number was not found and IS usable

def find_next(grid):

    for j in range(len(grid)):
        for i in range(len(grid)):
            if grid[j][i] == 0:
                return j, i
    return 'not found', 'nothing'


#empties = []
puzzle = []

#"C:\Users\Marce\Downloads\chromedriver_win32_2\chromedriver.exe"
PATH = r"C:\Users\Marce\Downloads\chromedriver_win32_2\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('https://www.nytimes.com/puzzles/sudoku/easy')
action = ActionChains(browser)
time.sleep(6)

soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
nums = soup.select('.su-board')
temp = []
dic= {}
for i in nums:
    for j in i:
        try:
            if str(j['aria-label']) == 'empty':
                temp.append(0)
                #empties.append(j['data-cell'])
            else:
                temp.append(int(j['aria-label']))

            
        except Exception:
            continue


# makes the list from a single list to a list of list
k = []
print(temp)
for i in range(len(temp)):
    if (i + 1) % 9 == 0:
        k.append(temp[i])
        puzzle.append(k)
        k = []
    else:
        k.append(temp[i])
print(k)
time.sleep(1)


def solve(grid):
    global action, browser, ct #,empties
    row, colum = find_next(grid)
    if row == 'not found':
        return True


    for i in range(1, 10):
        if check_box(row, colum, i, grid) is True and check_row(i, colum, grid) is True and check_lane(i, row, grid) is True:
            grid[row][colum] = i
            element_place = get_spot(row, colum)
            find_cell = browser.find_element(by=By.XPATH, value=f'//*[@id="pz-game-root"]/div[2]/div/div[1]/div/div/div/div[{int(element_place)}]')
            action.move_to_element(find_cell).click().send_keys(str(i)).perform()
            time.sleep(0.1)
            if solve(grid):
                return 1
            grid[row][colum] = 0

    return False



solve(puzzle)

for i in puzzle:
    print(i)



#try the nine numbers on the empty space
#if a number works then place it on the grid and go to the next one
#if a number does not work in the space, go to the previous space
    #delete the space cordinates from the list and try a bigger number then the one it had

