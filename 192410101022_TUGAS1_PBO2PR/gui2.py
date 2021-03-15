# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class regis
###########################################################################

class regis ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.ICONIZE|wx.BORDER_THEME )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.judul = wx.StaticText( self, wx.ID_ANY, u"HELLO WX\nSelamat Mendaftar!", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.judul.Wrap( -1 )

		self.judul.SetFont( wx.Font( 15, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Lucida Fax" ) )
		self.judul.SetForegroundColour( wx.Colour( 162, 127, 172 ) )
		self.judul.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1.Add( self.judul, 0, wx.ALIGN_CENTER|wx.ALL, 20 )

		gSizer1 = wx.GridSizer( 0, 0, 0, 0 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Nama            :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.inp_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), wx.TE_LEFT )
		self.inp_nama.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )

		fgSizer2.Add( self.inp_nama, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		pilihjlChoices = [ u"Laki-laki", u"Perempuan" ]
		self.pilihjl = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), pilihjlChoices, 0 )
		self.pilihjl.SetSelection( 0 )
		fgSizer2.Add( self.pilihjl, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"E-mail            :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.inp_mail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), 0 )
		fgSizer2.Add( self.inp_mail, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Password       :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.inp_pw = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,25 ), wx.TE_PASSWORD )
		fgSizer2.Add( self.inp_pw, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.ALIGN_CENTER, 5 )

		self.simpan1 = wx.Button( self, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.Size( 150,25 ), 0|wx.BORDER_NONE )

		self.simpan1.SetBitmapPosition( wx.BOTTOM )
		self.simpan1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Lucida Fax" ) )
		self.simpan1.SetBackgroundColour( wx.Colour( 162, 127, 172 ) )

		fgSizer2.Add( self.simpan1, 0, wx.TOP, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( fgSizer2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.RIGHT, 5 )


		bSizer1.Add( gSizer1, 1, wx.ALL|wx.EXPAND, 5 )

		self.namaBawah = wx.StaticText( self, wx.ID_ANY, u"ROSA  AMELIA  (192410101022)  (PBO-C)", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
		self.namaBawah.SetLabelMarkup( u"ROSA  AMELIA  (192410101022)  (PBO-C)" )
		self.namaBawah.Wrap( -1 )

		self.namaBawah.SetFont( wx.Font( 10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_LIGHT, False, "Lucida Fax" ) )
		self.namaBawah.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.namaBawah.SetBackgroundColour( wx.Colour( 162, 127, 172 ) )

		bSizer1.Add( self.namaBawah, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.simpan1.Bind( wx.EVT_BUTTON, self.buttonSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def buttonSimpan( self, event ):
		event.Skip()


