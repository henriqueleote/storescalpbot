from undetected_chromedriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup

# Configure Chrome options
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome driver
driver = Chrome(options=options)

# Set the URL to retrieve the HTML source code
url = "https://www.radiopopular.pt/categoria/computadores-portateis/"
# Open the URL in Chrome
driver.get(url)

# Get the HTML source code
html_source = driver.page_source

# Quit the driver
driver.quit()

# Parse the HTML source code
soup = BeautifulSoup(html_source, 'html.parser')

# Define keywords to search for
keywords = ['iphone', '€']

# Define tags to exclude from search
exclude_tags = ['body', 'head', 'header', 'nav']

# Find all parent elements with more than 20 children, an even number of children, and exclude specified tags
parent_elements = soup.find_all(
    lambda tag: (
        len(tag.find_all(recursive=False)) >= 10
        #and len(tag.find_all(recursive=False)) % 2 == 0
        and not tag.find('input', {'type': 'checkbox'})
        and tag.name not in exclude_tags
    )
)

filtered_parent_elements = []

for parent in parent_elements:
    if parent.find('a') and parent.find('img') and "benefits" not in str(parent) and "loyalty" not in str(parent) and "<nav" not in str(parent) and "category" not in str(parent):
        filtered_parent_elements.append(parent)

# Filter parent elements based on the presence of <a> tag among their children
filtered_parent_elements = [
    parent for parent in filtered_parent_elements if parent.find('a')
]

# Print the parent elements
for parent in filtered_parent_elements:
    parent_tag = parent.name
    print(f"Parent Element (Tag: {parent_tag}):")
    print(parent)
    print()
