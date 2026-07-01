from browser_use import Browser


def build_browser(headless=True):
    return Browser(headless=headless)