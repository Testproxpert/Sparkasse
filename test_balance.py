import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage

@pytest.mark.usefixtures("driver_init")
class TestBalance:
    def test_view_balance(self, driver):
        login_page = LoginPage(driver)
        login_page.login("testuser", "testpass")
        account_page = AccountPage(driver)
        balance = account_page.get_balance()
        assert balance is not None and balance != ''
