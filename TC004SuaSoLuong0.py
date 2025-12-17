# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC004SuaSoLuong0(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c004_sua_so_luong0(self):
        driver = self.driver
        driver.get("http://hauiproj.somee.com/Giohang.aspx")
        self.assertEqual(u"Tổng tiền: 1.000.000 VNĐ", driver.find_element_by_id("ContentPlaceHolder1_lblTongTien").text)
        driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_gvGioHang']/tbody/tr[2]").click()
        driver.find_element_by_id("ContentPlaceHolder1_gvGioHang_txtSoLuong_0").clear()
        driver.find_element_by_id("ContentPlaceHolder1_gvGioHang_txtSoLuong_0").send_keys("0")
        driver.find_element_by_xpath(u"//input[@value='Cập nhật']").click()
        self.assertEqual(u"Không có mặt hàng nào trong giỏ hàng!", driver.find_element_by_xpath("//table[@id='ContentPlaceHolder1_gvGioHang']/tbody/tr/td/div").text)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
