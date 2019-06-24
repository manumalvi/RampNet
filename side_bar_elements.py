import time


class next_elements():
    '''
    This class consist the side bar element functions which are present on the UI.
    They are being called by the main class.
    '''
    def __init__(self,driver):
        self.driver = driver
        self.login_username_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[1]/div[2]/input"
        self.login_password_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[2]/div[2]/input"
        self.login_button = "/html/body/app-root/app-login/div/div/form/div[2]/button"
        self.home_button_xpath = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[1]"
        self.playback_xpath    = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[2]"
        self.playback_close_xpath    = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[1]"
        self.playback_calander_xpath = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[3]/div[1]/p-calendar/span/input"
        self.playback_calander_select_date = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[3]/div[1]/p-calendar/span/div/div/div[2]/table/tbody/tr[5]/td[1]/a"
        self.playback_time_xpath = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[3]/div[2]/p-calendar/span/input"
        self.playback_time_box = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[3]/div[2]/p-calendar/span/div/div/div[1]/a[2]"
        self.playback_start = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[4]/div[2]/button"
        self.playback_download_xpath = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/app-play-back/div/div[4]/div[3]/button"
        self.fullscreen = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[5]/div/div[1]/app-menu/ul/li[3]"
        self.zoomin     = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[4]"
        self.zoomout    = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[5]"
        self.map_view    = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[6]"
        self.map_layer   = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[7]"
        self.map_offline = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[5]/div/div[2]/div/div[2]/div[1]"
        self.map_online  = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[5]/div/div[2]/div/div[2]/div[2]"
        self.button_box1 = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[2]/div/div[2]/label[1]/div"
        self.button_box2 = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[2]/div/div[2]/label[2]/div"
        self.button_box3 = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[2]/div/div[2]/label[3]/div"
        self.satellite_view = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[3]/img"
        self.navigator   = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[4]/img"

    def enter_username(self,username):
        self.driver.find_element_by_xpath(self.login_username_xpath).clear()
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.login_password_xpath).clear()
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def home_button(self):
        try:
            print("Clicking on the Home Button....")
            time.sleep(5)
            self.driver.find_element_by_xpath(self.home_button_xpath).click()
            print("home_button : Test PASS")
            time.sleep(2)
        except:
            print("home_button : Test FAIL")
            raise

    def playback_button(self):
        try:
            print("Clicking on the Playback Button....")
            self.driver.find_element_by_xpath(self.playback_xpath).click()
            print("playback_button : Test PASS")
            time.sleep(2)
        except:
            print("playback_button : Test FAIL")
            raise

    def playback_close(self):
        try:
            print("Clicking on the playback close Button....")
            self.driver.find_element_by_xpath(self.playback_close_xpath).click()
            print("playback_close : Test PASS")
            time.sleep(2)
        except:
            print("playback_close : Test FAIL")
            raise

    def playback_calander_open(self,date):
        try:
            self.playback_button()
            print("Clicking on the Playback Calander....")
            #self.driver.find_element_by_xpath(self.playback_calander_xpath).click()
            self.driver.find_element_by_xpath(self.playback_calander_xpath).send_keys(date)
            time.sleep(2)
            print("playback_calander_open : Test PASS")
        except:
            print("playback_calander_open : Test FAIL")
            raise

    def playback_time_open(self,clock):
        try:
            self.playback_button()
            print("Clicking on the Playback time Button....")
            #self.driver.find_element_by_xpath(self.playback_time_xpath).click()
            self.driver.find_element_by_xpath(self.playback_time_xpath).send_keys(clock)
            time.sleep(2)
            print("playback_time_open : Test PASS")
        except:
            print("playback_time_open : Test FAIL")
            raise

    def playback_start_stop(self):
        try:
            self.playback_button()
            print("Clicking on the palyback start stop button....")
            self.driver.find_element_by_xpath(self.playback_calander_xpath).send_keys('20.06.2019')
            time.sleep(2)
            self.driver.find_element_by_xpath(self.playback_time_xpath).send_keys('aaaaa')
            time.sleep(2)
            mm = self.driver.find_element_by_xpath(self.playback_start).is_enabled()
            print(mm)
            #time.sleep(5)
            #self.driver.find_element_by_xpath(self.playback_start).click()
            print("playback_start_stop_button : Test PASS")
        except:
            print("playback_start_stop_button : Test FAIL")
            raise

    def playback_download(self):
        try:
            print("Clicking on the Playback Download button....")
            self.driver.find_element_by_xpath(self.playback_download_xpath).click()
            print("playback_download : Test PASS")
            self.playback_close()
        except:
            print("playback_download : Test FAIL")
            raise

    def click_full_screen(self):
        try:
            print("Clicking on the Full screen button....")
            self.driver.find_element_by_xpath(self.fullscreen).click()
            print("click_full_screen : Test PASS")
            time.sleep(2)
        except:
            print("click_full_screen : Test FAIL")
            raise

    def click_zoom_in(self):
        try:
            print("Clicking on the Zoom in button....")
            self.driver.find_element_by_xpath(self.zoomin).click()
            time.sleep(2)
            print("click_zoom_in : Test PASS")
        except:
            print("click_zoom_in : Test FAIL")
            raise

    def click_zoom_out(self):
        try:
            print("Clicking on the zoom out button....")
            self.driver.find_element_by_xpath(self.zoomout).click()
            time.sleep(2)
            print("click_zoom_out : Test PASS")
        except:
            print("click_zoom_out : Test FAIL")
            raise

    def click_map_view(self):
        try:
            print("Clicking on the Map view button....")
            self.driver.find_element_by_xpath(self.map_view).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.map_view).click()
            print("click_map_view : Test PASS")
        except:
            print("click_map_view : Test FAIL")
            raise

    def click_map_layer(self):
        try:
            print("Clicking on the Map layers buttons....")
            self.driver.find_element_by_xpath(self.map_layer).click()
            print("click_map_layer : Test PASS")
            time.sleep(2)
        except:
            print("click_map_layer : Test FAIL")
            raise

    def gse_check_box(self):
        self.click_map_layer()
        try:
            print("Clicking on the Map layer Box GSE....")
            for i in range(2):
                time.sleep(3)
                self.driver.find_element_by_xpath(self.button_box1).click()
                print("check_box1 : Test PASS")
                time.sleep(3)
        except:
            print("check_box1 : Test FAIL")
            raise

    def flight_check_box(self):
        self.click_map_layer()
        try:
            print("Clicking on the Map layer Box Flight....")
            for i in range(2):
                time.sleep(3)
                self.driver.find_element_by_xpath(self.button_box2).click()
                time.sleep(3)
                print("check_box2 : Test PASS")
        except:
            print("check_box2 : Test FAIL")
            raise

    def geofence_check_box(self):
        self.click_map_layer()
        try:
            print("Clicking on the Map layer Box Geofence....")
            for i in range(2):
                time.sleep(3)
                self.driver.find_element_by_xpath(self.button_box3).click()
                print("check_box3 : Test PASS")
                time.sleep(3)
        except:
            print("check_box3 : Test FAIL")
            raise

    def satellite(self):
        try:
            self.driver.find_element_by_xpath(self.satellite_view).click()
            time.sleep(10)
            print("satellite : Test PASS")
        except:
            print("satellite : Test FAIL")
            raise

    def image_navigator(self):
        try:
            elem = self.driver.find_element_by_xpath(self.navigator)
            if 'ng-hide' in elem.get_attribute('class'):
                print('Navigation is not visible on screen')
                print("image_navigator : Test FAIL")
            else:
                print('Navigation is visible on screen')
                print("image_navigator : Test PASS")
        except:
            print("image_navigator : Test FAIL")
            raise

        #driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
