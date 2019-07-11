#!/usr/bin/python
import random

# Room class
# int roomNumber : when was this room generated (debug purpose mostly)
# int row : the room knows the row from the map in which it is
# int column : the room knows the column from the map in which it is
# 4 int: top, bottom, left, right:
#   - 0 if no room in that direction
#   - 1 if room in that direction
#   - -1 if no possible room in that direction
class Room:
    def __init__(self, roomNumber,row,column,top=0,bottom=0,left=0,right=0):
        self.roomNumber = roomNumber
        self.row = row
        self.column = column
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

# Map class
# int height : number of rows of the map generated
# int width : number of columns of the map generated
# Room[] : array that stores the rooms generated
#          - None if no room at that specific row column
# int roomsCount : random number of rooms to generate (0 to max possible which is height * width)
class Map:
    def __init__(self,height = 4, width = 4):
        random.seed() # takes system time by default
        if height < 1: height = 1
        if width < 1: width = 1
        self.height = height
        self.width = width
        self.roomArray = [[None for i in range(self.width)] for j in range(self.height)]
        self.roomsCount = random.randint(1,self.height * self.width)
        self.generateRooms()

    # generates an entire new map
    # can be of a different height and width possibly
    def generateNewMap(self,height=None,width=None):
        if height != None:
            self.height = height
        if width != None:
            self.width = width
        self.roomArray = [[None for i in range(self.width)] for j in range(self.height)]
        self.roomsCount = random.randint(1, self.height * self.width - 1)
        self.generateRooms()

    # generates new rooms for the current width and height
    # according to the roomsCount number
    def generateRooms(self):
        # using a temp array to generate rooms, since room is an
        # object and they are mutable, we can apply changes to
        # rooms in self.roomArray within the tmpRoomList rooms
        # procedure:
        #   - generate first room
        #   - generate rooms until we got count:
        #       1) pick a random room we already generated
        #       2) pick a direction from this room
        #       3) if direction does not go out of map or there is not
        #          already a room in that direction, then create a room
        #       4) apply door to picked room and new room

        tmpRoomList = [] 
        # random starting room
        row = random.randint(0,self.height-1)
        column = random.randint(0,self.width-1)
        firstRoom = Room(1,row,column)
        self.checkAroundRoom(firstRoom)
        self.roomArray[row][column] = firstRoom
        tmpRoomList.append(firstRoom)
        # generate new room until we did not reach desired number
        while len(tmpRoomList) < self.roomsCount:
            fromRoom = 1
            roomNumber = len(tmpRoomList)
            if roomNumber + 1 != 1:
                fromRoom = random.randint(0, roomNumber-1) # index room from which we go to a direction
                direction = random.randint(1,4) # 1 = top, 2 = bottom, 3 = left, 4 = right
                if direction == 1 and tmpRoomList[fromRoom].top == 0: # top
                    r = tmpRoomList[fromRoom].row-1
                    c = tmpRoomList[fromRoom].column
                    if self.roomArray[r][c] == None:
                        newRoom = Room(roomNumber+1, r, c, 0, 1, 0, 0)
                        newRoom.bottom = 1
                        tmpRoomList[fromRoom].top = 1
                        #self.roomArray[tmpRoomList[fromRoom].row][tmpRoomList[fromRoom].column].top = 1
                        self.checkAroundRoom(newRoom)
                        self.roomArray[r][c] = newRoom
                        tmpRoomList.append(newRoom)
                if direction == 2 and tmpRoomList[fromRoom].bottom == 0: # bottom
                    r = tmpRoomList[fromRoom].row+1
                    c = tmpRoomList[fromRoom].column
                    if self.roomArray[r][c] == None:
                        newRoom = Room(roomNumber+1, r, c, 1, 0, 0, 0)
                        newRoom.top = 1
                        tmpRoomList[fromRoom].bottom = 1
                        self.checkAroundRoom(newRoom)
                        self.roomArray[r][c] = newRoom
                        tmpRoomList.append(newRoom)
                if direction == 3 and tmpRoomList[fromRoom].left == 0: # left
                    r = tmpRoomList[fromRoom].row
                    c = tmpRoomList[fromRoom].column-1
                    if self.roomArray[r][c] == None:
                        newRoom = Room(roomNumber+1, r, c, 0, 0, 0 , 1)
                        newRoom.right = 1
                        tmpRoomList[fromRoom].left = 1
                        self.checkAroundRoom(newRoom)
                        self.roomArray[r][c] = newRoom
                        tmpRoomList.append(newRoom)
                if direction == 4 and tmpRoomList[fromRoom].right == 0: # right
                    r = tmpRoomList[fromRoom].row
                    c = tmpRoomList[fromRoom].column+1
                    if self.roomArray[r][c] == None:
                        newRoom = Room(roomNumber+1, r, c, 0, 0, 1, 0)
                        tmpRoomList[fromRoom].right = 1
                        self.checkAroundRoom(newRoom)
                        self.roomArray[r][c] = newRoom
                        tmpRoomList.append(newRoom)
    
    # helper function that check around a given room
    # and update its boundaries if any
    def checkAroundRoom(self,room):
        if room.row == 0:
            room.top = -1
        if room.row == self.height-1:
            room.bottom = -1
        if room.column == 0:
            room.left = -1
        if room.column == self.width-1:
            room.right = -1
    
    # draw the entire map
    # 
    def drawMap(self):
        print()
        """ Simple drawing version
        for i in range(0,self.height):
            for j in range(0,self.width):
                if self.roomArray[i][j] == None:
                    print(" * ",end="")
                else:
                    print(" " + str(self.roomArray[i][j].roomNumber) + " ", end="")
            print()
        """
    # a room is gonna be 8 characters wide
    # and 4 lines tall
    # top line for top
    # bottom line for bottom
    # 2 middle lines for left and right but also bottom if there is one         
    #
    # top room :
    #  _||_  
    # |    | 
    # |____| 
    #        
    # bottom room : 
    #  ____  
    # |    | 
    # |_  _| 
    #   ||   
    #
    # left room : 
    #  ____  
    #==    | 
    #==____| 
    #        
    # right room : 
    #  ____  
    # |    ==
    # |____==
    #        
        for i in range(0,self.height):
            for line in range(4):
                for j in range(0,self.width):
                    if self.roomArray[i][j] == None:
                        print("        ", end='')
                    else:
                        # draw top part
                        if line == 0:
                            if self.roomArray[i][j].top == 1:
                                print("  _||_  ",end='')
                            else:
                                print("  ____  ",end='')
                        # draw left right part and bottom
                        # string building by checking left, bottom(line 2 only) then right
                        if line == 1 or line == 2:
                            string = ""
                            if self.roomArray[i][j].left == 1:
                                string += "=="
                            else:
                                string += " |"
                            if self.roomArray[i][j].bottom == 1 and line == 2:
                                string += "_  _"
                            elif line == 1:
                                string += "    "
                            else:
                                string += "____"
                            if self.roomArray[i][j].right == 1:
                                string += "=="
                            else:
                                string += "| "
                            print(string, end='')
                        # draw bottom part
                        if line == 3:
                            if self.roomArray[i][j].bottom == 1:
                                print("   ||   ",end='')
                            else:
                                print("        ",end='')
                print() # newline

def main():
    map = Map()
    map.drawMap()

if __name__ == "__main__":
    main()