import time

def test_add_to_cart_button_is_existent(browser, language):
	link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
	browser.get(link)
	time.sleep(3)
	assert browser.find_element_by_class_name("btn-add-to-basket"), "Button doesn't exist"
