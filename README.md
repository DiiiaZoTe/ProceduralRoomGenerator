# ProceduralRoomGenerator
Python script to generate rooms procedurally + console output

class: - Room
       - Map

How to use: 

    // create a map replacing row and column (default 4 if left blank):
    map = Map(row,column)
    // call the drawing function
    map.drawMap()
    // you can generation a new map, different room number count, for a row/column size (leaving blank will keep previous size):
    map.generateNewMap(row,column)
    map.drawMap()
    // or you can generate a new map for same room number count and same row/column size
    map.generateRooms()
    map.drawMap()
    // you can find the furthest room away from the first room by using
    room, distance = map.findFurthestFromFirst()
    // or you can find the furthest from a specific room (you will need to loop through the map array to get the one you want)
    for i in range(0,map.height):
            for j in range(0,map.width):
                room = map.roomArray[i][j]
                if room != None:
                    furthest, distance = map.findFurthest(room)

main() countains an interactive sample
