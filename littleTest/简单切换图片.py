import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='简单图片切换', size=(500, 630))
        panel = wx.Panel(self)

        # 加载两张图片
        self.image1 = wx.Image('images/演员1.gif', wx.BITMAP_TYPE_ANY)
        self.scaled_image1 = self.image1.Scale(400, 500, wx.IMAGE_QUALITY_HIGH)
        self.bitmap1 = wx.Bitmap(self.scaled_image1)
        self.static_bitmap1 = wx.StaticBitmap(panel, -1, self.bitmap1)

        self.image2 = wx.Image('images/演员2.gif', wx.BITMAP_TYPE_ANY)
        self.scaled_image2 = self.image2.Scale(400, 500, wx.IMAGE_QUALITY_HIGH)
        self.bitmap2 = wx.Bitmap(self.scaled_image2)
        self.static_bitmap2 = wx.StaticBitmap(panel, -1, self.bitmap2)

        # 获取屏幕尺寸和面板尺寸
        screen_size = wx.DisplaySize()
        panel_size = panel.GetSize()

        # 计算居中位置
        center_x = (screen_size[0] - panel_size[0]) / 2
        center_y = (screen_size[1] - panel_size[1]) / 2

        # 初始只显示第一张图片，隐藏第二张图片
        self.static_bitmap2.Hide()

        # 获取屏幕尺寸和面板尺寸
        screen_size = wx.DisplaySize()
        panel_size = panel.GetSize()

        self.static_bitmap1.SetPosition((center_x, center_y))
        self.static_bitmap2.SetPosition((center_x, center_y))

        # 创建按钮并绑定事件
        button = wx.Button(panel, label='切换')
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # 使用垂直方向的 BoxSizer 布局，将图片和按钮依次添加
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.static_bitmap1, 0, wx.ALL, 0)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

    def on_button_click(self, event):
        if self.static_bitmap1.IsShown():
            self.static_bitmap1.Hide()
            self.static_bitmap2.Show()
        else:
            self.static_bitmap1.Show()
            self.static_bitmap2.Hide()
        self.Layout()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()