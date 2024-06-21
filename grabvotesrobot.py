from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

# 引號內放要去的網址
driver.get('https://shopping.friday.tw/ec2/product?pid=7380168&cid=418800&sid=0&mid=1')

driver.find_element_by_xpath("//*[@id=\"e3_buy\"]/span").click()

# 登入帳號密碼
account = driver.find_element_by_xpath("//*[@id=\"j_username\"]")
account.clear()
account.send.keys("你的帳號")
password = driver.find_element_by_xpath('//*[@id=\"j_password\"]')
password.clear()
password.send.keys("你的密碼")
driver.find_element_by_xpath("//*[@id=\"login_btn\"]").click()

driver.find_element_by_xpath("//*[@id=\"contarea-box\"]/ul/li/div[3]/button[1]/span").click()

cvc = driver.find_element_by_xpath("//*[@id=\"creidtcard_record_area_default\"]/div/div[2]/input[2]").click()
cvc.clear()
cvc.send.keys("信用卡驗證碼")

driver.find_element_by_xpath("//*[@id=\"same\"]")
homee2 = driver.find_element_by_xpath("//*[@id=\"shippingaddress2\"]")
homee2.clear()
homee2.send.keys("地址")

driver.find_element_by_xpath("//*[@id=\*contarea-box*\"]/div[3]/button").click()

# 如果是第一次購買的話，就新增以下資料
namee = driver.find_element_by_xpath("//*[@id=\"billingname\"]")
namee.clear()
namee.send.keys("姓名")
phonee = driver.find_element_by_xpath("//*[@id=\"billingmobile\"]")
phonee.clear()
phonee.send.keys("電話")
eemail = driver.find_element_by_xpath("//*[@id=\"billingemail\"]")
eemail.clear()
eemail.send.keys("電子郵件")
homee = driver.find_element_by_xpath("//*[@id=\"addConsigneeCityId2\"]")
homee.send.keys("縣市")
year = driver.find_element_by_xpath("//*[@id=\"birthbay_year\"]")
year.send.keys("西元出生年")
month = driver.find_element_by_xpath("//*[@id=\"birthbay_month\"]")
month.send.keys("月份不含0")
day = driver.find_element_by_xpath("//*[@id=\"birthbay_day\"]")
day.send.keys("日期不含0")
homee2 = driver.find_element_by_xpath("//*[@id=\"address3\"]")
homee2.send.keys("地址")
# 下面女生的話改成gender2
driver.find_element_by_xpath("//*[@id=\"gender1\"]").click()
driver.find_element_by_xpath("//*[@id=\"same\"]").click()
driver.find_element_by_xpath("//*[@id=\"same2\"]").click()