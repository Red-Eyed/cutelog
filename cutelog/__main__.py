import sys


def main():
    import signal
    from config import ROOT_LOG
    from main_window import MainWindow
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import QApplication

    if sys.platform == 'win32':
        import ctypes
        appid = 'busimus.cutelog'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/cutelog.png'))
    mw = MainWindow(ROOT_LOG, app)
    signal.signal(signal.SIGINT, mw.signal_handler)

    sys.exit(app.exec_())
    qCleanupResources()


if __name__ == '__main__':
    main()
