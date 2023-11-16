from flask import Flask, request, render_template, send_from_directory, session, flash, redirect, url_for, jsonify  # Añadir jsonify
from markupsafe import Markup  # Agrega esta línea
import os
import mysql.connector
import plotly
from plotly.graph_objs import Scatter, Layout
import logging
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)
app.secret_key = "<g\x93E\xf3\xc6\xb8\xc4\x87\xff\xf6\x0fxD\x91\x13\x9e\xfe1+%\xa3\x83\xb6"

def connectToMySql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="yourpassword",
        database="weatherstationesp32"
    )

    return mydb

def saveWeatherData(date, temperature, altitud, pressure):
    result = False
    mydb = connectToMySql()
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `indoorweatherdataesp32`(`Date`, `Temperature`, `Altitude`, `Pressure`) VALUES (%s,%s,%s,%s)"
        val = (date, temperature, altitud, pressure)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        if mycursor.rowcount > 0:
            result = True
        mydb.close()
    except:
        mydb.close()
    return result

def getLatestWeatherData():
    mydb = connectToMySql()
    try:
        mycursor = mydb.cursor()
        query = "SELECT * FROM `indoorweatherdataesp32` WHERE 1 ORDER BY Date DESC LIMIT 1"
        mycursor.execute(query)
        result = mycursor.fetchall()
        mydb.close()
    except:
        mydb.close()
        result = False
    return result

def checkSystemOn():
    systemOn = False
    IST = pytz.timezone('America/Bogota')
    datetime_utc = datetime.now(IST)
    #print("Date & Time in UTC : ", datetime_utc.strftime('%Y:%m:%d %H:%M:%S'))
    latestData = getLatestWeatherData()
    lastDate = latestData[0][0]
    #print("Latest Date : ", lastDate.strftime('%Y:%m:%d %H:%M:%S'))
    currentDateTime = datetime_utc.replace(tzinfo=None)
    lastDateTime = lastDate.replace(tzinfo=None)
    diffBetweenDates = currentDateTime-lastDateTime
    #print("Difference: ", diffBetweenDates)
    if diffBetweenDates > timedelta(minutes=15):
        systemOn = False
    else:
        systemOn = True
    return systemOn

def getSpecificData(dataToSelect):
    mydb = connectToMySql()
    mycursor = mydb.cursor()
    query = "SELECT Date ,"+dataToSelect+" FROM `indoorweatherdataesp32`"
    mycursor.execute(query)
    result = mycursor.fetchall()
    mydb.close()
    print(result)
    return result

def createPlot(datas, dataType):
    if dataType == 'Temperature':
        plotColor = '#ff9900'
        plotTitle = 'Temperatura'
    elif dataType == 'Altitude':
        plotColor = '#029400'
        plotTitle = 'Altitud'
    else:
        plotColor = '#70bfff'
        plotTitle ='Presión'

    dataDictionary = {
        "X": [],
        "Y": []
    }
    for x in datas:
        dataDictionary["X"].append(x[0])
        dataDictionary["Y"].append(x[1])
    plot = plotly.offline.plot({
        "data": [Scatter(x=dataDictionary["X"], y=dataDictionary["Y"], line=dict(color=plotColor, width=2))],
        "layout": Layout(title=plotTitle,width=1200, height=550, margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ))
    }, output_type='div'
    )

    return plot

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')    

@app.route('/home')
def homePage():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        #get latest sensor datas
        latestData = getLatestWeatherData()
        lastDataTime = latestData[0][0]
        lastTemperature = latestData[0][1]
        lastAltitude = latestData[0][2]
        lastPressure = latestData[0][3]
        #get data to build temperatures plot
        temperatures = getSpecificData("Temperature")
        temperaturesPlot = createPlot(temperatures, "Temperature")
        temperaturesPlotHtml = Markup(temperaturesPlot)
        #get data to build humidity plot
        altitude = getSpecificData("Altitude")
        altitudePlot = createPlot(altitude, "Altitude")
        altitudePlotHtml = Markup(altitudePlot)
        #get data to build atmospheric pressure plot
        pressure = getSpecificData("Pressure")
        pressurePlot = createPlot(pressure, "Pressure")
        pressurePlotHtml = Markup(pressurePlot)

        systemOn = checkSystemOn()

        return render_template("home.html", lastDataTime=lastDataTime, lastTemperature=lastTemperature, lastAltitude=lastAltitude, lastPressure=lastPressure, temperaturePlot=temperaturesPlotHtml,altitudePlot=altitudePlotHtml, pressurePlot=pressurePlotHtml, systemOn=systemOn)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'esp8266' and request.form['username'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('homePage'))
        else:
            flash('Wrong username or password!')
    return render_template('login.html')


@app.route("/logout", methods=['POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

#example query: /postWeatherData?Temp=26.3&Alt=23.7&Pres=3455.8&Date=2021-05-05&Time=12:39
# ejemplo de URL: http://127.0.0.1:5000/postWeatherData?Temp=26.3&Alt=23.7&Pres=3455.8&Date=2021-05-05&Time=12:39
@app.route('/postWeatherData', methods=['GET', 'POST'])
def postWeatherData():
    if request.method == 'GET':
        temperature = request.args.get('Temp')
        altitude = request.args.get('Alt')
        pressure = request.args.get('Pres')
        date = request.args.get('Date')
        time = request.args.get('Time')
        print("New Weather Data. T:" + temperature + " H:" + altitude + " P:" + pressure + " Date:" + date + " Time:" + time)
        datetime = date + " " + time
        if float(temperature) > -14 and float(temperature) < 46 and float(altitude) >4 and float(altitude) < 71:
            insertResult = saveWeatherData(temperature, altitude, pressure, datetime)
            print("postWeatherData result: " + str(insertResult))
        else:
            logging.info("Weather data values out of range (esp temperature sensor error). Weather Data received:  T:" + temperature + " H:" + altitude + " P:" + pressure + " Date:" + date + " Time:" + time )
        # return redirect('/')
    return 'ok'

if __name__ == '__main__':
    app.env = "debug"
    app.debug = True
    app.run()
