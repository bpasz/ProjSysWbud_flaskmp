# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:50:49 2019

@author: bartl
"""
from flask import Flask, render_template, request
import apka
from multiprocessing import Process, Manager

print("nazwa ",__name__)
app = Flask(__name__)

strona="""
<form action="/kreskowka">
  First name:<br>
  <input type="text" name="imie" value="Święty"><br>
  Last name:<br>
  <input type="text" name="nazwisko" value="Mikolaj"><br><br>
  <input type="submit" value="Submit">
</form>
"""

@app.route('/on')
def hello_world():
 #   return render_template('index.html')
     d["state"]=1
     return "ok"

@app.route('/off')
def nowa_kreskowa():
    d["state"]=0
#    print(request.args)
#    print("Imie przekzane w formularzu to:" + request.args.get('imie'))
    return "stop go"
    
    


if __name__ == '__main__':
    manager=Manager()
    d=manager.dict()
    d["state"]=0
    p = Process(target=apka.led, args=(d,))
    print("Proces jest żywy?: ",p.is_alive())
    p.start()
    app.run(debug=False, port=80, host='0.0.0.0')

