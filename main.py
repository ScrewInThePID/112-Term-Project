from cmu_112_graphics import *
from Notes import *
from Player import *
from Map import *

def appStarted(app):
    ##app.map will be a list of notes generated by the map class
    app.map = Map(app, 20, 2, 1)
    app.notesMap = app.map.notesMap
    app.player = Player()
    app.time = 0


def timerFired(app):
    app.time += 1
    #toggleSide(app)
    for note in app.notesMap:
        #Updates the position of each note
        note.updateNotePos(app.time)
        time = app.time
        score = 0

        #Special scoring method for Slider Note
        if type(note) == Slider:
            for node in note.scoringNodes:
                score = node.scoreNote(app.player.getInputs(), app.time)
        
        #Special scoring method for Down, we pass in old inputs too
        elif type(note) == Down:
            score = note.scoreNote(app.player.getInputs(), time, app.player.oldInputs)

        #Default scoring method
        score = note.scoreNote(app.player.getInputs(), app.time)
        
        #At the end of the if chain, updat the scor
        app.player.updateScore(score)
    app.player.updateOldInputs(app.player.inputs)


def keyPressed(app, event):
    app.player.holdKey(event)
    if event.key == "j":
        print(app.map.notesMap[1].scoringNodes)
def keyReleased(app, event):
    app.player.releaseKey(event)

def redrawAll(app, canvas):
    app.map.drawGame(canvas)
    app.player.drawScore(canvas)
    app.player.drawInputs(canvas, app.height, app.map.lBorder, app.map.cellWidth)

runApp(width=500, height=500)
