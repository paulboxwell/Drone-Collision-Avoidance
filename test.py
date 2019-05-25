#!/usr/bin/python
import random

def Initialise_Arena(Arena_Size):
    #Define Arena
    Arena = []
    for y in range(0,Arena_Size):
        row = []
        for x in range(0,Arena_Size):
            row.append(" ")
        Arena.append(row)
    return Arena

def Add_Route_To_Arena(Route, Arena):
    #Add Route to Arena
    count = 0
    for waypoint in Route:
        Arena[waypoint[1]][waypoint[0]] = str(count)
        count += 1

def Print_Arena(Arena):
    # Print Arena

    #Top Row
    output = "+-"
    for i in Arena[0]:
        output += "---"
    output += "-+"
    output += "\n"
    #Middle Rows
    for row in Arena:
        output += "| "
        for p in row:
            output += " "+p[0]+" "
        output += " |"
        output += "\n"
    #Bottom Rows
    output += "+-"
    for i in Arena[0]:
        output += "---"
    output += "-+"
    print(output)

#Define Route

Route = [(0,0)] # (x,y)


    

end = False
while(end == False):
    input("\nEnter for next frame")
    most_resent = Route[len(Route)-1]
    if most_resent[0] == 9 and most_resent[1] == 9:
        end = True
    elif most_resent[0] == 9:
        Route.append((most_resent[0],most_resent[1]+1))
    elif most_resent[1] == 9:
        Route.append((most_resent[0] + 1,most_resent[1]))
    elif random.random() > 0.5:
        Route.append((most_resent[0],most_resent[1] + 1))
    else:
        Route.append((most_resent[0] + 1,most_resent[1]))
    Arena = Initialise_Arena(10)
    Add_Route_To_Arena(Route, Arena)
    Print_Arena(Arena)
print("Made it to the end in:" + str(len(Route)))
input()