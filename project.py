import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from hangman import Ui_MainWindow
from datastrore import Datastore

class MainWindow:
    def __init__(self):
# to initialize the main window

        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

# --- initialize the program ---

        self.data = Datastore()
        self.word = ""
        self.guessedWord = []
        self.wrong = 0

# ---- initialize UI ---

        self.chose_word()
        self.display_guess()
        self.display_pictures()
        self.buttons()
        if (self.wrong > 7):
            self.new_word()

# to show the main window

    def show(self):

        self.main_win.show()

#---- generate the word to be guessed ----#

    def chose_word(self):

        self.word = self.data.get_word()
        self.guessedWord = ["_"] * len(self.word)
        self.index = self.data.get_index()
        self.ui.guess.setText(self.index)
        print(self.word)

# -- display the guessed word on the UI --
    def display_guess(self):

        self.display = ""
        for character in self.guessedWord:
            self.display = self.display + character + " "
        self.ui.guessLbl.setText(self.display)  

# -- display the picture --

    def display_pictures(self):
        #self.value = 1
        filename = (f"icons\{self.wrong}.png")
        picture = QPixmap(filename)
        self.ui.label_2.setPixmap(picture)
        self.ui.label_2.setScaledContents(True)

# -- write the function of each button --

    def buttons(self):
       
        self.ui.HintLbl.clicked.connect(lambda : self.new_word())
        self.ui.Abtn.clicked.connect(lambda : self.letter(self.ui.Abtn))
        self.ui.Bbtn.clicked.connect(lambda : self.letter(self.ui.Bbtn))
        self.ui.Cbtn.clicked.connect(lambda : self.letter(self.ui.Cbtn))
        self.ui.Dbtn.clicked.connect(lambda : self.letter(self.ui.Dbtn))
        self.ui.Ebtn.clicked.connect(lambda : self.letter(self.ui.Ebtn))
        self.ui.Fbtn.clicked.connect(lambda : self.letter(self.ui.Fbtn))
        self.ui.Gbtn.clicked.connect(lambda : self.letter(self.ui.Gbtn))
        self.ui.Hbtn.clicked.connect(lambda : self.letter(self.ui.Hbtn))
        self.ui.Ibtn.clicked.connect(lambda : self.letter(self.ui.Ibtn))
        self.ui.Jbtn.clicked.connect(lambda : self.letter(self.ui.Jbtn))
        self.ui.Kbtn.clicked.connect(lambda : self.letter(self.ui.Kbtn))
        self.ui.Lbtn.clicked.connect(lambda : self.letter(self.ui.Lbtn))
        self.ui.Mbtn.clicked.connect(lambda : self.letter(self.ui.Mbtn))
        self.ui.Nbtn.clicked.connect(lambda : self.letter(self.ui.Nbtn))
        self.ui.Obtn.clicked.connect(lambda : self.letter(self.ui.Obtn))
        self.ui.Pbtn.clicked.connect(lambda : self.letter(self.ui.Pbtn))
        self.ui.Qbtn.clicked.connect(lambda : self.letter(self.ui.Qbtn))
        self.ui.Rbtn.clicked.connect(lambda : self.letter(self.ui.Rbtn))
        self.ui.Sbtn.clicked.connect(lambda : self.letter(self.ui.Sbtn))
        self.ui.Tbtn.clicked.connect(lambda : self.letter(self.ui.Tbtn))
        self.ui.Ubtn.clicked.connect(lambda : self.letter(self.ui.Ubtn))
        self.ui.Vbtn.clicked.connect(lambda : self.letter(self.ui.Vbtn))
        self.ui.Wbtn.clicked.connect(lambda : self.letter(self.ui.Wbtn))
        self.ui.Xbtn.clicked.connect(lambda : self.letter(self.ui.Xbtn))
        self.ui.Ybtn.clicked.connect(lambda : self.letter(self.ui.Ybtn))
        self.ui.Zbtn.clicked.connect(lambda : self.letter(self.ui.Zbtn))

        pass
# -- letter button action --

    def letter(self,button):

        self.guess = button.text().lower()
        print(self.guess)

# -- disable button after click --

        button.setEnabled(False)

# -- check if letter is in the word --

        if self.guess in self.word:
# -- add guess to the guessed words--

            for index , letter in enumerate(self.word):
                if self.guess == letter:
                    self.guessedWord[index] = self.guess.upper()
            if "_" not in self.guessedWord:
                self.ui.guess.setText("Yaay you WON !!")
                self.enable_buttons(False)

# --- display new guessed word --

            self.display_guess()

        else:
            self.wrong += 1
            self.display_pictures()
        if self.wrong == 7 :
            self.ui.guess.setText(f"The word was {self.word.upper()}")
            self.enable_buttons(False)

# to enable all buttons again
    def enable_buttons(self,val):
        self.ui.Abtn.setEnabled(val)
        self.ui.Bbtn.setEnabled(val)
        self.ui.Cbtn.setEnabled(val)
        self.ui.Dbtn.setEnabled(val)
        self.ui.Ebtn.setEnabled(val)
        self.ui.Fbtn.setEnabled(val)
        self.ui.Gbtn.setEnabled(val)
        self.ui.Hbtn.setEnabled(val)
        self.ui.Ibtn.setEnabled(val)
        self.ui.Jbtn.setEnabled(val)
        self.ui.Kbtn.setEnabled(val)
        self.ui.Lbtn.setEnabled(val)
        self.ui.Mbtn.setEnabled(val)
        self.ui.Nbtn.setEnabled(val)
        self.ui.Obtn.setEnabled(val)
        self.ui.Pbtn.setEnabled(val)
        self.ui.Qbtn.setEnabled(val)
        self.ui.Rbtn.setEnabled(val)
        self.ui.Sbtn.setEnabled(val)
        self.ui.Tbtn.setEnabled(val)
        self.ui.Ubtn.setEnabled(val)
        self.ui.Vbtn.setEnabled(val)
        self.ui.Wbtn.setEnabled(val)
        self.ui.Xbtn.setEnabled(val)
        self.ui.Ybtn.setEnabled(val)
        self.ui.Zbtn.setEnabled(val)

# -- to generate new words over and over again 

    def new_word(self):

        self.chose_word()
        self.display_guess()

# -- reset gui --
        self.wrong = 0
        self.display_pictures()
        self.enable_buttons(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())