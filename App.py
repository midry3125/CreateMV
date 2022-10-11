# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "CMV", pos = wx.DefaultPosition, size = wx.Size( 800, 500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(700, 500), wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_panel2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(250, 500), wx.TAB_TRAVERSAL )
        gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"保存先", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        gSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl16 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

        self.m_button11 = wx.Button( self.m_panel2, wx.ID_ANY, u"参照", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button11, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"音声ファイル", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        gSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl14 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_textCtrl14, 0, wx.ALL, 5 )

        self.m_button8 = wx.Button( self.m_panel2, wx.ID_ANY, u"参照", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"背景画像", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gSizer5.Add( self.m_staticText9, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl15 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

        self.m_button9 = wx.Button( self.m_panel2, wx.ID_ANY, u"参照", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button9, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"オーディオスペクトラムの種類", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        gSizer5.Add( self.m_staticText11, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        m_choice2Choices = [ u"直線形", u"円形" ]
        self.m_choice2 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        gSizer5.Add( self.m_choice2, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"オーディオスペクトラムの色", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        gSizer5.Add( self.m_staticText12, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        m_choice3Choices = [ u"赤", u"青", u"緑", u"黄色", u"黒", u"白" ]
        self.m_choice3 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
        self.m_choice3.SetSelection( 0 )
        gSizer5.Add( self.m_choice3, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        self.m_staticText81 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"背景画像の明るさ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )

        gSizer5.Add( self.m_staticText81, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_slider1 = wx.Slider( self.m_panel2, wx.ID_ANY, 0, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
        gSizer5.Add( self.m_slider1, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, "0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.SetForegroundColour("#FF0000")
        self.m_staticText13.Wrap( -1 )

        gSizer5.Add( self.m_staticText13, 0, wx.ALL, 5 )


        gSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button10 = wx.Button( self.m_panel2, wx.ID_ANY, u"生成", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer5.Add( self.m_button10, 0, wx.ALL, 5 )


        self.m_panel2.SetSizer( gSizer5 )
        self.m_panel2.Layout()
        gSizer5.Fit( self.m_panel2 )
        bSizer8.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(550, 500), wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap2 = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, self.m_panel3.Size, 0 )
        bSizer11.Add( self.m_bitmap2, 0, wx.ALL, 5 )


        self.m_panel3.SetSizer( bSizer11 )
        self.m_panel3.Layout()
        bSizer11.Fit( self.m_panel3 )
        bSizer8.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_panel1.SetSizer( bSizer8 )
        self.m_panel1.Layout()
        bSizer8.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button11.Bind( wx.EVT_BUTTON, self.m_button11OnButtonClick )
        self.m_button8.Bind( wx.EVT_BUTTON, self.m_button8OnButtonClick )
        self.m_button9.Bind( wx.EVT_BUTTON, self.m_button9OnButtonClick )
        self.m_button10.Bind( wx.EVT_BUTTON, self.m_button10OnButtonClick )
        self.m_choice2.Bind( wx.EVT_CHOICE, self.show_preview )
        self.m_choice3.Bind( wx.EVT_CHOICE, self.show_preview )
        self.m_textCtrl15.Bind( wx.EVT_TEXT, self.show_preview )
        self.m_slider1.Bind( wx.EVT_SLIDER, self.m_slider1OnSlider )
        self.m_textCtrl4.Bind( wx.EVT_TEXT, self.m_textCtrl4OnText )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def m_button11OnButtonClick( self, event ):
        event.Skip()

    def m_button8OnButtonClick( self, event ):
        event.Skip()

    def m_button9OnButtonClick( self, event ):
        event.Skip()

    def m_button10OnButtonClick( self, event ):
        event.Skip()

    def show_preview( self, event ):
        event.Skip()

    def m_slider1OnSlider( self, event ):
        event.Skip()

    def m_textCtrl4OnText( self, event ):
        event.Skip()
