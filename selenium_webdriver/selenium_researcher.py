import time
import pickle
from selenium import webdriver
from selenium_webdriver.selenium_results.order import Order
from selenium_webdriver.selenium_results.researcher_result import \
    ResearcherResult

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://allegro.pl/myaccount/')

# Logowanie w serwisie Allegro:
login_box = driver.find_element_by_name('username')
login_box.send_keys('mrfarinq')
password_box = driver.find_element_by_name('password')
password_box.send_keys('Seleniumlab10')
login_box.submit()
time.sleep(7)

# Rozwinięcie listy z opcjami sortowania zamówień.
driver.find_element_by_xpath(".//button[@ng-blur='showDropdown = false']") \
    .click()
time.sleep(5)

# Wybór sortowania - od najwyższej ceny.
driver.find_element_by_xpath("//*[contains(text(), 'od najwyższej')]").click()
time.sleep(5)

# Pobranie zawartości kontenera przechowującego zamówienia.
orders_sections = driver \
    .find_element_by_xpath(".//div[@class='listing ng-scope']") \
    .find_elements_by_xpath(".//section[@class='panel panel-default "
                            "panel-order ng-scope']")

# Wyłuskanie pożądanych elementów charakterystycznych zamówień.
researcherResult = ResearcherResult()
for order_section in orders_sections:
    number_of_elements_in_order = int(order_section.find_element_by_xpath(
        ".//offer-quantity[@class='didascalia-color ng-isolate-scope']")
                                      .text.split(" ", 1)[0])

    researcherResult.orders = Order(
        seller=str(order_section.find_element_by_xpath(
            ".//a[@class='seller-login ng-scope']").text),
        purchase_date=order_section.find_element_by_xpath(
            ".//div[@class='order-status-date ng-binding']").text[13:],
        price=float(order_section.find_element_by_xpath(
            ".//formatted-price[@amount='ctrl.offerPriceAmount']").text[
                    :-3].replace(',', '.')),
        price_with_delivery=float(order_section.find_element_by_xpath(
            ".//formatted-price[@amount='order.totalCost.amount']").text[
                                  :-3].replace(',', '.')),
        number_of_elements=number_of_elements_in_order)

# Rozwinięcie listy z opcjami sortowania zamówień.
driver.find_element_by_xpath(".//button[@ng-blur='showDropdown = false']") \
    .click()
time.sleep(5)

# Wybór sortowania - od najstarszego zamówienia.
driver.find_element_by_xpath(
    "//*[contains(text(), 'od najstarszych')]").click()
time.sleep(5)

# Pobranie zawartości kontenera przechowującego zamówienia.
orders_sections = driver \
    .find_element_by_xpath(".//div[@class='listing ng-scope']") \
    .find_elements_by_xpath(".//section[@class='panel panel-default "
                            "panel-order ng-scope']")

# Wyłuskanie pożądanych elementów charakterystycznych najstarszego zamówienia.
number_of_elements_in_order = int(orders_sections[0].find_element_by_xpath(
    ".//offer-quantity[@class='didascalia-color ng-isolate-scope']")
                                  .text.split(" ", 1)[0])

researcherResult.oldest_order = Order(

    seller=str(orders_sections[0].find_element_by_xpath(
        ".//a[@class='seller-login ng-scope']").text),
    purchase_date=orders_sections[0].find_element_by_xpath(
        ".//div[@class='order-status-date ng-binding']").text[13:],
    price=float(orders_sections[0].find_element_by_xpath(
        ".//formatted-price[@amount='ctrl.offerPriceAmount']").text[
                :-3].replace(',', '.')),
    price_with_delivery=float(orders_sections[0].find_element_by_xpath(
        ".//formatted-price[@amount='order.totalCost.amount']").text[
                              :-3].replace(',', '.')),
    number_of_elements=number_of_elements_in_order)

print("Wynik poszukiwań:")
print(researcherResult.orders)
print("\nIlość zamówień:")
print(len(researcherResult.orders))
print("\nNajstarsze zamówienie:")
print(researcherResult.oldest_order)

try:
    with open('previous_test.pkl', 'rb') as previous_test_result_input:
        previousResearcherResult = pickle.load(previous_test_result_input)
        if researcherResult == previousResearcherResult:
            print("\nWynik testu regresyjnego: pozytywny.")
        else:
            print("\nWynik testu regresyjnego: negatywny.")
            print("\nWynik poszukiwań z poprzedniego testu:")
            print(previousResearcherResult.orders)
            print("\nIlość zamówień z poprzedniego testu:")
            print(len(previousResearcherResult.orders))
            print("\nNajstarsze zamówienie z poprzedniego testu:")
            print(previousResearcherResult.oldest_order)
except FileNotFoundError:
    with open('previous_test.pkl', 'wb') as output:
        pickle.dump(researcherResult, output, pickle.HIGHEST_PROTOCOL)
        print("\nWynik testu regresyjnego: brak (plik z wynikiem poprzedniego"
              "testu nie istnieje).share")


# Rozwinięcie listy z m.in. opcją wylogowania.
driver.find_element_by_xpath(".//button[@class='_iu5pr _z41ha fee54_3GU3E "
                             "fee54_3U14k']") \
    .click()
time.sleep(2)

# Wylogowanie z serwisu Allegro.
driver.find_element_by_xpath(
    "//a[contains(text(),'wyloguj')]").click()

driver.close()
