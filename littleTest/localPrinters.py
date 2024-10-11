import wx
import win32print
import threading
    
file_path = 'C:\\Users\\Administrator\\Desktop\\test.txt'
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
        self.dropdown = wx.Choice(self.panel, choices=choices, pos=(100, 50))
        self.dropdown.SetSelection(0)

        # 绑定下拉框选择事件
        self.dropdown.Bind(wx.EVT_CHOICE, self.on_dropdown_select)
        
        # 创建一个按钮
        button = wx.Button(self.panel, label='Start Printing', pos=(100, 100))

        # 绑定按钮的点击事件
        button.Bind(wx.EVT_BUTTON, self.on_button_click)
            
    def on_button_click(self):
        # 创建一个线程来执行打印任务
        print_thread = threading.Thread(target=self.print_file, args=(file_path,))

        print_thread.start()

    def on_dropdown_select(self, event):
        selected_index = event.GetSelection()
        selected_option = self.dropdown.GetString(selected_index)
        print(f'Selected option: {selected_option}')

    def print_file(self):
        selected_index = self.dropdown.GetSelection()
        printer_name = self.dropdown.GetString(selected_index)
        # 打开打印机句柄
        printer_handle = win32print.OpenPrinter(printer_name)
        try:
            # 开始打印文档
            win32print.StartDocPrinter(printer_handle, 1, ("Document Name", None, "RAW"))
            win32print.StartPagePrinter(printer_handle)

            # 读取文件内容并写入打印机
            with open(file_path, 'rb') as f:
                data = f.read()
                win32print.WritePrinter(printer_handle, data)

            # 结束打印
            win32print.EndPagePrinter(printer_handle)
            win32print.EndDocPrinter(printer_handle)
        finally:
            # 关闭打印机句柄
            win32print.ClosePrinter(printer_handle)

if __name__ == '__main__':
    app = wx.App()
    frame = PrinterFrame()
    frame.Show()
    app.MainLoop()