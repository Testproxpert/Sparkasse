from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    BALANCE = (By.ID, 'accountBalance')
    
    def get_balance(self):
        balance_text = self.find(self.BALANCE).text
        return balance_text
