'''
Author: Bug Router
Date: 2024-09-29 17:55:46
Description: Default
'''
import wx

class ImageDropTarget(wx.FileDropTarget):
    def __init__(self, panel):
        wx.FileDropTarget.__init__(self)
        self.panel = panel

    def OnDropFiles(self, x, y, filenames):
        print(filenames)
        if len(filenames) > 0:
            image_path = filenames[0]
            if image_path.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                img = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
                bmp = wx.Bitmap(img)
                self.panel.SetBitmap(bmp)
        return True

class ImagePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundStyle(wx.BG_STYLE_PAINT)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        if hasattr(self, 'bitmap'):
            dc.DrawBitmap(self.bitmap, 0, 0)

    def SetBitmap(self, bmp):
        self.bitmap = bmp
        self.Refresh()

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='图片查看器', size=(500, 630))

        panel = ImagePanel(self)
        drop_target = ImageDropTarget(panel)

        # 加载图片
        image = wx.Image('images/default.png', wx.BITMAP_TYPE_ANY)
        scaled_image = image.Scale(100, 100, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(scaled_image)

        # 创建一个静态位图，用于显示背景图
        static_bitmap = wx.StaticBitmap(panel, wx.ID_ANY, bitmap)

        # 绑定窗口大小调整事件
        self.Bind(wx.EVT_SIZE, self.on_size)
        panel.SetDropTarget(drop_target)

    def on_size(self, event):
        # 在窗口大小调整时，调整静态位图的大小以适应窗口
        event.Skip()
        size = self.GetClientSize()
        bitmap = wx.Bitmap('images/default.png', wx.BITMAP_TYPE_ANY)
        resized_bitmap = bitmap.Rescale(size.width, size.height)
        static_bitmap = wx.StaticBitmap(self.GetChildren()[0], wx.ID_ANY, resized_bitmap)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()