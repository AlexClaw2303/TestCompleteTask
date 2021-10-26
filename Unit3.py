def Test1():
  #wndYandexBrowser_WidgetWin_1 = Aliases.browser.wndYandexBrowser_WidgetWin_12
  
  # OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("C4 New File...").Click()
  wndYandexBrowser_WidgetWin_1 = Aliases.browser.wndYandexBrowser_WidgetWin_12
  chrome_RenderWidgetHostHWND = wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND
  OCR.Recognize(wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1.Keys("Пишу текст, по которому буду искать информацию")
  chrome_RenderWidgetHostHWND.Click(30, 106)
  wndYandexBrowser_WidgetWin_1.Keys("Пишу")

