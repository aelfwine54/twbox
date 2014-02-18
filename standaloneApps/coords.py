# -*- coding: utf-8 -*-
#!/usr/bin/python

"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
import Tkinter as tk
import pyperclip as clipboard


class Interface(tk.Frame):

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        # On crée une fenêtre, racine de notre interface
        fenetre.title('Coord')
        self.initHaut(fenetre)
        self.initBas(fenetre)
        

    def initHaut(self,fenetre):
        self.cadreHaut = tk.Frame(fenetre, width=768, height=350, borderwidth=1, background = 'yellow')
        self.cadreHaut.pack(fill=tk.BOTH)

        self.champ_label = tk.Label(self.cadreHaut, text="Entrer les coordonnees ici")
        self.champ_label.pack()


        self.userInput = tk.Text(self.cadreHaut, width=60, height=20)
        self.userInput.pack(padx=5, pady=5)

        self.convertBtn = tk.Button(self.cadreHaut, text='To BBcode', command=self.toBBcode)
        self.convertBtn.pack()

    def initBas(self,fenetre):
        self.cadreBas = tk.Frame(fenetre, height=350, borderwidth=1,background='red')
        self.cadreBas.pack(fill=tk.BOTH)

        self.answer = tk.Text(self.cadreBas, width=60, height=20)
        self.answer.pack(padx=5, pady=5)
        self.answer.config(state=tk.DISABLED)

        self.clipboardBtn = tk.Button(self.cadreBas, text='To clipboard', command=self.toClipboard)
        self.clipboardBtn.pack()

    def toBBcode(self):
        texte = self.userInput.get(1.0, tk.END)

        self.answer.config(state=tk.NORMAL)

        self.answer.delete(1.0, tk.END)

        for line in set(w for w in texte.split('\n') if len(w) >=2):
            if len(line) == 6:
                self.answer.insert(tk.END, '[coord]')
                self.answer.insert(tk.END, line[:3])
                self.answer.insert(tk.END, "|")
                self.answer.insert(tk.END, line[:3])
                self.answer.insert(tk.END, '[/coord]')
            else:
                self.answer.insert(tk.END, '[coord]')
                self.answer.insert(tk.END, line)
                self.answer.insert(tk.END, '[/coord]')

            self.answer.insert(tk.END, '\n')
        self.answer.config(state=tk.DISABLED)

    def toClipboard(self):
        texte = self.answer.get(1.0, tk.END)
        clipboard.copy(texte)

        



def main():
    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetre = tk.Tk()
    interface = Interface(fenetre)

    interface.mainloop()
    interface.destroy()

if __name__ == "__main__":
    main()