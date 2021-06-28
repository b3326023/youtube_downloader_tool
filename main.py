import sys
import youtube_dl
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5 import QtGui
from mainUI import Ui_MainWindow  # mainUI 是 UI 的 .py 檔案名字

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png')) 

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_dl.clicked.connect(self.download)

        # Initialize the ComboBox of Q1.3
        fmt_list = ['mp3', 'mp4']
        self.ui.comboBox_fmt.addItems(fmt_list)

        
    def download(self):
        url = self.ui.lineEdit_url.text()
        directory = self.ui.lineEdit_dir.text()
        fmt = self.ui.comboBox_fmt.currentText()
        if fmt == 'mp3':
            ydl_opts={'outtmpl':directory+'/%(title)s.%(ext)s','format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':'mp3','preferredquality':'192'}]}
        elif fmt == 'mp4':
            ydl_opts={'outtmpl':directory+'/%(title)s.%(ext)s','format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]'}
        print("Start Download...")
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print("Download Finished!")
        



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())