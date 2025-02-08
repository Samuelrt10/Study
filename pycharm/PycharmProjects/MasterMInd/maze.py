import os
import readchar
from random import randint

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 20
NUM_OF_MAP_OBJECTS = 10

my_position = [5,3]
tail_length = 0
tail= []
map_objects= []
end_game = False

while len(map_objects) < NUM_OF_MAP_OBJECTS:
    pos_x_obj = randint(0, MAP_WIDTH)
    pos_y_obj = randint(0, MAP_HEIGHT)

    new_object= [pos_x_obj, pos_y_obj]

    if new_object not in map_objects and new_object != my_position:
        map_objects.append(new_object)

while not end_game:

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end= "")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y]== coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw= "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    print("Has muerto!")
                    end_game = True


            print(" {} ".format(char_to_draw), end= "")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    print(direction)

    if direction =="w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        if my_position[POS_Y] < 0:
            my_position[POS_Y] = 19
    elif direction =="s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        if my_position[POS_Y] > 19:
            my_position[POS_Y] = 0
    elif direction =="a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        if my_position[POS_X] < 0:
            my_position[POS_X] = 19
    elif direction =="d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        if my_position[POS_X] > 19:
            my_position[POS_X] = 0
    elif direction =="q":
        end_game = True




    os.system("cls")