import math
import pygame
from random import randrange
import time

height_arr = []
num_rects = 100

width =  750
height = 500
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("BUBBLE SORT ANIMATION")
offset = 3
grey = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
height_arr = [randrange(3, height - offset) for i in range(num_rects)]


def is_sorted(array):
    prev_elt = -math.inf
    for elt in array:
        if prev_elt > elt:
            return False

        prev_elt = elt
    return True


def swap(index1, index2, array):
    temp_elt = array[index1]

    array[index1] = array[index2]
    array[index2] = temp_elt


def bubble_sort(array):
    for index, elt in enumerate(array):
        if is_sorted(array):
            return False

        if index != len(array) - 1:
            nxt_elt = array[index + 1]
            if elt > nxt_elt:
                swap(index, index + 1, array)
    return True


def compare(index1, index2, arr):
	try:
		elt = arr[index1]
		other_elt = arr[index2]
		if elt > other_elt:
			swap(index1, index2, arr)
			compare(index1 + 1, index2 + 1, arr)
	except:
		pass


def insertion_sort(array):
    for index, elt in enumerate(array):
        compare(index, index + 1, array)
    return True


def partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[hi] = array[hi], array[i]
    return i


def quickSort(arr, pairs):
    try:
        lo, hi = pairs.pop(0)
        if lo < hi:
            p = partition(arr, lo, hi)
            pairs.append((lo, p - 1))
            pairs.append((p + 1, hi))
        return True
    except:
        print("DONE!!!!!!!")
        return False


def random_colour():
    min_val = 70
    max_val = 230
    r = randrange(min_val, max_val)
    b = randrange(min_val, max_val)
    g = randrange(min_val, max_val)
    return (r, g, b)


def sketch():
    running = True
    border_width = 2
    rect_width = (width / num_rects)
    max_fps = 10
    sorting = True
    colour_arr = []
    pairs = [(0, len(height_arr) - 1)]
    for i in range(num_rects):
        colour_arr.append(random_colour())

    while running:
        # clock.tick(max_fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                return

        # DRAWING, ANIMATIONS AND SORTING
        screen.fill(grey)

        for index, length in enumerate(height_arr):
            rect_x = index * rect_width
            rect_y = height - length
            pygame.draw.rect(screen, colour_arr[index], (int(rect_x), rect_y, int(rect_width), length))
            pygame.draw.aaline(screen, black, (rect_x, rect_y), (rect_x + rect_width, rect_y))
            pygame.draw.aaline(screen, black, (rect_x, rect_y), (rect_x, height))

        if sorting:
            sorting = quickSort(height_arr, pairs)
            # pygame.time.delay(100)

        pygame.display.update()


if __name__ == '__main__':
    sketch()