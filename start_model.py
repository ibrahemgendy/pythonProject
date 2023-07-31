import sys
import traceback
from PyQt5 import QtWidgets
from main import Application


def main():
    try:
        aPyqt_App = QtWidgets.QApplication(sys.argv)
        aApp = Application()
        aApp.set_throttle(50)
        aApp.set_steering(40)
        aApp.run_application()
        sys.exit(aPyqt_App.exec())
    except Exception as e:
        print("An unhandled exception occurred:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
