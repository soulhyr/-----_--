from selenium import webdriver # 웹 브라우저를 자동화할 수 있는 객체와 함수 제공
from selenium.webdriver.chrome.service import Service # ChromeDriver와 통신하기 위한 Service 클래스
from webdriver_manager.chrome import ChromeDriverManager # ChromeDriver를 자동으로 설치하고 관리하는 클래스
from selenium.webdriver.chrome.options import Options # Chrome webdriver 생성 시 설정하는 옵션을 관리하는 클래스

def setup_headless_chrome():
    # Chrome 옵션 객체 생성 및 설정
    options = Options()
    options.headless = True
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920x1080')

    # ChromeDriverManager를 통해 자동으로 드라이버를 설치하고 서비스 객체 생성
    service = Service(ChromeDriverManager().install())

    # 설정한 옵션과 서비스 객체를 이용하여 Chrome WebDriver 객체 생성
    # 실제 웹 스크래핑을 수행하는 객체
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_website(url):
    driver = setup_headless_chrome()
    driver.get(url)

    # 페이지의 타이틀 출력
    print("Page Title is:", driver.title)

    # 첫 번째 h2 찾기
    header = driver.find_element('xpath', '//h2').text
    print("First Header:", header)

    # WebDriver 종료
    driver.quit()

# 원하는 URL로 변경
scrape_website('https://quotes.toscrape.com/')
