from pages.home_page import HomePage
from utils.config_reader import ConfigReader

def test_home_page(page):

    home_page = HomePage(page)
    base_url=ConfigReader.get_base_url()

    home_page.open_home_page(base_url)

    assert home_page.is_logo_visible()

    assert "Iqra" in page.title()