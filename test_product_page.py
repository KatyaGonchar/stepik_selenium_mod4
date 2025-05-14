from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    name = page.get_product_name()
    price = page.get_product_price()

    page.should_be_correct_product_in_message(name)
    page.should_be_correct_price_in_message(price)