'''
Author: Bug Router
Date: 2024-09-30 16:18:47
Description: Default
'''
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='背景图片示例', size=(800, 580))

        # 创建一个面板
        panel = wx.Panel(self)

        # 加载图片
        image1 = wx.Image('images/default.png', wx.BITMAP_TYPE_ANY)
        scaled_image1 = image1.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(scaled_image1)
        self.SetBackgroundStyle(wx.BG_STYLE_ERASE, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        # 绑定窗口大小调整事件
        self.Bind(wx.EVT_SIZE, self.OnEraseBackground)

    def OnEraseBackground(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        width, height = self.GetSize()
        bmp = self.bitmap
        bmp_width, bmp_height = bmp.GetWidth(), bmp.GetHeight()
        x = (width - bmp_width) // 2
        y = (height - bmp_height) // 2
        dc.DrawBitmap(bmp, x, y)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()