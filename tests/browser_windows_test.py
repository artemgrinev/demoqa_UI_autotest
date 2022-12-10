from pages.browser_windows_page import BrowserWindow, AlertPage, FramePage, ModalDialogPage
from pytest_check import check

class TestBrowserWindow:
    def test_open_tab(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window(tab=True)
        assert text == "This is a sample page", "New tab has not opened"

    def test_open_window(self, driver):
        page = BrowserWindow(driver, "https://demoqa.com/browser-windows")
        page.open()
        text = page.check_open_window()
        assert text == "This is a sample page", "New tab has not opened"


class TestAlert:
    def test_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_alert_btn()
        assert text == "You clicked a button"

    def test_time_alert_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_time_alert_btn()
        assert text == "This alert appeared after 5 seconds"

    def test_confirm_alert_click_ok_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn()
        assert text == "You selected Ok"

    def test_confirm_alert_click_no_button(self, driver):
        page = AlertPage(driver, "https://demoqa.com/alerts")
        page.open()
        text = page.click_confirm_btn(cancel_alert=True)
        assert text == "You selected Cancel"


class TestFrame:

    def test_frame(self, driver):
        page = FramePage(driver, "https://demoqa.com/frames")
        page.open()
        result_frame1 = page.check_frame("frame1")
        result_frame2 = page.check_frame("frame2")
        with check:
            assert result_frame1 == ['500px', '350px', 'This is a sample page'], 'The frame does not exist'
        with check:
            assert result_frame2 == ['100px', '100px', 'This is a sample page'], 'The frame does not exist'


class TestModalDialog:
    URL = "https://demoqa.com/modal-dialogs"

    def test_modal_dialog(self, driver):
        page = ModalDialogPage(driver, self.URL)
        page.open()
        modal_width, title_text, len_body = page.check_modal()
        with check:
            assert modal_width == "800", "window size does not match"
        with check:
            assert title_text == "Large Modal"
        with check:
            assert len_body == "574"

    def test_small_modal_dialog(self, driver):
        page = ModalDialogPage(driver, self.URL)
        page.open()
        modal_width, title_text, body_text = page.check_modal(small=True)
        with check:
            assert modal_width == "300"
        with check:
            assert title_text == "Small Modal"
        with check:
            assert body_text == "47"