#driver = webdriver.Chrome(executable_path=r'C:\Users\mmalvi\Desktop\chromedriver.exe')
#print ("I am temp file")
# driver.maximize_window()
# driver.get("http://inl00085/")
# next_elements = next_elements(driver)
# next_elements.enter_username("avatar")
# time.sleep(2)
# next_elements.enter_password("qwerty")
# time.sleep(2)
# next_elements.click_login_button()
# time.sleep(2)
# next_elements.home_button()
# time.sleep(2)
# next_elements.playback_button()
# time.sleep(2)
# next_elements.playback_close()
# time.sleep(2)
# next_elements.playback_calander_open("31.05.2019")
# time.sleep(2)
# next_elements.playback_time_open()
# time.sleep(2)
# next_elements.playback_start_stop_button()
# time.sleep(2)
# next_elements.playback_download()
# time.sleep(2)
# next_elements.click_full_screen()
# time.sleep(2)
# next_elements.click_zoom_in()
# time.sleep(2)
# next_elements.click_zoom_out()
# time.sleep(2)
# next_elements.click_map_view()
# time.sleep(2)
# next_elements.click_map_layer()
# time.sleep(2)
# next_elements.check_box1()
# time.sleep(2)
# next_elements.check_box2()
# time.sleep(2)
# next_elements.check_box3()
# time.sleep(2)
# next_elements.click_map_layer()
# time.sleep(2)
# next_elements.satellite()
# time.sleep(2)
# next_elements.image_navigator()

#driver.close()
