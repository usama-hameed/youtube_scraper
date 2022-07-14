import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_total_views(driver):
    views = driver.find_element_by_tag_name("ytd-video-view-count-renderer")
    return views.find_element_by_tag_name('span').text


def get_total_likes(driver):
    main_div = driver.find_element_by_id("top-level-buttons-computed")
    likes = main_div.find_element_by_tag_name("ytd-toggle-button-renderer")
    return likes.find_element_by_tag_name("yt-formatted-string").text


def get_posted_date(driver):
    main_div = driver.find_element_by_id("info-strings")
    date = main_div.find_element_by_tag_name("yt-formatted-string")
    return date.text


def get_channel_name(driver):
    channel = driver.find_element_by_class_name("style-scope.ytd-channel-name")
    return channel.text


def get_comments_and_commentors(driver):
    scroll_down()
    main_div = driver.find_element_by_id("contents")
    inner = main_div.find_element_by_class_name("style-scope.ytd-item-section-renderer")
    here = inner.find_element_by_tag_name("ytd-comment-renderer")
    print(here)


def scroll_down():
    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(10)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
    # time.sleep(10)


PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/watch?v=b5jt2bhSeXs")
wait = WebDriverWait(driver, 20)
time.sleep(10)
# wait.until(EC.presence_of_element_located((By.TAG_NAME, "ytd-comments")))
wait.until(EC.presence_of_element_located((By.TAG_NAME, "ytd-item-section-renderer")))

# views = get_total_views(driver)
# likes = get_total_likes(driver)
# posted_date = get_posted_date(driver)
# channel = get_channel_name(driver)
get_comments_and_commentors(driver)
# print(views,likes,channel,posted_date)
driver.quit()
