def test_wait_more_than_30_sec(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_pages.open_page_after_wait(3)
    assert desktop_app_auth.demo_pages.check_wait_page()

def test_ajax(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_pages.open_page_and_wait_ajax(2)
    assert 2 == desktop_app_auth.demo_pages.get_ajax_responses_count()

def test_handlers(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_pages.click_new_page_button()
    desktop_app_auth.demo_pages.inject_js()
    desktop_app_auth.navigate_to('Test cases')
    assert desktop_app_auth.demo_pages.check_test_exists('Check new test')
