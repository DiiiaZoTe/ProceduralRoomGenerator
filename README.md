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

main() countains a sample interactive program (soon)
