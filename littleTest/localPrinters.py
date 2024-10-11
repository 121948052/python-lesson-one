import wx
import win32print
    
class PrinterFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Local Printers', size=(400, 500))

        # 创建下拉框选项列表
        choices = []
        self.panel = wx.Panel(self)

        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        for printer in printers:
            choices.append(printer[2])
            
        # 创建下拉框
        self.dropdown = wx.Choice(self.panel, choices=choices)
        self.dropdown.SetSelection(0)  # 设置默认选中的选项索引

        # 绑定下拉框选择事件
        self.dropdown.Bind(wx.EVT_CHOICE, self.on_dropdown_select)

    def on_dropdown_select(self, event):
        selected_index = event.GetSelection()
        selected_option = self.dropdown.GetString(selected_index)
        print(f'Selected option: {selected_option}')

if __name__ == '__main__':
    app = wx.App()
    frame = PrinterFrame()
    frame.Show()
    app.MainLoop()