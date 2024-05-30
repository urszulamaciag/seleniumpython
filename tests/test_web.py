from fixtures.chrome import chrome_browser
from fixtures.edge import edge_browser


# Test - uruchomienie Chroma
def test_my_first_chrome_selenium(chrome_browser):
    chrome_browser.set_window_size(1920, 1080)
    chrome_browser.get('http://demo.testarena.pl/zaloguj')
    assert 'TestArena' in chrome_browser.title


def test_title_on_ftfs(chrome_browser):
    chrome_browser.get('https://www.ftfs.it/')
    assert 'Friday Tips for Seniors' in chrome_browser.title


def test_my_first_edge_selenium(edge_browser):
    edge_browser.get('https://www.ftfs.it/')
