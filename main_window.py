# Create Basic Window

import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self.CreateStatusBar()  # A Statusbar in the bottom 

        # Setting up the menu.
        #-----------------------------------------------------------------------------------------------------------
                
        #Creating the File Menu (filemenu)
        filemenu= wx.Menu()
        filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        # Other that I could use are here: http://docs.wxwidgets.org/2.8.12/wx_stdevtid.html
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        #Creating the Edit menu (editmenu)
        editmenu=wx.Menu()
        editmenu.Append(wx.ID_UNDO,"Undo","Undo the last thing you did")

        #Creating Fetct menu (fetchmenu)
        fetchmenu= wx.Menu()
        fetchmenu.Append(31, "IMDB"," Fetch Movie Data From IMDB")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editmenu,"Edit") # Adding the "editmenu" to the MenuBar
        menuBar.Append(fetchmenu,"Fetch") # Adding the "fetchmenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, "Movie Library")
app.MainLoop()

