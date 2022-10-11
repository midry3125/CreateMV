import wx
from CreateMVMyFrame1 import CreateMVMyFrame1

def main():
    app = wx.App()
    frame = CreateMVMyFrame1(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()
