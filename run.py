import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from Base import KalosPage
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope="module")

def driver_setup():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "8.1.0",
        "deviceName": "TGZS6PM7UCAYPBZH",
        "appPackage": "com.kwshortvideo.kalostv",
        "appActivity": "com.kwshortvideo.kalostv.ui.main.MainActivity",
        "automationName": "uiautomator2"
    })
    appium_server_url = 'http://192.168.50.40:4723'
    driver = webdriver.Remote(appium_server_url, options=options)
    page = KalosPage(driver)
    sleep(20)
    yield driver,page
    sleep(5)  # 等待5秒以便查看测试结果
    driver.quit()

def test_new_user_guide(driver_setup): # 新手引导测试
    driver,page = driver_setup
    page.xs()  # 在这里执行点击操作
    assert not page.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_confirm"))

def test_hightlights_Like(driver_setup): # 点赞测试
    driver,page = driver_setup
    checkbox = driver.find_element(By.ID, "com.kwshortvideo.kalostv:id/ivLike")
    initial_selected = checkbox.is_selected()
    checkbox.click()
    time.sleep(3)
    after_click_selected = checkbox.is_selected()
    assert initial_selected != after_click_selected

def test_hightlights_shelf(driver_setup): # 收藏测试
    driver,page = driver_setup
    shelf_box = driver.find_element(By.ID, "com.kwshortvideo.kalostv:id/ivCollect")
    initial_selected = shelf_box.is_selected()
    shelf_box.click()
    time.sleep(3)
    after_click_selected = shelf_box.is_selected()
    assert initial_selected != after_click_selected

def test_highlights_Episode(driver_setup):  # highlights切换剧集测试
    driver,page = driver_setup
    episdoe_before = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/tvEpisode")))
    episode_text_before = episdoe_before.text
    page.seekBar(0.9)
    time.sleep(10)
    episode_after = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/tvEpisode")))
    episode_text_after = episode_after.text
    assert episode_text_after != episode_text_before
def test_highlights_Series(driver_setup): #highlights跳转播放器测试
    driver,page = driver_setup
    page.seekBar(0.5)
    episdoe_before = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/tvEpisode")))
    episdoe_before_text = episdoe_before.text
    seekBar_before = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/seekBar")))
    seekBar_before_text = seekBar_before.text
    page.Series()
    page.Bf_xs()
    page.Playerstop()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.invisibility_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/pb")))
    seekBar_after = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/seekBar")))
    seekBar_after_text = seekBar_after.text
    episdoe_after = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "com.kwshortvideo.kalostv:id/tv_progress")))
    episdoe_after_text = episdoe_after.text
    assert seekBar_before_text <= seekBar_after_text and episdoe_before_text == episdoe_after_text
