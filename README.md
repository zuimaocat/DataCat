# DataCat - 物流数据采集工具 V1.0.0

**简介：**

数据猫是一款用于采集物流网站数据的工具，可以获取物流网站对应地点的线路数据，包括公司名称、重货价、轻货价、公司资历等信息。该工具支持通过URL爬取数据，可以一次采集多个URL的数据，并支持输入起点和终点来获取数据。获取的数据会自动保存到Excel表格中。
![UI](https://github.com/zuimaocat/picbed/blob/main/UI.png)

**使用方法：**

1. 安装Chrome浏览器版本104.0.105+（其他版本未经过测试）。
2. 运行主程序 `main.py`。
3. 在主程序中，可以输入物流线路的起点和终点。
4. 输入要采集的物流网站的URL或多个URL。
5. 点击开始采集按钮，工具将自动访问网站并采集数据。
6. 采集完成后，数据会自动写入Excel表格中。

**注意事项：**

1. 本软件需要配合104.0.105+版本的Chrome浏览器使用，其他版本未经过测试
2. `selenium.py` 和 `UI.py` 暂时没有作用，与Selenium和用户界面相关的代码已经整合到 `main.py` 中。

**运行环境**

1.谷歌浏览器
```bash
https://www.slimjet.com/chrome/download-chrome.php?file=files%2F104.0.5112.102%2FChromeStandaloneSetup.exe
```
2.chromedriver（用于控制浏览器）
```bash
https://registry.npmmirror.com/-/binary/chromedriver/104.0.5112.79/chromedriver_win32.zip
```
3.依赖的Python库
```bash
pip install -r requirements.txt
```
4.Python版本：V3.8.8
**未来更新计划：**

1. 从多个网站中获取数据，使用正则表达式或其他方法匹配数据，并且使用多线程进行高效采集。

2. 使用Scrapy框架重新编写，使软件更加工程化和可维护。

3. 扩展数据采集范围，包括公司地点、联系方式等更多信息。

4. 加入数据分析功能，不再局限于仅存储数据，提供数据分析和可视化工具。

5. 重新设计用户界面，添加进度条、复选框、弹窗提示等改进功能，提高用户体验。

数据猫是一个功能强大的物流数据采集工具，随着未来更新计划的实施，将提供更多的功能和便利，帮助用户更轻松地采集和分析物流数据。
