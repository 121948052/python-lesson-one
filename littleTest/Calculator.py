import wx

class CalculatorFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Simple Calculator', size=(300, 400))

        self.panel = wx.Panel(self)

        # 创建显示结果的文本框
        self.display = wx.TextCtrl(self.panel, style=wx.TE_RIGHT | wx.TE_READONLY)

        # 创建按钮
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        grid_sizer = wx.GridSizer(5, 4, 5, 5)
        for button_label in buttons:
            button = wx.Button(self.panel, label=button_label)
            grid_sizer.Add(button, 0, wx.EXPAND)
            button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # 布局
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.display, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(grid_sizer, 1, wx.EXPAND)

        self.panel.SetSizer(main_sizer)

    def on_button_click(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()
        current_value = self.display.GetValue()

        if label == '=':
            try:
                result = str(eval(current_value))
                self.display.SetValue(result)
            except Exception as e:
                self.display.SetValue('Error')
        elif label == 'C':
            self.display.SetValue('')
        else:
            self.display.SetValue(current_value + label)

if __name__ == '__main__':
    app = wx.App()
    frame = CalculatorFrame()
    frame.Show()
    app.MainLoop()