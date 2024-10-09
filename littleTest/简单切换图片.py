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
        size = self.GetClientSize()
        element_size = self.static_bitmap1.GetSize()

        # 计算居中位置
        x_pos = (size.width - element_size.width) // 2
        y_pos = (size.height - element_size.height) // 2

        # 初始只显示第一张图片，隐藏第二张图片
        self.static_bitmap2.Hide()

        self.static_bitmap1.SetPosition((x_pos, y_pos))
        self.static_bitmap2.SetPosition((x_pos, y_pos))

        # 创建按钮并绑定事件
        button = wx.Button(panel, label='切换')
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # 使用垂直方向的 BoxSizer 布局，将图片和按钮依次添加
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.static_bitmap1, 0, wx.ALL | wx.CENTER, 0)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 10)

        panel.SetSizer(sizer)

        self.Bind(wx.EVT_SIZE, self.on_resize)

    def on_button_click(self, event):
        if self.static_bitmap1.IsShown():
            self.static_bitmap1.Hide()
            self.static_bitmap2.Show()
        else:
            self.static_bitmap1.Show()
            self.static_bitmap2.Hide()
        self.Layout()

    def on_resize(self, event):
        size = self.GetClientSize()
        element_size = self.static_bitmap1.GetSize()
        x_pos = (size.width - element_size.width) // 2
        y_pos = (size.height - element_size.height) // 2
        self.static_bitmap1.SetPosition((x_pos, y_pos))
        self.static_bitmap2.SetPosition((x_pos, y_pos))

        # 计算高度最大时的宽度比例
        aspect_ratio = self.image1.GetWidth() / self.image1.GetHeight()
        new_height = size.GetHeight() - 50
        new_width = new_height * aspect_ratio

        resized_image = self.image1.Scale(int(new_width), int(new_height))
        self.bitmap1 = wx.Bitmap(resized_image)
        self.static_bitmap1.SetBitmap(self.bitmap1)
        
        self.bitmap2 = wx.Bitmap(resized_image)
        self.static_bitmap2.SetBitmap(self.bitmap2)
        
        size = self.GetClientSize()
        button_size = self.FindWindowByName('切换').GetSize()
        x_pos = (size.width - button_size.width)
        self.FindWindowByName('切换').SetPosition((x_pos, 20))

        event.Skip()

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()