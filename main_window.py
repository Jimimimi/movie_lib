# Create Basic Window

import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^wx.MAXIMIZE_BOX)
        self.CreateStatusBar()  # A Statusbar in the bottom

        #Create the Image Holder (imageHolder)
        
        
        # Create the Two Boxes with 1 panel each
                
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.pnl1 = wx.Panel(self, -1, size=(250,600), style=wx.NO_BORDER)
        self.pnl2 = wx.Panel(self, -1, size=(600,600),style=wx.NO_BORDER)
        
        #image = wx.Image('C:\Users\Administrator\Pictures\img.jpg', wx.BITMAP_TYPE_ANY)
        instructions = 'Kati ithela na grapsw edw alla ti?'
        image = wx.EmptyImage(240,280)
        self.PhotoMaxSize = 240
        
        
        browseBtn = wx.Button(self.pnl1, label='Browse')
        browseBtn.Bind(wx.EVT_BUTTON, self.onBrowse)
        self.imageBitmap = wx.StaticBitmap(self.pnl1, wx.ID_ANY, wx.BitmapFromImage(image))
        
        instructLbl = wx.StaticText(self.pnl1, label=instructions)
        self.photoTxt = wx.TextCtrl(self.pnl1, size=(68,0))
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        
        
        
        mainSizer.Add(wx.StaticLine(self.pnl1, wx.ID_ANY),
                           0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(instructLbl, 0, wx.ALL, 5)
        mainSizer.Add(self.imageBitmap, 0, wx.ALL, 5)
        sizer.Add(self.photoTxt, 0, wx.ALL, 5)
        sizer.Add(browseBtn, 0, wx.ALL, 5)
                
        mainSizer.Add(sizer, 0, wx.ALL, 5)
 
        self.pnl1.SetSizer(mainSizer)

        mainSizer.Fit(self.pnl1)
        self.pnl1.Layout()
                
                
        hbox.Add(self.pnl1, 1, wx.EXPAND | wx.ALL, 3)
        hbox.Add(self.pnl2, 1, wx.EXPAND | wx.ALL, 3)
                            
        self.SetSize((800, 600))
        self.SetSizer(hbox)
        self.Centre()
        
        
        
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
               
    def onBrowse(self,event):
        """ 
        Browse for file
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"
        dialog = wx.FileDialog(None, "Choose a file",
                               wildcard=wildcard,
                               style=wx.OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            self.photoTxt.SetValue(dialog.GetPath())
        dialog.Destroy() 
        self.onView()
 
    def onView(self):
        filepath = self.photoTxt.GetValue()
        img = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)
 
        self.imageBitmap.SetBitmap(wx.BitmapFromImage(img))
        self.pnl1.Refresh()


app = wx.App(False)
frame = MainWindow(None, "Movie Library")
app.MainLoop()

