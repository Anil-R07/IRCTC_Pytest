from page.irctc_page import IRCTCPage

def test_irctc_search(page):
    irctc = IRCTCPage(page)

    irctc.open()
    irctc.select_from("Bangalore")
    irctc.select_to("Mangalore")
    irctc.select_date(31)
    irctc.click_search()

    trains = irctc.get_train_list()
    print(trains)
    assert len(trains) > 0