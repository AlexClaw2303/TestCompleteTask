def Test1():
  wndYandexBrowser_WidgetWin_1 = Aliases.browser.wndYandexBrowser_WidgetWin_12
  OCR.Recognize(wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1.Keys("hello world")

  
  
