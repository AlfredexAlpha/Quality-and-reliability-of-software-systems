#main programm
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import xlsxwriter

class ProductParser: 
    def setupDriver():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    def collectProductLinks(driver):
        driver.get('https://iotvega.com/product/server')
        time.sleep(3)
        elems = driver.find_element(By.XPATH, "//a[@href]")
        links = [elem.get_attribute("href") for elem in elems]
        return list(filter(lambda x : x.find('product/') != -1, links))

    def exportArrayToXls(path, items):
        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 50)
        worksheet.write('A1', 'Products')
        row = 1
        for item in items:
            worksheet.write(row, 0, item)
            row = row + 1
        workbook.close()

    def main(driver):
        driver.maximize_window()
        #1. collect links of products
        links = collectProductLinks(driver)
        for elem in links:
            print(elem)
        #2. export in exile
        exportArrayToXls('C:/Users/zelez/Desktop/KachestvoAndNadezno/products_links.xlsx', links)
        #4.in end
        driver.quit()
    
#ProductParser.main(ProductParser.setupDriver())



#tests
import unittest
import os.path

class TestProductParser(unittest.TestCase):
    def test_init(self):
        driver = ProductParser.setupDriver()
        isHaveDirver = driver is not None
        driver.quit()
        self.assertTrue(isHaveDirver)
    def test_collect_links_in_page(self):
        driver = ProductParser.setupDriver()
        links = ProductParser.collectProductLinks(driver)
        driver.quit()
        self.assertTrue(len(links) > 0)
    def test_export_exls(self):
        links = ['link1', 'link2', 'link3']
        path = 'C:/Users/zelez/Desktop/KachestvoAndNadezno/products_links.xlsx'
        ProductParser.exportArrayToXls(path, links)
        self.assertTrue(os.path.exists(path))


#run tests
unittest.main(argv=[''], verbosity=2, exit=False)