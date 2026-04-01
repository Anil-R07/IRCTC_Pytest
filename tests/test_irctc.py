import pytest
from pages.irctc_page import IRCTCPage
from utils.data_reader import load_test_data

test_data = load_test_data("testdata/irctc_data.json")

@pytest.mark.parametrize("data", test_data)
def test_irctc_search(page, data):
    irctc = IRCTCPage(page)

    irctc.open()
    irctc.select_from(data["from"])
    irctc.select_to(data["to"])
    irctc.select_date(data["date"])
    ircctc.select_class(data["class"])
    irctc.click_search()

    trains = irctc.get_train_list()
    print(trains)
    assert len(trains) >= data["expected_min_trains"]