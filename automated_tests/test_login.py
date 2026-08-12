from playwright.sync_api import sync_playwright

def test_saucedemo_login():
    # Start Playwright and open a browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        # Go to the demo website
        page.goto("https://www.saucedemo.com/")

        # Find the username/password boxes and type in the dummy credentials
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Click the login button
        page.click("#login-button")

        # We check if the word "Products" is visible, proving the login was successful
        assert page.is_visible("text=Products"), "Login failed: 'Products' text not found!"

        print("Test Passed: Successfully logged in!")
        
        # Close the browser
        browser.close()

# Run the function
test_saucedemo_login()