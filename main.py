import sys

#importing Widgtes
from PyQt5.QtWidgets import *

#importing Engine Widgets
from PyQt5.QtWebEngineWidgets import *

#importing QtCore to use Qurl
from PyQt5.QtCore import *

from  PyQt5 import  QtGui

#main window class (to create a window)-sub class of QMainWindow class
class Window(QMainWindow):

    #defining constructor function
    def __init__(self):
        #creating connnection with parent class constructor
        super(Window,self).__init__()

        #---------------------adding browser-------------------
        self.browser = QWebEngineView()

        #setting url for browser, you can use any other url also
        self.browser.setUrl(QUrl('http://google.com'))

        #to display google search engine on our browser
        self.setCentralWidget(self.browser)

        #-------------------full screen mode------------------
        #to display browser in full screen mode, you may comment below line if you don't want to open your browser in full screen mode
        self.showMaximized()

        #----------------------navbar-------------------------
        #creating a navigation bar for the browser
        navbar = QToolBar()
        #adding created navbar
        self.addToolBar(navbar)

        #-----------------prev Button-----------------
        #creating prev button
        prevBtn = QAction('<--',self)
        #when triggered set connection 
        prevBtn.triggered.connect(self.browser.back)
        # adding prev button to the navbar
        navbar.addAction(prevBtn)

        #-----------------next Button---------------
        nextBtn = QAction('-->',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #-----------refresh Button--------------------
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #-----------home button----------------------
        homeBtn = QAction('Home',self)
        #when triggered call home method
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)

        #---------------------search bar---------------------------------
        #to maintain a single line
        self.searchBar = QLineEdit()
        #when someone presses return(enter) call loadUrl method
        self.searchBar.returnPressed.connect(self.loadUrl)
        #adding created seach bar to navbar
        navbar.addWidget(self.searchBar)
        #if url in the searchBar is changed then call updateUrl method
        self.browser.urlChanged.connect(self.updateUrl)
        # ---------------------logo---------------------------------
        self.setWindowIcon(QtGui.QIcon('AH.jpeg'))
        self.show()

        self.addToolBarBreak()

        # Adding another toolbar which contains the bookmarks
        bookmarks = QToolBar('Bookmarks', self)
        self.addToolBar(bookmarks)

        google = QAction("Google", self)
        google.setStatusTip("Go to Google")
        google.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.google.com")))
        bookmarks.addAction(google)


        facebook = QAction("Facebook", self)
        facebook.setStatusTip("Go to Facebook")
        facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
        bookmarks.addAction(facebook)

        youTube = QAction("YouTube", self)
        youTube.setStatusTip("Go to YouTube")
        youTube.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.youTube.com")))
        bookmarks.addAction(youTube)

        instagram = QAction("Instagram", self)
        instagram.setStatusTip("Go to Instagram")
        instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
        bookmarks.addAction(instagram)

        twitter = QAction("Twitter", self)
        twitter.setStatusTip("Go to Twitter")
        twitter.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
        bookmarks.addAction(twitter)


    #method to navigate back to home page
    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    #method to load the required url
    def loadUrl(self):
        #fetching entered url from searchBar
        url = self.searchBar.text()
        #loading url
        self.browser.setUrl(QUrl(url))

    def go_to_URL(self, url: QUrl):
        self.browser.setUrl(url)
        self.updateUrl(url)

    #method to update the url
    def updateUrl(self, url):
        #changing the content(text) of searchBar
        self.searchBar.setText(url.toString())


MyApp = QApplication(sys.argv)

#setting application name
QApplication.setApplicationName('AH')

#creating window
window = Window()

#executing created app
MyApp.exec_()

#installation cmds-----
# pip install PyQtWebEngine
# pip install PyQt5