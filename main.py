


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# base = r"https://adventofcode.com/"

# https://adventofcode.com/{year}/day/2
# https://adventofcode.com/2022/day/2
# r"https://adventofcode.com/2022/day/15/input"

opts = Options()
# only needed if detection fails and you set SE_CHROME_PATH instead:
# opts.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(options=opts)  # Selenium Manager resolves & downloads
driver.get(r"https://adventofcode.com/2022/day/15/input")
print(driver.find_element(By.TAG_NAME, "body").text)
driver.quit()


#idk never mind I'll do this later.

# One-time setup (Windows)
# Close all Chrome windows.
# Pick a dedicated profile folder (to avoid corrupting your daily profile), e.g. C:\Chrome\SeleniumProfile.
# Start Chrome manually once with that folder:
# "C:\Program Files\Google\Chrome\Application\chrome.exe" --user-data-dir="C:\Chrome\SeleniumProfile"



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_driver() -> webdriver.Chrome:
    options = Options()
    options.add_argument(r'--user-data-dir=C:\Chrome\SeleniumProfile')  # your dedicated profile
    # (Optional) If you created multiple Chrome profiles inside that folder:
    # options.add_argument('--profile-directory=Default')
    # Headed is best for OAuth flows; headless may fail 2FA/U2F.
    return webdriver.Chrome(options=options)  # Selenium Manager handles the driver

driver = make_driver()
try:
    driver.get("https://the-site-that-uses-github-oauth.example/")
    # wait for the page that requires auth to finish loading:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print(driver.find_element(By.TAG_NAME, "body").text[:500])
finally:
    driver.quit()
