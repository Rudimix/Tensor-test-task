from Pages import SearchHelper

def test_tensor_search(driver):
    helper = SearchHelper(driver)
    helper.go_to_site()
    helper.click_contacts()
    helper.click_tensor_icon()
    helper.click_about()
    check=helper.check_photos()
    assert check == True