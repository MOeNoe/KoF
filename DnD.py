import numpy as np
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from PIL import Image

# Loads weapons list
weapons = pd.read_csv('./items/wep.csv',
                      sep=';',
                      names=['Category','Item','Price', 'Currency','Weight in lb','Weight in kg'])
weapons = pd.pivot_table(weapons,index=['Category','Item','Currency'],values=['Price', 'Currency','Weight in lb','Weight in kg'])
# Starts flask wep app
app = Flask(__name__)

# Sets root and allows for GET and POST, REST methods
@app.route('/', methods=['GET', 'POST'])

# Main Loop
def home():
  # Switches between maps
  if 'None' in str(type(request.form.get('maps'))):
    img = './static/DnDStarterSet/StarterSet_CragmawHideout_Player.jpg'
  else:
    img = './static/DnDStarterSet/' + str(request.form.get('maps'))

  # Switches between playes inventory
  if 'None' in str(type(request.form.get('tables'))):
    table = weapons.to_html()
  elif 'wep' in str(request.form.get('tables')):
    table = weapons.to_html()
  else:
    table = pd.read_csv('./players/'+str(request.form.get('tables')) + '.csv',sep=';').to_html()


  # Loads image dimensions
  im = Image.open(img)
  width, height = im.size
  return render_template('DnD.html',img=img,
                                    height = height/5,
                                    width  = width/5,
                                    table = table)
   
# Runs the local webserver here the port can be sepecified,
# and the debugger is turned on or off
if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=True,host='0.0.0.0', port=4000)


