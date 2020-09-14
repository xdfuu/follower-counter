from selenium import webdriver
import time
import userInfo as kb


class Browser:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goInstagram(self)
    
    def goInstagram(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)
        Browser.getFollowers(self)


    def getFollowers(self):
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)
        Browser.scrollDown(self)
        followers = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        numb = 0
        for follower in followers:
            numb += 1
            print(str(numb) +": " +follower.text)

    def scrollDown(self):
        jsCommand = """
        sayfa = document.querySelector(".isgrP");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """
        sayfaSonu = self.browser.execute_script(jsCommand)
        while True:
            son = sayfaSonu
            time.sleep(1)
            sayfaSonu = self.browser.execute_script(jsCommand)
            if son == sayfaSonu:
                break


    def login(self):
        username = self.browser.find_element_by_name("username")
        password = self.browser.find_element_by_name("password")

        username.send_keys(kb.userName)
        password.send_keys(kb.password)
        time.sleep(1)

        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        loginBtn.click()
        time.sleep(4)

        self.browser.get(self.link+"/"+kb.userName)
        time.sleep(3)