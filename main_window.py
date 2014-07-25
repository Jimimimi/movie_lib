# Create Basic Window

import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self.CreateStatusBar()  # A Statusbar in the bottom

        #Create the Image Holder (imageHolder)
        imageHolder=wx.Panel(self)

        #Setting up the menu.
        #-----------------------------------------------------------------------------------------------------------
                
        #Creating the File Menu (filemenu)
        filemenu= wx.Menu()
        menuAbout=filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        # Other that I could use are here: http://docs.wxwidgets.org/2.8.12/wx_stdevtid.html
        filemenu.AppendSeparator()
        menuExit=filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        #Creating the Edit menu (editmenu)
        editmenu=wx.Menu()
        editmenu.Append(wx.ID_UNDO,"Undo","Undo the last thing you did")

        #Creating Fetct menu (fetchmenu)
        fetchmenu= wx.Menu()
        fetchmenu.Append(31, "IMDB"," Fetch Movie Data From IMDB")

        #Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editmenu,"Edit") # Adding the "editmenu" to the MenuBar
        menuBar.Append(fetchmenu,"Fetch") # Adding the "fetchmenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        #Set Events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        #Show menu or not
        self.Show(True)


    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        AboutMessage='''Movie Library
-----------------------------------------------------------------------------------------
[2014]  Harris Arvanitis
Email: xaris@gmx.com

This program is coded in python.
It is a home movie library for managing movies, series or videos etc.

Licence: Free
GitHub: https://github.com/XarisA/movie_lib
'''
        dlg = wx.MessageDialog( self,AboutMessage, "Movie Library", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # Destroy it when finished.
        

    def OnExit(self,e):
        self.Close(True)  # Close the frame.
    
class ImgPanel(wx.Panel):
    def __init__(self, parent, image):
        wx.Panel.__init__(self, parent)

        img = wx.Image(image, wx.BITMAP_TYPE_ANY)
        self.sBmp = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img))

        sizer = wx.BoxSizer()
        sizer.Add(item=self.sBmp, proportion=0, flag=wx.ALL, border=10)
        self.SetBackgroundColour('green')
        self.SetSizerAndFit(sizer)


app = wx.App(False)
frame = MainWindow(None, "Movie Library")
app.MainLoop()

