from appium import webdriver
from appium.options.common.base import AppiumOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import  time

class KalosPage:
    def __init__(self, driver):
        self.driver = driver

    def find_and_click(self, locator, timeout=20):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            element.click()
            return True
        except TimeoutException:
            print("元素点击失败")
            return False

    def xs(self):  # highlights新手引导
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tvRetry"))
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_step1"))
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_switch"))
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_confirm"))

    def Bf_xs(self):  # 播放器新手引导
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_step1"))
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_switch"))
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/tv_confirm1"))

    def seekBar(self,size):  # 进度条拖动
        progress = WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located((By.ID, "com.kwshortvideo.kalostv:id/seekBar")))#设置了显性等待
        # 找到进度条元素
        progress_bar = self.driver.find_element(By.ID, "com.kwshortvideo.kalostv:id/seekBar")
        # 获取进度条的位置和尺寸
        progress_bar_location = progress_bar.location_in_view
        progress_bar_size = progress_bar.size
        # 计算滑动的起始点和结束点
        start_x = progress_bar_location['x'] + progress_bar_size['width'] * 0.2
        end_x = progress_bar_location['x'] + progress_bar_size['width'] * size
        y = progress_bar_location['y'] + progress_bar_size['height'] * 0.5
        # 创建 MobileTouchAction 实例
        action = ActionChains(self.driver)
        # 按住进度条并拖动
        action.click_and_hold(progress_bar).move_by_offset(end_x - start_x, 0).release().perform()
    def dz(self):
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/ivLike"))

    def shelf(self):
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/ivCollect"))

    def Playerstop(self):
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/exo_subtitles"))

    def hd(self):#滑动动作
        # 获取屏幕的宽度和高度
        screen_width = self.driver.get_window_size()['width']
        screen_height = self.driver.get_window_size()['height']
        # 设置滑动的起始点和结束点
        start_x = screen_width // 2  # 屏幕宽度的一半
        start_y = int(screen_height * 0.8)  # 屏幕高度的80%
        end_y = int(screen_height * 0.2)  # 屏幕高度的20%
        # 执行向上滑动操作
        self.driver.swipe(start_x, start_y, start_x, end_y, duration=1000)

    def zt(self):
        self.find_and_click((By.XPATH, '//android.widget.FrameLayout[@resource-id="com.kwshortvideo.kalostv:id/exo_subtitles"]/android.view.View'))
    def Series(self):
        self.find_and_click((By.ID, "com.kwshortvideo.kalostv:id/series"))
    def Home(self):
        self.find_and_click((By.XPATH,"//android.widget.TextView[@resource-id=\"com.kwshortvideo.kalostv:id/tab_down_text\" and @text=\"Home\"]"))
    def get_initial_progress(self):
        progress_bar = self.driver.find_element(By.ID, "com.kwshortvideo.kalostv:id/seekBar")
        return progress_bar.get_attribute("value")

    def get_progress(self):
        progress_bar = self.driver.find_element(By.ID,"com.kwshortvideo.kalostv:id/seekBar")
        return progress_bar.get_attribute("value")
def myFindElement(self, by1, ele):
    poplist = [
        (By.ID, "com.kwshortvideo.kalostv:id/ivClose"),
        (By.ID,"com.kwshortvideo.kalostv:id/tvRetry"),
        # 可以继续添加其他弹窗元素
    ]
    try:
        return self.driver.find_element(by1, ele)
    except Exception as e:
        print('没有定位到元素，处理弹窗异常')
        for pop in poplist:
            elements = self.driver.find_elements(*pop)
            if elements:
                for element in elements:
                    try:
                        element.click()
                        print("关闭一个弹窗成功")
                    except Exception as e:
                        print("关闭弹窗失败: {str(e)}")
                # 继续捕捉异常
                return self.myFindElement(by1, ele)
        print("未找到弹窗元素或目标元素")
        return None

def get_initial_progress(self):
    progress_bar = self.driver.find_element(By.ID, "com.kwshortvideo.kalostv:id/seekBar")
    return progress_bar.get_attribute("value")

def get_progress(self):
    progress_bar = self.driver.find_element(By.ID,"com.kwshortvideo.kalostv:id/seekBar")
    return progress_bar.get_attribute("value")