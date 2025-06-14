import pytest
from pages.login_page import LoginPage
from pages.transfer_page import TransferPage

@pytest.mark.usefixtures("driver_init")
class TestTransfer:
    def test_make_transfer(self, driver):
        login_page = LoginPage(driver)
        login_page.login("testuser", "testpass")
        transfer_page = TransferPage(driver)
        transfer_page.make_transfer("recipient123", "100")
        assert transfer_page.transfer_successful()
