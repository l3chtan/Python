#!/usr/bin/python3.4

import copy
import time
import sys
import curses

stdscr = curses.initscr()

width = 10
height = 10

cur_gen = [["." for x in range(width)] for x in range(height)]
next_gen = [["." for x in range(width)] for x in range(height)]
tmp = ["." for x in range(9)]

			
def setPix():

	for i in range(height):
		for j in range(width):
			tmp[4] = cur_gen[i][j]
			if i < height-1:
				tmp[7] = cur_gen[i+1][j]
				if (j < width-1):
					tmp[5] = cur_gen[i][j+1]
					tmp[8] = cur_gen[i+1][j+1]
				if j > 0:
					tmp[3] = cur_gen[i][j-1]
					tmp[6] = cur_gen[i+1][j-1]
			if i > 0:
				tmp[1] = cur_gen[i-1][j]
				if (j < width-1):
					tmp[2] = cur_gen[i-1][j+1]
				if j > 0:
					tmp[0] = cur_gen[i-1][j-1]
			next_gen[i][j] = getNewGen()


def getNewGen():

	cnt = 0
	for i in tmp:
		if i == "#":
			cnt += 1
	if tmp[4] == "." and cnt == 3:
		tmp[4] = "#"
	elif tmp[4] == "#":
		if cnt < 3 or cnt > 4:
			tmp[4] = "."

	return tmp[4]

def set_start(u,v,x,y):
	
	for i in range(u, v):
		for j in range(x, y):
			cur_gen[i][j] = "#"	


if __name__ == '__main__':

	set_start(7,9,3,6)
	set_start(1,6,5,7)
	set_start(3,6,1,2)
	set_start(6,9,5,7)

	while True:
#		time.sleep(1)
#		sys.stdout.write("\r%s%%" % cur_gen[0])
#		sys.stdout.write("\r%s%%" % cur_gen[1])
#		sys.stdout.write("\r%s%%" % cur_gen[2])
#		sys.stdout.write("\r%s%%" % cur_gen[3])
#		sys.stdout.write("\r%s%%" % cur_gen[4])
#		sys.stdout.write("\r%s%%" % cur_gen[5])
#		sys.stdout.write("\r%s%%" % cur_gen[6])
#		sys.stdout.write("\r%s%%" % cur_gen[7])
#		sys.stdout.write("\r%s%%" % cur_gen[8])
#		sys.stdout.write("\r%s%%" % cur_gen[9])
#		sys.stdout.flush()
#		print("---------------------------------------------------------------------")
		setPix();
		cur_gen = copy.deepcopy(next_gen)
