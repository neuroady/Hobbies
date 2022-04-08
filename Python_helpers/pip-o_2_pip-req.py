#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file converts the `pip list -o > pip_o.txt` file into pip requirements file which updates all your pip packages via
`pip install -r ./update_pip_requirements.txt`.
Note that when you run the update command there will be dependency conflicts which you will have to resolve manually. 
One way to do that is by commenting out the update of packages which are causing the conflict.
For example: if the update (installation) ipython==8.0.2 is causing a conflict because some other library wants 
ipython<8, you can choose to not update ipython to 8.0.2. This can be done by commenting out the ipython line in the
`update_pip_requirements.txt` file like : # ipython==8.0.2

Check this documentation for more info: https://pip.pypa.io/en/latest/reference/requirements-file-format/

Feel free to modify this script for your purposes. 
Cheers!

Created on Fri Apr  8 10:16:50 2022

@author: neuroady
"""

import os

## get the file
path_o_txt = os.getcwd()+"/pip_o.txt"

f = open(path_o_txt, "r")
text = f.read()
f.close()

## some nifty string manipulation
text = text.split("\n")
text = [tt.split() for tt in text]
text = text[2:-1]
text = [ text[ii][0]+"=="+text[ii][2]+"\n" for ii, tt in enumerate(text) ]

out_text = ''
for tt in text:
    out_text = out_text + tt

## export the update requirements file
out_text = out_text.encode("utf-8")
with open(path_o_txt.rpartition("/")[0]+"/"+"update_pip_requirements.txt", "wb") as f:
     f.write(out_text)
