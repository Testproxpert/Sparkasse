import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver_init")
class TestLogin:
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("testuser", "testpass")
        # Add assertions based on expected post-login behavior
        assert "Dashboard" in driver.title
