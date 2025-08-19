# ------------------ IMPORTS ------------------ #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# ------------------ SETUP CHROME OPTIONS ------------------ #
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--log-level=3")  # suppress logs
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# ------------------ DARAZ SCRAPER ------------------ #
def scrape_daraz(product, max_pages=2):
    """
    Scrapes Daraz.pk for the given product across multiple pages.
    """
    product_query = product.replace(' ', '%20')
    scraped_data = []

    for page in range(1, max_pages + 1):
        if page == 1:
            url = f"https://www.daraz.pk/catalog/?q={product_query}"
        else:
            url = f"https://www.daraz.pk/catalog/?q={product_query}&page={page}"

        print(f"Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(3)  # wait for JS to load

        try:
            # Wait until products load
            product_boxes = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Bm3ON"))
            )

            for box in product_boxes:
                try:
                    link_tag = box.find_element(By.TAG_NAME, "a")
                    product_link = link_tag.get_attribute("href")

                    # Open product page in new tab
                    driver.execute_script("window.open(arguments[0]);", product_link)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(2)

                    # Title
                    try:
                        title_element = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "div.pdp-mod-product-badge-wrapper h1.pdp-mod-product-badge-title")
                            )
                        )
                        title = title_element.text
                    except:
                        title = "N/A"

                    # Price
                    try:
                        price_element = driver.find_element(
                            By.CSS_SELECTOR, "span.pdp-price.pdp-price_type_normal"
                        )
                        price = price_element.text
                    except:
                        price = "N/A"

                    scraped_data.append({
                        "title": title,
                        "price": price,
                        "link": product_link
                    })

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                except Exception as e:
                    print("Error scraping product:", e)

        except:
            print(f"No products found on page {page} for '{product}'.")

    return scraped_data

# ------------------ IMTIAZ SCRAPER ------------------ #


def handle_imtiaz_popup(driver):
    try:
        # Wait until popup appears (max 10s)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Select your order type')]"))
        )
        print("Popup detected, handling...")

        # Click Express
        express_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Express')]")
        express_btn.click()
        time.sleep(1)

        # Select City (Karachi is already selected by default in your screenshot)
        # If not, you can click and choose manually:
        # city_input = driver.find_element(By.XPATH, "//input[@placeholder='Select City / Region']")
        # city_input.click()
        # city_input.send_keys("Karachi")
        # time.sleep(1)
        # first_option = driver.find_element(By.XPATH, "//li[contains(text(),'Karachi')]")
        # first_option.click()

        # Open Area dropdown
        area_dropdown = driver.find_element(By.XPATH, "//input[@placeholder='Select Area / Sub Region']")
        area_dropdown.click()
        time.sleep(1)

        # Select the first area option (you can also match exact text if needed)
        first_area = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(@class,'MuiAutocomplete-option')]"))
        )
        first_area.click()
        time.sleep(1)

        # Click the Select button
        select_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Select')]")
        driver.execute_script("arguments[0].click();", select_btn)  # safer than normal click
        time.sleep(2)

        print("Popup handled successfully.")

    except Exception as e:
        print("No popup or already handled:", e)


def scrape_imtiaz(product, max_pages=2):
    product_query = product.replace(' ', '+')
    scraped_data = []

    for page in range(1, max_pages + 1):
        url = f"https://shop.imtiaz.com.pk/search?q={product_query}&page={page}"
        print(f"Scraping page {page}: {url}")
        driver.get(url)
        handle_imtiaz_popup(driver)
        time.sleep(3)  # wait for JS to load

        try:
            # Wait until product boxes load
            product_boxes = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "div.hazle-product-item_product_item__FSm1N")
                )
            )
            print(f"Found {len(product_boxes)} products on page {page}.")
            
            for i in range(len(product_boxes)):
                try:
                    # Re-fetch product boxes to avoid stale elements
                    product_boxes = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, "div.hazle-product-item_product_item__FSm1N")
                        )
                    )
                    box = product_boxes[i]

                    # ---------------- SCRAPE PRICE FROM BOX ---------------- #
                    try:
                        price = box.find_element(By.CSS_SELECTOR, "div.hazle-product-item_product_item_price_label__ET_we > span").text
                    except:
                        price = "N/A"

                    print(f"\nClicking product {i+1}...")
                    driver.execute_script("arguments[0].scrollIntoView(true);", box)
                    driver.execute_script("arguments[0].click();", box)
                    time.sleep(2)  # wait for product page to load

                    # ---------------- SCRAPE TITLE FROM PRODUCT PAGE ---------------- #
                    try:
                        title_element = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "h2.HazleProduct_product_item_name__IX5lz")
                            )
                        )
                        title = title_element.text
                    except:
                        title = "N/A"

                    print(f"Product: {title} | Price: {price}")

                    scraped_data.append({
                        "title": title,
                        "price": price,
                        "link": driver.current_url
                    })

                    driver.back()  # return to search page
                    time.sleep(2)

                except Exception as e:
                    print("Error scraping product:", e)


        except:
            print(f"No products found on page {page} for '{product}'.")

    return scraped_data


# ------------------ MAIN SCRIPT ------------------ #
if __name__ == "__main__":
    products_input = input("Enter product(s) separated by comma: ")
    products_list = [p.strip() for p in products_input.split(',')]

    all_data = []

    for product in products_list:
        # ------------------ Scrape Daraz ------------------ #
        print(f"\nScraping Daraz for: {product}")
        daraz_data = scrape_daraz(product)
        if daraz_data:
            for item in daraz_data:
                item['product_searched'] = product
                item['store'] = 'Daraz'
                all_data.append(item)
        else:
            print("No Daraz results found.")

        # ------------------ Scrape Imtiaz ------------------ #
        print(f"\nScraping Imtiaz for: {product}")
        imtiaz_data = scrape_imtiaz(product)
        if imtiaz_data:
            for item in imtiaz_data:
                item['product_searched'] = product
                item['store'] = 'Imtiaz'
                all_data.append(item)
        else:
            print("No Imtiaz results found.")

    # ------------------ Save to CSV ------------------ #
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv("all_products.csv", index=False, encoding="utf-8")
        print(f"\nScraping completed! Total products saved: {len(all_data)}")

    driver.quit()

    # Dettol Soap,Sprite Drink
