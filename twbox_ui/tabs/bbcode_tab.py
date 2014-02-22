# -*- coding: utf-8 -*-

# Copyright 2014 Frederic Bergeron. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
# 
#    1. Redistributions of source code must retain the above copyright notice, this list of
#       conditions and the following disclaimer.
# 
#    2. Redistributions in binary form must reproduce the above copyright notice, this list
#       of conditions and the following disclaimer in the documentation and/or other materials
#       provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY Frederic Bergeron ``AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL Frederic Bergeron OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# The views and conclusions contained in the software and documentation are those of the
# authors and should not be interpreted as representing official policies, either expressed
# or implied, of Frederic Bergeron.

import Tkinter as tk
import sys
import os
root =  os.getenv('TWBOX_ROOT')
#sys.path.append(root+'/twbox_ui')
from thirdparty import pyperclip as clipboard

sys.path.append(root)
import utils.BBcode as BBcode

class BBcodeTab(tk.Frame):

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        # On crée une fenêtre, racine de notre interface
        fenetre.title('BBcode')
        self.initInput(fenetre)
        self.initOutput(fenetre)
        self.initRightPanel(fenetre)
        self.bbcode = BBcode.BBcode()
        

    def initInput(self,parent):
        self.cadreHaut = tk.Frame(parent, width=768, height=350, borderwidth=1, background = 'yellow')
        self.cadreHaut.grid(row=0,column=0)

        self.champ_label = tk.Label(self.cadreHaut, text="Plain text here")
        self.champ_label.grid()

        self.userInput = tk.Text(self.cadreHaut, width=60, height=20)
        self.userInput.grid(padx=5, pady=7)
        self.userInput.bind("<FocusIn>", self.inputFocusIn)
        self.userInput.insert(tk.END, 'Plain text here')



    def initOutput(self,parent):
        self.cadreBas = tk.Frame(parent, height=350, borderwidth=1,background='red')
        self.cadreBas.grid(row=1,column=0)

        self.answer = tk.Text(self.cadreBas, width=60, height=20)
        self.answer.grid(padx=5, pady=5)
        self.answer.config(state=tk.DISABLED)

        self.clipboardBtn = tk.Button(self.cadreBas, text='To clipboard', command=self.toClipboard)
        self.clipboardBtn.grid(pady=7)

    def initRightPanel(self,parent):
        self.cadreDroit = tk.Frame(parent, width=100, borderwidth=1,background='pink')
        self.cadreDroit.grid(row=0,rowspan=2,column=1, sticky=tk.W+tk.E+tk.N+tk.S,ipadx=5)

        centeredFrame = tk.Frame(self.cadreDroit,bg='pink')
        centeredFrame.place(anchor="c", relx=.5, rely=.48)

        modes = [
                ("Coord", "coord"),
                ("Player", "player"),
                ("Ally ", "ally"),
                ("Report", "report"),
                ("Report Display", "report_display")
            ]
            
        self.bbcodeMode = tk.StringVar()
        self.bbcodeMode.set("L") # initialize
        r=0    
        for text, mode in modes:
            b = tk.Radiobutton(centeredFrame, text=text, variable=self.bbcodeMode, value=mode, indicatoron=0, command=self.toBBcode)
            b.grid(row=r, sticky=tk.W+tk.E+tk.N+tk.S, pady=3)
            r+=1


    def toBBcode(self):
        texte = self.userInput.get(1.0, tk.END)

        self.answer.config(state=tk.NORMAL)
        self.answer.delete(1.0, tk.END)

        coded = []
        value = self.bbcodeMode.get();

        if value == 'coord':
            coded = self.bbcode.surroundByCoord(set(w for w in texte.split('\n') if len(w) >=2))
        elif value == 'player':
            coded = self.bbcode.surroundByPlayer(set(w for w in texte.split('\n') if len(w) >=2))
        elif value == 'ally':
            coded = self.bbcode.surroundByAlly(set(w for w in texte.split('\n') if len(w) >=2))
        elif value == 'report':
            coded = self.bbcode.surroundByReport(set(w for w in texte.split('\n') if len(w) >=2))
        elif value == 'report_display':
            coded = self.bbcode.surroundByReportDisplay(set(w for w in texte.split('\n') if len(w) >=2))

        for line in coded:
            self.answer.insert(tk.END, line)
            self.answer.insert(tk.END, '\n')
        self.answer.config(state=tk.DISABLED)

    def toClipboard(self):
        texte = self.answer.get(1.0, tk.END)
        clipboard.copy(texte.strip())

    def inputFocusIn(self, event):
        texte = self.userInput.get(1.0, tk.END).strip()
        if (texte == 'Plain text here'):
            self.userInput.delete(1.0, tk.END)
