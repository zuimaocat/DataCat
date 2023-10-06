# 导入 webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.Chrome()
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 
sheng_from = '广东省'
city_from = '广州市'

sheng_to = '河北省'
city_to = '承德市'
driver.get("https://www.chinawutong.com/201/")
driver.maximize_window()
# # id="kw"是百度搜索输入框，输入字符串"长城" 
driver.find_element(By.CSS_SELECTOR,"#tbFrom").click()

religion = driver.find_element(By.CSS_SELECTOR, 'span.wtm_a_txt[txt={}]'.format(sheng_from)).click()
time.sleep(1)

religion = driver.find_element(By.CSS_SELECTOR, 'span.wtm_a_txt[txt={}]'.format(city_from)).click()

driver.find_element(By.CSS_SELECTOR,"#tbTo").click()
religion = driver.find_element(By.CSS_SELECTOR, 'span.wtm_a_txt[txt={}]'.format(sheng_to)).click()
time.sleep(1)


religion = driver.find_element(By.CSS_SELECTOR, 'span.wtm_a_txt[txt={}]'.format(city_to)).click()
driver.find_element(By.CSS_SELECTOR, 'span.orangeBtn').click()



# 点击该元素
# # id="su"是百度搜索按钮，click() 是模拟点击
# driver.find_element(By.CSS_SELECTOR,"#su").click()
time.sleep(19)
# # 关闭浏览器
