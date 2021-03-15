import wx
from gui2 import regis


class loginFrame (regis) :
    
    def __init__(self,parent):
       regis. __init__  (self,parent) 
       
       self.SetIcon(wx.Icon("LOGO.ico"))
       self.SetTitle ("Daftar")
       png = wx.Image('transparant.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
       wx.StaticBitmap(self, 5, png, (20, 100), (png.GetWidth(), png.GetHeight()))

    def buttonSimpan(self, event):
        nama = self.inp_nama.GetValue()
        email = self.inp_mail.GetValue()
        pswr= self.inp_pw.GetValue()
        if (len(nama) != 0 and len(email)!= 0 and len(pswr)!= 0 ):
            print ("Tidak boleh ada data yang kososng")
       
       
       
        
      
    



app = wx.App()
login2 = loginFrame (parent = None)
login2.Show()
app.MainLoop()


