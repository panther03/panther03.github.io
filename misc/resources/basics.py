import requests
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    driver = webdriver.Chrome('drivers/chromedriver_win32.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    f = open('page_info.txt','w')
    urls = ["https://www.google.com/search?source=hp&ei=7ASnWuf4EsrNjwS1-ouQCQ&q=android+jobs+in+denver&oq=android+jobs+in+denver&gs_l=psy-ab.3..33i22i29i30k1l10.1116.12089.0.12212.61.26.27.6.10.0.110.1775.24j2.26.0....0...1c.1.64.psy-ab..2.59.1966...0j46j0i131k1j0i10k1j0i46k1j0i22i30k1j33i21k1j33i160k1.0.smO-NgSKBKQ",
            "https://www.google.com/search?source=hp&ei=pg2nWvPeMOLjjwTR9aCgBw&q=ASP.net+jobs&oq=ASP.net+jobs&gs_l=psy-ab.3..35i39k1j0l9.32293.35343.0.35552.27.17.8.0.0.0.150.1347.11j4.16.0..2..0...1.1.64.psy-ab..3.24.1462.6..0i227i67k1j0i67k1j0i131k1j0i131i67k1j0i10i67k1j0i20i263k1j0i10k1.69.3bdAw4kXoa4",
            "https://www.google.com/search?ei=zA2nWsrBCMzgjwTg2J-IDA&q=ruby+on+rails+jobs&oq=ruby+on+rails+jobs&gs_l=psy-ab.3..0i20i263k1j0l9.10495.12820.0.12885.22.19.2.0.0.0.163.1767.14j5.19.0....0...1.1.64.psy-ab..1.21.1760...46j35i39k1j0i131k1j0i67k1j0i46k1j0i131i67k1j0i10k1.0.EAzMe4CAO0Y",
            "https://www.google.com/search?ei=2w2nWqbnDejZjwSbnZ2gBg&q=web+developer+jobs&oq=web+dev&gs_l=psy-ab.3.0.0i67k1l7j0i20i263k1j0i67k1l2.10820.29387.0.30168.28.15.12.0.0.0.115.1163.12j2.15.0..2..0...1.1.64.psy-ab..1.27.1323.6..0j35i39k1j0i131k1j0i227i67k1j0i131i46i67k1j46i131i67k1j0i227k1.116.Lm-Nb8UoRo8",
            "https://www.google.com/search?ei=-g2nWrOVKae0jwTIlprgBA&q=java+developer+jobs&oq=java+developer+jobs&gs_l=psy-ab.3..0l4j0i67k1j0l5.7925.10639.0.10759.19.18.0.0.0.0.147.1531.15j3.18.0..2..0...1.1.64.psy-ab..1.18.1514...35i39k1j0i227i67k1j0i227k1j0i131i67k1j0i131k1j0i20i263k1.0.2zEKswNHFKU",
            "https://www.google.com/search?ei=Bw6nWpm-KcHAjwT6lp7ADg&q=sales+analyst+jobs&oq=sales+analyst+jobs&gs_l=psy-ab.3..0l10.27527.29719.0.29833.18.18.0.0.0.0.98.1269.17.17.0..2..0...1.1.64.psy-ab..1.17.1258...35i39k1j0i131i227i67k1j0i227i67k1j0i67k1j0i131k1j0i131i67k1j0i227k1j0i20i263k1.0._FO0Jwy5lq8"]
    try:
        for url in urls:
            driver.get(url)
            element = driver.find_element_by_xpath("/*");
            f.write("==================" + '\n')
            f.write(element.text + '\n')
            time.sleep(random.randint(1,10))
    finally:
        driver.quit()
