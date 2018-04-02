import numpy as np
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from PIL import Image

weapons = pd.read_csv('./items/wep.csv',sep=';',names=['Item','Price', 'Currency','Weight in lb','Weight in kg'])

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def home():
  if 'None' in str(type(request.form.get('maps'))):
    img = './static/DnDStarterSet/StarterSet_CragmawHideout_Player.jpg'
  else:
    img = './static/DnDStarterSet/' + str(request.form.get('maps'))
  if 'None' in str(type(request.form.get('tables'))):
    table = weapons.to_html()
  else:
    table = pd.read_csv(str(request.form.get('tables'))).to_html()
  im = Image.open(img)
  width, height = im.size
  return render_template('DnD.html',img=img,
                                    height = height/5,
                                    width  = width/5,
                                    table = table)
   
  
if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=True,host='0.0.0.0', port=4000)


