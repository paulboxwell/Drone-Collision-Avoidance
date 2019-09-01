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



def Random_Route(Route):
    end = False
    while(end == False):
        most_resent = Route[len(Route)-1]

        x = 0
        y = 0

        if most_resent[0] == 9 and most_resent[1] == 9:
            end = True
        else:
            if most_resent[0] != 9 and random.random() > 0.5:
                x = 1
            if most_resent[1] != 9 and random.random() > 0.5:
                y = 1
            Route.append((most_resent[0] + x,most_resent[1] + y))
    return len(Route)

#Define Route

FirstRoute = [(0,0)] # (x,y)
CurrentBestLenght = Random_Route(FirstRoute)
CurrentBestRoute = FirstRoute

print("NEW COMMIT")

while(True):
    Route = [(0,0)] # (x,y)
    newlength = Random_Route(Route)
    if newlength < CurrentBestLenght:
        CurrentBestLenght = newlength
        CurrentBestRoute = Route


    Arena = Initialise_Arena(10)
    Add_Route_To_Arena(CurrentBestRoute, Arena)
    Print_Arena(Arena)

    input()