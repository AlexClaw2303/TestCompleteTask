

def Test2():
  browser = Aliases.browser
  wndYandexBrowser_WidgetWin_1 = browser.wndYandexBrowser_WidgetWin_12
  chrome_RenderWidgetHostHWND = wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1.Keys("Файл, который можно будет сохранить")
  chrome_RenderWidgetHostHWND.Click(25, 24)
  chrome_RenderWidgetHostHWND.Click(322, 191)
  browser.dlgSaveAs.btnSave.ClickButton()

  
  

def Test1():
  # без перезаписи
  browser = Aliases.browser
  #wndYandexBrowser_WidgetWin_1 = browser.wndYandexBrowser_WidgetWin_12
  #chrome_RenderWidgetHostHWND = wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND
  #OCR.Receognize(chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1 = Aliases.browser.wndYandexBrowser_WidgetWin_12
  OCR.Recognize(wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1.Keys("Новый файл, для сохранения ")
  wndYandexBrowser_WidgetWin_1.Keys("^ы")
  browser.dlgSaveAs.btnSave.ClickButton()
