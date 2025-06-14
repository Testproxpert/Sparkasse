from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TransferPage(BasePage):
    RECIPIENT = (By.ID, 'recipient')
    AMOUNT = (By.ID, 'amount')
    TRANSFER_BUTTON = (By.ID, 'transferButton')
    SUCCESS_MSG = (By.ID, 'transferSuccess')
    
    def make_transfer(self, recipient, amount):
        self.type(self.RECIPIENT, recipient)
        self.type(self.AMOUNT, amount)
        self.click(self.TRANSFER_BUTTON)
    def transfer_successful(self):
        return self.find(self.SUCCESS_MSG) is not None
