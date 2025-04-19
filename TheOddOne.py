from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel
                             ,QWidget,QVBoxLayout,QGridLayout,QHBoxLayout,
                             QGroupBox,QPushButton,QSlider)
from PyQt5.QtGui import QPixmap,QFont, QMovie,QIcon,QColor
from PyQt5.QtCore import Qt, QTimer
import sys
import pygame
import random




class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("The Odd One Game")
        self.setGeometry(0,0,800,450)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,470)
        picture = QPixmap("stockimages/Fantasiereise-fuer-Kinder-Wunderland.jpg")
        self.label.setPixmap(picture)
        self.label.setScaledContents(True)
        self.setFixedSize(800,450)
        self.Icon = QIcon("stockimages/1712197885705-79588672 (1).png")
        self.setWindowIcon(self.Icon)

        timer = QTimer(self)

        self.initUI()
        self.center_Window()

        self.StartAnimation()

        timer.singleShot(10000,self.stopAnimation)   

    #All Gui Related is here
    def initUI(self):
        GameLabel = QLabel("The Odd One",self)
        GameLabel.setFont(QFont("Papyrus",40))
        GameLabel.setGeometry(0,100,800,80)
        GameLabel.setScaledContents(True)
        GameLabel.setStyleSheet("""
                                color:rgb(0,0,0);
                                font-weight:bold;
                                border-radius:10px;       
                                """)
        
        GameLabel.setAlignment(Qt.AlignCenter)

        self.loadingIcon = QMovie("stockimages/loading-ezgif.com-gif-maker.gif")
        LoadingScreenLabel = QLabel(self)
        LoadingScreenLabel.setMovie(self.loadingIcon)
        LoadingScreenLabel.setGeometry(310,180,200,200)

    #loading screen animation control for the gif     
    def StartAnimation(self):
        self.loadingIcon.start()

    def stopAnimation(self):
        self.loadingIcon.stop()

    #for automatic centering of the window
    def center_Window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("The Odd One Game")
        self.setGeometry(0,0,800,450)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,450)
        picture = QPixmap("stockimages/1712197885705-79588672 (1).png")
        self.label.setPixmap(picture)
        self.label.setScaledContents(True)
        self.setFixedSize(800,450)
        self.Icon = QIcon("stockimages/1712197885705-79588672 (1).png")
        self.setWindowIcon(self.Icon)
        
        self.setStyleSheet("""
                            QPushButton{
                            color:white;
                            border-radius:20px;
                           }
                           QPushButton:hover{
                            background-color:rgba(0,0,0,150)
                           
                           }
                            """)

        self.WindowCenter()
        self.initUI()
        self.backgroundMusic()
        
    def WindowCenter(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def initUI(self):
        central_Widget = QWidget()
        self.setCentralWidget(central_Widget)
        outerLayout = QVBoxLayout()
        outerLayout.setAlignment(Qt.AlignCenter)

        MenuBox = QGroupBox()
        MenuLayout = QVBoxLayout()

        MenuBox.setStyleSheet("border:none;")

        GameTitle = QLabel("The Odd One")
        GameTitle.setFont(QFont("Papyrus",30))
        GameTitle.setAlignment(Qt.AlignCenter)
        GameTitle.setStyleSheet("font-weight:bold;")

        StartBtn = QPushButton("Start")
        SettingsBtn = QPushButton("Settings")
        CreditstBtn = QPushButton("Credits")
        ExitBtn = QPushButton("Exit")


        #funtions of the buttons
        ExitBtn.clicked.connect(self.exitButton)
        StartBtn.clicked.connect(self.gamestartButton)
        CreditstBtn.clicked.connect(self.creditButton)
        SettingsBtn.clicked.connect(self.settingsButton)

        StartBtn.setFont(QFont("Papyrus",25))
        SettingsBtn.setFont(QFont("Papyrus",25))
        CreditstBtn.setFont(QFont("Papyrus",25))
        ExitBtn.setFont(QFont("Papyrus",25))

        MenuLayout.addWidget(GameTitle)
        MenuLayout.addWidget(StartBtn)
        MenuLayout.addWidget(SettingsBtn)
        MenuLayout.addWidget(CreditstBtn)
        MenuLayout.addWidget(ExitBtn)
        

        MenuBox.setLayout(MenuLayout)

        MenuBox.setFixedSize(400, 400)
        outerLayout.addWidget(MenuBox,alignment=Qt.AlignCenter)

        #initialize the Vertical layout
        central_Widget.setLayout(outerLayout)

    def gamestartButton(self):
        window.hide()
        GameStartWindow.show()
        GameStartWindow.restartGame()
        
        

    def settingsButton(self):
        window.hide()
        SetingsWindow.show()
        

    def creditButton(self):
        window.hide()
        CreditsWindow.show()

    def exitButton(self):
        window.close()
        
    def backgroundMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Workspace/Mark_Steven/TheOddOneGame/stockMusic/New_Project.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.10)
        


