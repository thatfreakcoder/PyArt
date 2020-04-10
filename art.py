import pyautogui as pg
import time
import random

# I have created this program keeping in mind my screen size and Paint App coordinates. If you wish to test it on your
# computer, be sure to change the values of all coordinates, as the Paint App holds different coordinates for everyone.

def select_color_upper(clr_index): # Color Index selects the respective color numbered on the pallete

	# coordinates of the first color of first row in the pallete.
	x_clr = 738
	y_clr = 60
	jump = 22     # Distance between the X Coordinate of First and Second color in the pallete.

	pg.moveTo(x_clr + (clr_index * jump), y_clr)
	pg.click()


def select_color_lower(clr_index):

	# coordinates of the first color of second row in the pallete 
	x_clr = 738
	y_clr = 82
	jump = 22

	pg.moveTo(x_clr + (clr_index * jump), y_clr)
	pg.click()


# Function to select the brush width
def select_brush(strk_index):
	# Coordinates of Brush Size Icon
	x_selector = 630
	y_selector = 60
	pg.moveTo(x_selector, y_selector)
	time.sleep(0.2)
	pg.click()

	# Coordinates of the first brush size
	x_brush = 645
	y_brush = 95
	jump = 40    # Distance between the first and second brush size
	pg.moveTo(x_brush, y_brush + (strk_index * jump))
	time.sleep(0.2)
	pg.click()
	time.sleep(0.1)


def top_stroke(): 			# Random Stroke Anywhere on the Top of the Screen
	center = (670, 409) 	# Center Coordinates
	y = 150		# Y Coordinate of the top left of the painting area
	x = random.randint(10, 1351)	# Random Point across the top of the painting area. 
	pg.moveTo(center)
	pg.dragTo(x, y)


def left_stroke():
	center = (670, 409)
	y = random.randint(150, 720)
	x = 10
	pg.moveTo(center)
	pg.dragTo(x, y)


def bottom_stroke():
	center = (670, 409)
	y = 720
	x = random.randint(10, 1351)
	pg.moveTo(center)
	pg.dragTo(x, y)


def right_stroke():
	center = (670, 409)
	y = random.randint(150, 720)
	x = 1350
	pg.moveTo(center)
	pg.dragTo(x, y)


def complete_stroke(): 	# One Complete Circle of Strokes
	top_stroke()
	left_stroke()
	bottom_stroke()
	right_stroke()


def art(strokes): 	# Final Function
	# Select random Color
	# Select random Brush Size
	# Strokes all sides of the screen
	for x in range(strokes):
		select_color_upper(random.randint(1, 10))
		select_brush(random.randint(1, 4))
		complete_stroke()

		select_color_lower(random.randint(1, 10))
		select_brush(random.randint(1, 4))
		complete_stroke()


if __name__ == '__main__':
	rounds = int(input())
	art(rounds)
