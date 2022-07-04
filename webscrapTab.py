# Python programm:  Web scrapping Tables
# Credits / source: https://www.youtube.com/watch?v=ODNMNwgtehk
# Adaptation codes by: Carlos Javier
# need lxml package too ** Attention **
#
# Setting packages
import pandas as pd
import numpy as np
import csv
from flask import Flask, flash, render_template, request


#
app = Flask(__name__)
# 'This is NOT a good practice for Secret_key (just for study purpose only)
app.secret_key = ("YOUDONOTPUTSETSECRETKEYHERE")
player_data=[]

# ==> to HTML , Main rout
@app.route('/', methods=["POST","GET"])
def home():
    return  render_template('index.html')

# Get Player1 Data , Scrapping, return to HTML
@app.route("/player1.html/",methods=["POST","GET"])
def player1():
    url ='https://www.baseball-reference.com/players/s/sotoju01.shtml'
    df = pd.read_html(url)
    df[0].to_csv('player1.csv')
    with open("player1.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[1] == '2022'):
                bavg1 = (round(float(row[18]) * 1000))
                hr1 = row[12]
                hit1 = row[9]
                obp1 = row[19]
                slg1 = row[20]
    player_data = (bavg1, hr1, hit1, obp1 ,slg1)
    return render_template('player1.html', bavg1=bavg1 , hr1=hr1 , hit1=hit1, obp1=obp1, slg1=slg1)

# Get Player2 Data , Scrapping, return to HTML
@app.route("/player2.html/",methods=["POST","GET"])
def player2():
    url ='https://www.baseball-reference.com/players/g/guerrvl02.shtml'
    df = pd.read_html(url)
    df[0].to_csv('player2.csv')
    with open("player2.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[1] == '2022'):
                bavg1 = (round(float(row[18]) * 1000))
                hr1 = row[12]
                hit1 = row[9]
                obp1 = row[19]
                slg1 = row[20]
    player_data = (bavg1, hr1, hit1, obp1 ,slg1)
    return render_template('player2.html', bavg1=bavg1 , hr1=hr1 , hit1=hit1, obp1=obp1, slg1=slg1)

if __name__ == '__main__':
    app.run(debug=True)


# print(,row[9],row[11],row[12],row[17],row[18],row[19])
#print (bavg1,hr1,hit1,(float(obp1)*1000),(float(slg1)*1000))

#g(4),h(8),11hr,12rbi,BA(17),slg18,obs19
# print(df[0])
# Save to CSV file




