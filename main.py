from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import random
import multiprocessing


invite = "https://discord.gg/YourLink"
options = Options()
options.headless = True
options.add_argument("disable-gpu")
options.add_argument("disbale-infobars")
options.add_argument("--disable-extenstions")
options.add_argument("window-size=640x360")

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True


with open('proxies.txt') as f:
    proxies_list = [proxies_list.rstrip() for proxies_list in f]


with open('tokens.txt') as f:
    tokenlist = [tokenlist.rstrip() for tokenlist in f]

def run(x):
            PROXY = random.choice(proxies_list)

            firefox_capabilities['proxy'] = {
                "proxyType": "MANUAL",
                "httpProxy": PROXY,
                "sslProxy": PROXY
            }
            browser = webdriver.Firefox(capabilities=firefox_capabilities, options=options)
            browser.get(invite)
            
            browser.delete_all_cookies()
            token = x.rstrip()
            js = '''function login(token) { setInterval(() => {  document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` }, 50);  setTimeout(() => {   location.reload();  }, 2500); } 
            login("'''+token+'''")'''
            browser.execute_script(js)
            while True:
                try:
                    elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/section/div/button")
                    elem.click()
                    break
                except:
                    'nothing'
            while True:
                try:
                    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/section/div/button').click()
                    break
                except:
                    'nothing'
            print(token, "joined")
            browser.delete_all_cookies()
            browser.quit()

if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=12)
    pool.map(run, tokenlist)
    pool.close()
    pool.join()
    print("DOne")
