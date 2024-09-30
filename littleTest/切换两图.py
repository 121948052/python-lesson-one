'''
Author: Bug Router
Date: 2024-09-30 18:03:26
Description: Default
'''
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='简单图片切换', size=(500, 630))

        panel = wx.Panel(self)

        # 创建一个垂直方向的 BoxSizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # 加载两张图片
        image1 = wx.Image('images/演员1.gif', wx.BITMAP_TYPE_ANY)
        scaled_image1 = image1.Scale(400, 500, wx.IMAGE_QUALITY_HIGH)
        bitmap1 = wx.Bitmap(scaled_image1)
        static_bitmap1 = wx.StaticBitmap(panel, wx.ID_ANY, bitmap1)
        vbox.Add(static_bitmap1, 0, wx.EXPAND | wx.TOP, 10)

        # image2 = wx.Image('images/演员2.gif', wx.BITMAP_TYPE_ANY)
        # scaled_image2 = image2.Scale(400, 500, wx.IMAGE_QUALITY_HIGH)
        # bitmap2 = wx.Bitmap(scaled_image2)
        # static_bitmap2 = wx.StaticBitmap(panel, wx.ID_ANY, bitmap2)
        # vbox.Add(static_bitmap2, 0, wx.EXPAND | wx.TOP, 10)

        # 按钮用于切换图片层级
        button = wx.Button(panel, label='切换')
        self.Bind(wx.EVT_BUTTON, self.on_button_click, button)

        # 将按钮添加到 BoxSizer 中，并设置对齐方式为居中对齐
        vbox.Add(button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)
        panel.SetSizer(vbox)

    def on_button_click(self, event):
        # 获取窗口中的子窗口（这里假设只有两个静态位图）
        children = self.GetChildren()[0].GetChildren()
        if len(children) == 2:
            static_bitmap1, static_bitmap2 = children
            # 切换层级
            if static_bitmap1.IsShown():
                static_bitmap1.SendToBack()
                static_bitmap2.BringToFront()
            else:
                static_bitmap2.SendToBack()
                static_bitmap1.BringToFront()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()