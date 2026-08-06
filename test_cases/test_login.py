from selenium.webdriver.common.by import By
import pytest


class TestDashboard:

    @pytest.mark.tc_login_001
    def test_dashboard_title(self, login_setup):

        self.driver = login_setup

        assert self.driver.title == "OrangeHRM"

    def test_dashboard_header(self, login_setup):

        self.driver = login_setup

        dashboard = self.driver.find_element(
            By.XPATH,
            "//h6[text()='Dashboard']"
        ).text

        assert dashboard == "Dashboard"