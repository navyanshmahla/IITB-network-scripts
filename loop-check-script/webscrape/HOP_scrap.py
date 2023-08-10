from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def HOP_scrap(wing , floor, side):
    str_wing = "Wing " + str(wing)
    if int(floor) in [0, 1]:
        str_floor = "Floor 0,1"
    else:
        str_floor = "Floor " + str(floor)


    wing_floor_str = str_wing+" "+side+", "+str_floor
    # URL of the target page
    url = "https://cc.iitb.ac.in"

    options = Options()
    options.add_argument("--headless=new")
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)  # You need to download and provide the path to the Chrome driver executable
    
    # Open the URL in the WebDriver
    driver.get(url)

    # Find the link to "IP Allocation" tab
    wait = WebDriverWait(driver, 15)
    ip_allocation_link = wait.until(EC.presence_of_element_located((By.ID, "ipalloc-tab")))
    ip_allocation_link.click()

    hostel_allocation_link = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Hostel IP Allocation")))
    print(wing_floor_str)
    if hostel_allocation_link:
        # Click on the "IP Allocation" link
        hostel_allocation_link.click()

        # Hostel selection
        select_hostel = wait.until(EC.presence_of_element_located((By.ID, 'ddlHostel')))
        select_hostel = Select(select_hostel)
        select_hostel.select_by_visible_text('Hostel 02')

        select_wing = wait.until(EC.presence_of_element_located((By.ID, 'ddlHostelWing')))
        select_wing = Select(select_wing)
        select_wing.select_by_visible_text(wing_floor_str)

        # Define the xpaths for the hop text and value elements
        hop_text_xpaths = [
            '//*[@id="HosHOPPart"]/tbody/tr[1]/td[1]/strong',
            '//*[@id="HosHOPPart"]/tbody/tr[2]/td[1]/strong',
            '//*[@id="HosHOPPart"]/tbody/tr[3]/td[1]/strong',
            '//*[@id="HosHOPPart"]/tbody/tr[4]/td[1]/strong',
            '//*[@id="HosHOPPart"]/tbody/tr[5]/td[1]/strong'
        ]

        hop_value_xpaths = [
            '//*[@id="lblhoshop1"]',
            '//*[@id="lblhoshop2"]',
            '//*[@id="lblhoshop3"]',
            '//*[@id="lblhoshop4"]',
            '//*[@id="lblhoshop5"]'
        ]

        # Create the dictionary
        hop_dict = {}

        # Loop through the xpaths and find the elements
        for i in range(len(hop_text_xpaths)):
            hop_text = driver.find_element(By.XPATH, hop_text_xpaths[i]).text
            hop_value = driver.find_element(By.XPATH, hop_value_xpaths[i]).text
            hop_dict[hop_text] = hop_value

    driver.quit()
    return hop_dict

    

# Call the function
#print(HOP_scrap(4, 2, "Left"))
