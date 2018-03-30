
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
import RaceSelector as rs
import ClassSelector as cs
import Util as u

app = Flask(__name__)

@app.route('/')
def fullRoll():
    arr = u.rollStats()
    raceStr = rs.pickRaceByStats(arr, u.rankStats(arr), u.highestStatIndexes)
    classStr = cs.pickClassByStats(arr, u.rankStats(arr), 0)
    return render_template('fullRoll.html',
                           race=raceStr,
                           charClass=classStr,
                           statStr=arr[0],
                           statDex=arr[1],
                           statCon=arr[2],
                           statInt=arr[3],
                           statWis=arr[4],
                           statCha=arr[5])

@app.route('/stats')
def justStats():
    arr = u.rollStats()
    return render_template('justStats.html',
                           statStr=arr[0],
                           statDex=arr[1],
                           statCon=arr[2],
                           statInt=arr[3],
                           statWis=arr[4],
                           statCha=arr[5])