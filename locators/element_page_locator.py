from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    ITEM_LIST_OUTPUT = (By.CSS_SELECTOR, "span[class='text-success']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"


class RadioButtonLocators:
    LABEL_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    LABEL_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    LABEL_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTAMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    ROW_PAGE_DROP_DAWN = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    ROWS_TABLE_LIST = (By.XPATH, "//select/*")
    ROWS = (By.CSS_SELECTOR, "div[role='rowgroup']")

    ALL_TABLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

    NO_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")


class ButtonPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    DYNAMIC_CLICK_BUTTON = (By.CSS_SELECTOR, "div[class='mt-4']:nth-child(3) > button")

    DOUBLE_CLICK_MASSAGE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_MASSAGE = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    DYNAMIC_CLICK_MASSAGE = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    # ALL_LINKS = (By.CSS_SELECTOR, "div[id='linkWrapper'] > p > a")
    # SIMPLE_LINKS = (By.CSS_SELECTOR, "a[id='simpleLink']")
    CREATED_LINKS = (By.XPATH, "//*[normalize-space(.)='Created']/a")
    SIMPLE_LINKS = (By.XPATH, "//*[normalize-space(.)='Home']/a")
    NO_CONTENT_LINKS = (By.XPATH, "//*[normalize-space(.)='No Content']/a")
    BAD_REQUEST_LINKS = (By.XPATH, "//*[normalize-space(.)='Bad Request']/a")
    NOT_FOUND_LINKS = (By.XPATH, "//*[normalize-space(.)='Not Found']/a")



