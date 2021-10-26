def Test1():
  wndYandexBrowser_WidgetWin_1 = Aliases.browser.wndYandexBrowser_WidgetWin_12
  chrome_RenderWidgetHostHWND = wndYandexBrowser_WidgetWin_1.Chrome_RenderWidgetHostHWND
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("New").Click()
  wndYandexBrowser_WidgetWin_1.Keys("Шрифт меняю")
  chrome_RenderWidgetHostHWND.Click(36, 1266)
  chrome_RenderWidgetHostHWND.Click(136, 938)
  chrome_RenderWidgetHostHWND.Click(1258, 353)
  wndYandexBrowser_WidgetWin_1.Keys("[BS][BS]20")
  chrome_RenderWidgetHostHWND.Click(1467, 368)
  OCR.Recognize(chrome_RenderWidgetHostHWND).BlockByText("Шрифт").Click()