class GamePlay(QWidget):
    
    def __init__(self):
        super().__init__()

       
        self.setWindowTitle("The Odd One Game")
        self.setGeometry(0, 0, 800, 450)
        self.setFixedSize(800, 450)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 800, 470)
        picture = QPixmap("stockimages/Fantasiereise-fuer-Kinder-Wunderland.jpg")
        self.label.setPixmap(picture)
        self.label.setScaledContents(True)

        self.setWindowIcon(QIcon("stockimages/1712197885705-79588672 (1).png"))

        self.WindowCenter()
        self.initUI()
        self.generate_Grid()

    def WindowCenter(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def initUI(self):
        self.gridsize = 2
        self.score = 0
        self.timeLeft = 20
        self.base_color_diff = 30
        self.buttons = []

        fontStyle = QFont("papyrus", 10)

        # Pause Button
        QuitButton= QPushButton("Quit", self)
        QuitButton.setGeometry(700, 20, 50, 50)
        QuitButton.setFont(fontStyle)
        QuitButton.setObjectName("pausebutton")
        QuitButton.setStyleSheet("""
            #pausebutton {
                color: white;
                border-radius: 25px;
                background-color: rgba(0, 0, 0, 155);
                border: 1px solid white;
            }
            #pausebutton:hover {
                background-color: rgba(255, 255, 255, 0);
            }
        """)

        QuitButton.clicked.connect(self.exit_to_main_menu)

        # Restart Button
        self.restartButton = QPushButton("Restart", self)
        self.restartButton.setGeometry(620, 20, 70, 50)
        self.restartButton.setFont(fontStyle)
        self.restartButton.setObjectName("restartbutton")
        self.restartButton.setStyleSheet("""
            #restartbutton {
                color: white;
                border-radius: 25px;
                background-color: rgba(0, 0, 0, 155);
                border: 1px solid white;
            }
            #restartbutton:hover {
                background-color: rgba(255, 255, 255, 0);
            }
        """)
        self.restartButton.clicked.connect(self.restartGame)

        # Layouts
        outerlayout = QVBoxLayout()
        outerlayout.setAlignment(Qt.AlignCenter)
        TimerandScoreLayout = QHBoxLayout()
        self.GameBox = QGroupBox()
        self.GameGrid = QGridLayout()

        self.scoreBoard = QLabel("Score: 0")
        self.scoreBoard.setFont(fontStyle)
        self.scoreBoard.setStyleSheet("""
                                      color:white;
                                      background-color:rgba(0,0,0,180);
                                     
                                      """)
        self.Timer = QLabel(f"Time: {self.timeLeft}")
        self.Timer.setFont(fontStyle)
        self.Timer.setStyleSheet("""
                                 color:white;
                                 background-color:rgba(0,0,0,180);
                                      
                                      """)

        TimerandScoreLayout.addWidget(self.scoreBoard)
        TimerandScoreLayout.addWidget(self.Timer)

        outerlayout.addLayout(TimerandScoreLayout)
        outerlayout.addWidget(self.GameBox)

        self.GameBox.setFixedSize(350, 300)
        self.GameBox.setLayout(self.GameGrid)
        self.GameBox.setStyleSheet("""
            QGroupBox {
                background-color: rgba(0, 0, 0, 155);
                border-radius: 30px;
                border: 2px solid white;
            }
        """)

        self.setLayout(outerlayout)

        self.TimeCounter = QTimer()
        self.TimeCounter.timeout.connect(self.updateTime)
        self.TimeCounter.start(1000)

        # Game Over Message Label
        self.gameOverLabel = QLabel("", self)
        self.gameOverLabel.setGeometry(300, 200, 200, 50)
        self.gameOverLabel.setAlignment(Qt.AlignCenter)
        self.gameOverLabel.setStyleSheet("color: red; font-size: 24px; background-color: white; border-radius: 10px;")
        self.gameOverLabel.hide()

    def updateTime(self):
        self.timeLeft -= 1
        self.Timer.setText(f"Time: {self.timeLeft}")
        if self.timeLeft <= 0:
            self.TimeCounter.stop()
            self.showGameOver()

    def showGameOver(self):
        self.gameOverLabel.setText("Game Over!")
        self.gameOverLabel.show()

        # Disable all buttons when game is over
        for btn in self.buttons:
            btn.setEnabled(False)

    def correctAnswer(self):
        self.score += 1
        self.scoreBoard.setText(f"Score: {self.score}")

        # Add 3 seconds to the timer when the player chooses the correct answer
        self.timeLeft += 1.5

        # Make sure the time does not exceed 60 seconds
        if self.timeLeft > 20:
            self.timeLeft =20

        self.Timer.setText(f"Time: {self.timeLeft}")

        if self.score % 3 == 0:
            self.gridsize += 1

        self.generate_Grid()

    def wrong_choice(self): 

        self.scoreBoard.setText(f"Score: {self.score}")


        self.timeLeft = max(0, self.timeLeft - 3)
        self.Timer.setText(f"Time: {self.timeLeft}")

        if self.timeLeft <= 0:
            self.showGameOver()

        

    def restartGame(self):
        self.score = 0
        self.timeLeft = 20 
        self.gridsize = 2
        self.scoreBoard.setText("Score: 0")
        self.Timer.setText("Time: 20")
        self.TimeCounter.start(1000)
        self.generate_Grid()

        
        self.gameOverLabel.hide()

        for btn in self.buttons:
            btn.setEnabled(True)

    def generate_Grid(self):
        for btn in self.buttons:
            self.GameGrid.removeWidget(btn)
            btn.deleteLater()
        self.buttons.clear()

        total_buttons = self.gridsize ** 2
        oddIndex = random.randint(0, total_buttons - 1)

        base_r = random.randint(50, 200)
        base_g = random.randint(50, 200)
        base_b = random.randint(50, 200)

        difficulty = max(2, self.base_color_diff - self.score // 3)

        odd_r = min(255, max(0, base_r + random.choice([-difficulty, difficulty])))
        odd_g = min(255, max(0, base_g + random.choice([-difficulty, difficulty])))
        odd_b = min(255, max(0, base_b + random.choice([-difficulty, difficulty])))

        base_color = QColor(base_r, base_g, base_b)
        odd_color = QColor(odd_r, odd_g, odd_b)

        # Calculate dynamic button size
        groupBox_width = self.GameBox.width()
        groupBox_height = self.GameBox.height()

        # Calculate the number of rows and columns
        rows = self.gridsize
        cols = self.gridsize

        # Dynamically adjust button size
        button_width = groupBox_width // cols
        button_height = groupBox_height // rows

        button_size = min(button_width, button_height)

        # Set a minimum button size to prevent buttons from being too small
        button_size = max(button_size, 15)

        for i in range(total_buttons):
            btn = QPushButton("")
            btn.setFixedSize(button_size, button_size)
            color = odd_color if i == oddIndex else base_color
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color.name()};
                    border-radius: 20px;
                    border: 2px solid white;
                }}
                QPushButton:hover {{
                    border: 2px solid yellow;
                }}
            """)

            if i == oddIndex:
                btn.clicked.connect(self.correctAnswer)
            else:
                btn.clicked.connect(self.wrong_choice)

            self.buttons.append(btn)
            self.GameGrid.addWidget(btn, i // self.gridsize, i % self.gridsize)

    def exit_to_main_menu(self):
        self.restartGame()
        GameStartWindow.close()
        window.show()



class Settings(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Odd One Game")
        self.setGeometry(0,0,800,450)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,450)
        picture = QPixmap("stockimages/1712197885705-79588672 (1).png")
        self.label.setPixmap(picture)
        self.label.setScaledContents(True)
        self.setFixedSize(800,450)
        self.Icon = QIcon("stockimages/1712197885705-79588672 (1).png")
        self.setWindowIcon(self.Icon)

        self.WindowCenter()
        self.initUI()


    def initUI(self):

        outerLayout = QVBoxLayout()
        outerLayout.setAlignment(Qt.AlignCenter)

        SettingsBox = QGroupBox()
        SettingsBox.setStyleSheet("""border:none;
                                  """)

        SettingsLayout = QGridLayout()


        MusicLabel = QLabel("Music")
        MusicLabel.setFont(QFont("Papyrus",20))
        MusicLabel.setAlignment(Qt.AlignLeft)
        MusicLabel.setStyleSheet("""  font-weight:bold;
                                      padding:30px,10px,0px,30px;
                               """)

        MusicVolumeSlider = QSlider(Qt.Horizontal)
        MusicVolumeSlider.setMinimum(0)
        MusicVolumeSlider.setMaximum(100)
        MusicVolumeSlider.setValue(50)

        MusicVolumeSlider.setStyleSheet("""
                                        
                                           QSlider{
                                                margin-left:30px;
                                                padding-right:30px;
                                        }
                                           QSlider::groove:horizontal{
                                                height:10px;
                                                background:#ddd;
                                                border-radius:5px;  
                                         }
                                            QSlider::handle:horizontal{
                                                    width:20px;
                                                    height:20px;
                                                    background:#5c5cff;
                                                    border:none;
                                                    border-radius:10px;
                                                    margin:-10px -10px -10px -10px;
                                            }
                                            QSlider::sub-page:horizontal{
                                                    background:#5c5cff;
                                                    border-radius:5px;

                                        } 
                                            QSlider::add-page:horizontal{
                                                    background:#aaa;
                                                    border-radius:5px;    
                                        }
                                        """)
        


        SettingsLayout.addWidget(MusicLabel, 0,0)
        SettingsLayout.addWidget(MusicVolumeSlider,0,1)

        MusicVolumeSlider.valueChanged.connect(self.volumeControl)




        SettingsBox.setLayout(SettingsLayout)

        SettingsBox.setFixedSize(500, 400)
        outerLayout.addWidget(SettingsBox,alignment=Qt.AlignCenter)


        self.setLayout(outerLayout)

        BackButton = QPushButton("Back",self)
        BackButton.setGeometry(30,30,70,50)
        BackButton.setFont(QFont("Papyrus",15))

        self.setStyleSheet("""QPushButton{
                                border:none;
                                border-radius:10px;
                                background:none;
                           }
                            QPushButton:hover{
                                color:white;
                                background-color:rgba(0,0,0,150)
                                
                           }
                           """)
        
        #activates when the backcbutton is clicked. it goes back to the main window
        BackButton.clicked.connect(self.backButton)


    def volumeControl(self,value):
        volume = value/100

        pygame.mixer.music.set_volume(volume)

    def backButton(self):
        SetingsWindow.close()
        window.show()


    def WindowCenter(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

        

class Credits(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Odd One Game")
        self.setGeometry(0,0,800,450)
        self.label = QLabel(self)
        self.label.setGeometry(0,0,800,450)
        picture = QPixmap("stockimages/1712197885705-79588672 (1).png")
        self.label.setPixmap(picture)
        self.label.setScaledContents(True)
        self.setFixedSize(800,450)
        self.Icon = QIcon("stockimages/1712197885705-79588672 (1).png")
        self.setWindowIcon(self.Icon)

        self.WindowCenter()
        self.initUI()


    
        

    def initUI(self):

        outerLayout = QVBoxLayout()
        outerLayout.setAlignment(Qt.AlignCenter)

        creditBox = QGroupBox()
        creditLayout = QVBoxLayout()

        creditBox.setStyleSheet("""border:none;
                                    color:white;
                                    background-color:rgba(0,0,0,155);
                                    border-radius:20px;
                                   
                                """) 
        

        creditTitle = QLabel("Credits")
        creditTitle.setFont(QFont("Papyrus",30))
        creditTitle.setAlignment(Qt.AlignCenter)
        creditTitle.setStyleSheet("""font-weight:bold;
                                     border:none;
                                     background:none;
                                        
                                    """)
        designs = QLabel("Designs: Kenth Michael Arminal")
        designs.setFont(QFont("Papyrus",15))
        designs.setAlignment(Qt.AlignCenter)
        designs.setStyleSheet("""font-weight:bold;
                                    border:none;
                                    background:none;
                     
                                    """)
        

        Music_and_SFX = QLabel("Music: Troy Leuterio")
        Music_and_SFX.setFont(QFont("Papyrus",15))
        Music_and_SFX.setAlignment(Qt.AlignCenter)
        Music_and_SFX.setStyleSheet("""font-weight:bold;
                                        border:none;
                                        background:none;
                     
                                        """)

        Programmer = QLabel("Programmer: Mark Steven Camposano")
        Programmer.setFont(QFont("Papyrus",15))
        Programmer.setAlignment(Qt.AlignCenter)
        Programmer.setStyleSheet("""font-weight:bold;
                                    border:none;
                                    background:none;
                                """)


        creditLayout.addWidget(creditTitle)
        creditLayout.addWidget(designs)
        creditLayout.addWidget(Music_and_SFX)
        creditLayout.addWidget(Programmer)

        creditBox.setLayout(creditLayout)

        creditBox.setFixedSize(500, 400)
        outerLayout.addWidget(creditBox,alignment=Qt.AlignCenter)

        #initialize the Vertical layout
        self.setLayout(outerLayout)

        BackButton = QPushButton("Back",self)
        BackButton.setGeometry(30,30,70,50)
        BackButton.setFont(QFont("Papyrus",15))

        self.setStyleSheet("""QPushButton{
                                border:none;
                                border-radius:10px;
                                background:none;
                           }
                            QPushButton:hover{
                                color:white;
                                background-color:rgba(0,0,0,150)
                                
                           }
                           """)
        
        #activates when the backcbutton is clicked. it goes back to the main window
        BackButton.clicked.connect(self.backButton)



    def backButton(self):
        CreditsWindow.close()
        window.show()


    def WindowCenter(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()

        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())




if __name__ =="__main__":

    app = QApplication(sys.argv)
    GameStartWindow = GamePlay()
    SetingsWindow = Settings()
    CreditsWindow = Credits()

    Splash = SplashScreen()
    Splash.show() 

    def start_main():
        global window 
        Splash.close()
        window = MainWindow()  
        window.show()
        
    QTimer.singleShot(3000,start_main)
    
    sys.exit(app.exec_())