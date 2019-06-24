import os
import time
import unittest
import HtmlTestRunner
import top_bar_elements
import side_bar_elements
from selenium import webdriver
from LoginPage import LoginPage


class All_Tests(unittest.TestCase):
    '''
    This Class contain all the Test cases we are executing and generating the HTML Result
    Report after the execution completed.
    '''


    def setUp(self):
        #create a new chrome session
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\mmalvi\Desktop\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://inl00085")
        driver = self.driver
        login = LoginPage(driver)

        login.enter_username("avatar")
        time.sleep(2)
        login.enter_password("qwerty")
        time.sleep(2)
        login.click_login_button()
        time.sleep(5)

    def test_1_login_page_valid(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\mmalvi\Desktop\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://inl00085")
        top_bar_elements.top_bar_element.cial_login_page(self)

    def test_2_profile_logo_button(self):
        driver = self.driver
        login = LoginPage(driver)
        login.profile_button()

    def test_3_logout_button(self):
        driver = self.driver
        login = LoginPage(driver)
        login.profile_button()
        login.logout_button()

    def test_4_login_invalid(self):
        driver = self.driver
        login = LoginPage(driver)
        self.test_3_logout_button()
        login.invalid_username()

    def test_5_cial_logo(self):
        top_bar_elements.top_bar_element.cial_logo_on_header(self)

    def test_6_ARINC_logo(self):
        top_bar_elements.top_bar_element.arinc_logo(self)

    def test_7_clock(self):
        top_bar_elements.top_bar_element(self.driver).check_time_clock()

    def test_8_search(self):
        top_bar_elements.top_bar_element(self.driver).search_box()

    def test_9_search_vehicle(self):
        top_bar_elements.top_bar_element(self.driver).enter_in_search()

    def test_10_search_invalid_vehicle(self):
        top_bar_elements.top_bar_element(self.driver).invalid_vehicle_search("manu")

    def test_11_search_valid_vehicle(self):
        top_bar_elements.top_bar_element(self.driver).valid_vehicle_search("A8500")

    def test_12_search_point(self):
        top_bar_elements.top_bar_element(self.driver).search_point_button()

    def test_13_search_point_showall(self):
        top_bar_elements.top_bar_element(self.driver).search_point_showAll()

    def test_14_search_point_add(self):
        top_bar_elements.top_bar_element(self.driver).search_point_Add_button()

    def test_15_add_new_search_point(self):
       top_bar_elements.top_bar_element(self.driver).add_new_search_point('manu')

    def test_16_delete_added_search_point(self):
        top_bar_elements.top_bar_element(self.driver).delete_added_search_point()

    def test_17_notam(self):
        top_bar_elements.top_bar_element(self.driver).notam_button()

    def test_18_notam_info(self):
        top_bar_elements.top_bar_element(self.driver).check_the_notam()

    def test_19_filter_button(self):
        top_bar_elements.top_bar_element(self.driver).filter_button()

    def test_20_filter_reset(self):
        top_bar_elements.top_bar_element(self.driver).filter_reset_button()

    def test_21_geofence_button(self):
        top_bar_elements.top_bar_element(self.driver).geofence_button()

    def test_22_geofence_enter_point(self):
        top_bar_elements.top_bar_element(self.driver).geofence_enter_points_button()

    def test_23_geofence_showall(self):
        top_bar_elements.top_bar_element(self.driver).geofence_showall()

    def test_24_notification_button(self):
        top_bar_elements.top_bar_element(self.driver).notification()

    def test_25_notifications_sound(self):
        top_bar_elements.top_bar_element(self.driver).mute_unmute_notifications()

    def test_26_check_notifications(self):
        top_bar_elements.top_bar_element(self.driver).check_notificatios()

    def test_27_past_violations_notifications(self):
        top_bar_elements.top_bar_element(self.driver).past_violations_button()

    def test_28_past_violations_close(self):
        top_bar_elements.top_bar_element(self.driver).past_violations_close_button()

    def test_29_reports(self):
        top_bar_elements.top_bar_element(self.driver).check_reports()

    def test_30_reports_all_violations(self):
        top_bar_elements.top_bar_element(self.driver).all_violations()

    def test_31_reports_operators_involved(self):
        top_bar_elements.top_bar_element(self.driver).operators_involved()

    def test_32_reports_assets_involved(self):
        top_bar_elements.top_bar_element(self.driver).assets_involved()

    def test_33_reports_weekly_basis(self):
        top_bar_elements.top_bar_element(self.driver).reports_weekly()

    def test_34_reports_monthly_basis(self):
        top_bar_elements.top_bar_element(self.driver).reports_monthly()

    def test_35_reports_yearly_basis(self):
        top_bar_elements.top_bar_element(self.driver).reports_yearly()

    def test_36_full_screen(self):
        top_bar_elements.top_bar_element(self.driver).click_full_screen()

    def test_37_home_button(self):
        side_bar_elements.next_elements(self.driver).home_button()

    def test_38_playback_button(self):
        side_bar_elements.next_elements(self.driver).playback_button()

    def test_39_playback_close(self):
        self.test_38_playback_button()
        side_bar_elements.next_elements(self.driver).playback_close()

    def test_40_playback_calander(self):
        side_bar_elements.next_elements(self.driver).playback_calander_open('20.06.2019')

    def test_41_playback_time(self):
        side_bar_elements.next_elements(self.driver).playback_time_open('09:09 AM')

    def test_42_zoom_in(self):
        side_bar_elements.next_elements(self.driver).click_zoom_in()

    def test_43_zoom_out(self):
        side_bar_elements.next_elements(self.driver).click_zoom_out()

    def test_44_map_view_button(self):
        side_bar_elements.next_elements(self.driver).click_map_view()

    def test_45_map_layer_button(self):
        side_bar_elements.next_elements(self.driver).click_map_layer()

    def test_46_map_layer_gse(self):
        side_bar_elements.next_elements(self.driver).gse_check_box()

    def test_47_map_layer_flight(self):
        side_bar_elements.next_elements(self.driver).flight_check_box()

    def test_48_map_layer_geofence(self):
        side_bar_elements.next_elements(self.driver).geofence_check_box()

    def test_49_satellite_view(self):
        side_bar_elements.next_elements(self.driver).satellite()

    def test_50_image_navigator(self):
        side_bar_elements.next_elements(self.driver).image_navigator()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results_dir'))

