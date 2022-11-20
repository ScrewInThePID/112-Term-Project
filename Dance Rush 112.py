from cmu_112_graphics import *
from Node import Node
from Notes import Notes
from Slider import Slider
from Player import Player

def appStarted(app):
    ##app.map will be a list of notes generated by the map class
    app.map = [Node(100, 20, 15, 20), Slider(200, 20, 5, 5, 10)]
    app.player = Player()
    app.time = 0
    app.x0 = 0
    app.x1 = 0


def timerFired(app):
    app.time += 1
    app.pressed = False

    for note in app.map:
        #Updates the position of each note
        note.updateNotePos(app.time)
        
        #Scores the note if the time == the note's game time
        if app.time == note.scoreTime:
            note.scoreNote

    #Testing for key held down
    print(app.player.inputs) #prints out key value  
    app.player.setDefaultInput()
    print(app.player.inputs) #prints out default value

def keyPressed(app, event):
    app.player.updatePlayerInputs(event)

def redrawAll(app, canvas):
    for note in app.map:
        note.drawNote(canvas)

runApp(width=1000, height=500)
