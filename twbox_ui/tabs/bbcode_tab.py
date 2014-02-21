# -*- coding: utf-8 -*-
#!/usr/bin/python


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
#import twbox
#from twbox.thirdparty import pyperclip as clipboard
#from twbox.BBcode import *

class BBcodeTab(tk.Frame):

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        # On crée une fenêtre, racine de notre interface
        fenetre.title('Coord')
        self.initHaut(fenetre)
        self.initBas(fenetre)
        self.bbcode = BBcode()
        

    def initHaut(self,fenetre):
        self.cadreHaut = tk.Frame(fenetre, width=768, height=350, borderwidth=1, background = 'yellow')
        self.cadreHaut.pack(fill=tk.BOTH)

        self.champ_label = tk.Label(self.cadreHaut, text="Entrer les coordonnees ici")
        self.champ_label.pack()


        self.userInput = tk.Text(self.cadreHaut, width=60, height=20)
        self.userInput.pack(padx=5, pady=7)

        self.convertBtn = tk.Button(self.cadreHaut, text='To BBcode', command=self.toBBcode)
        self.convertBtn.pack(pady=7)

    def initBas(self,fenetre):
        self.cadreBas = tk.Frame(fenetre, height=350, borderwidth=1,background='red')
        self.cadreBas.pack(fill=tk.BOTH)

        self.answer = tk.Text(self.cadreBas, width=60, height=20)
        self.answer.pack(padx=5, pady=5)
        self.answer.config(state=tk.DISABLED)

        self.clipboardBtn = tk.Button(self.cadreBas, text='To clipboard', command=self.toClipboard)
        self.clipboardBtn.pack(pady=7)

    def toBBcode(self):
        texte = self.userInput.get(1.0, tk.END)

        self.answer.config(state=tk.NORMAL)

        self.answer.delete(1.0, tk.END)

        for line in self.bbcode.surroundByCoord(set(w for w in texte.split('\n') if len(w) >=2)):
            self.answer.insert(tk.END, line)
            self.answer.insert(tk.END, '\n')
        self.answer.config(state=tk.DISABLED)

    def toClipboard(self):
        texte = self.answer.get(1.0, tk.END)
        clipboard.copy(texte.strip())