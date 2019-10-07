import config
import json
import os
import pymysql
from flask import Flask
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION

mydb = pymysql.connect(
  host=config.MYSQL_URL,
  user=config.MYSQL_USER,
  passwd=config.MYSQL_PW,
  database=config.MYSQL_DB)

mycursor = mydb.cursor()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('insertCorado.html')
    
    @app.route('/search')
    def search():
        return render_template('searchCorado.html')

    @app.route('/getAll')
    def getAll():
        SELECT = f"SELECT * FROM {config.MYSQL_TABLE}"
        results = dict()
        mycursor.execute(SELECT)
        myresult = mycursor.fetchall()
        for  x in myresult:
            print(x)
            temp_results={str(x[0]):{'name':x[1], 'gamertag':x[2], 'phone':x[3], 'discord':x[4]}}
            results.update(temp_results)
        return results
    
    @app.route('/insertResults', methods=['POST'])
    def insertResults():
        print(request.form)
        INSERT = f"INSERT INTO `{config.MYSQL_TABLE}`(`NAME`, `GAMERTAG`, `PHONE`, `DISCORD`) VALUES ('{request.form['name']}', '{request.form['gamerTag']}', '{request.form['phone']}', '{request.form['discord']}');"
        print(INSERT)
        mycursor.execute(INSERT)
        mydb.commit()
        return request.form

    @app.route('/searchResults', methods=['POST'])
    def searchResults():
        print(request.form)
        searchSELECT = f"SELECT * FROM {config.MYSQL_TABLE} WHERE lower(NAME) LIKE lower('%{request.form['keyword']}%');"
        print(searchSELECT)
        results = dict()
        mycursor.execute(searchSELECT)
        myresult = mycursor.fetchall()
        for  x in myresult:
            print(x)
            temp_results={str(x[0]):{'name':x[1], 'gamertag':x[2], 'phone':x[3], 'discord':x[4]}}
            results.update(temp_results)
        return results

    return app

if __name__ == '__main__':
  app =create_app()
  app.run(host='0.0.0.0', debug=True, port=80)