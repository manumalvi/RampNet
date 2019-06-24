from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

class top_bar_element():
    '''
    This class consist the top bar element functions which are present on the UI.
    They are being called by the main class.
    '''
    def __init__(self,driver):
        self.driver = driver
        self.login_username_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[1]/div[2]/input"
        self.login_password_xpath = "/html/body/app-root/app-login/div/div/form/div[1]/div[2]/div[2]/input"
        self.login_button = "/html/body/app-root/app-login/div/div/form/div[2]/button"
        self.fullscreen = "/html/body/app-root/app-authenticated-pages/app-monitoring/div/app-maps/div/div[6]/div/div[1]/app-menu/ul/li[3]"
        self.time_clock = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/div[1]"
        self.search_box_xpath = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[1]"
        self.enter_search     = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[1]/app-search/div/p-autocomplete/span/input"
        #self.search_points    = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[2]"
        self.search_points = "//*[name()='svg']//*[name()='use' and @*='#searchpoint']"
        self.search_showall   = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[3]/app-menu/ul/li[2]/div"
        self.search_point_add = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[3]/app-menu/ul/li[1]"
        self.delete1 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[2]/div"
        self.delete2 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[3]/div"
        self.delete3 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[4]/div"
        self.delete4 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[5]/div"
        self.delete5 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[6]/div"
        self.delete6 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[7]/div"
        self.delete7 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[8]/div"
        self.delete8 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[9]/div"
        self.delete9 = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[10]/div"
        self.add_new_search   = "//*[@id='searchPointNameField']"
        self.save_and_add     = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[4]/button"
        self.sp_close_button  = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[5]/button[1]"
        self.sp_finish_button = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-search-point/div/div/div[5]/button[2]"
        self.notam_button_xpath = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[3]"
        self.check_notam      = "//*[@id='mat-expansion-panel-header-0']"
        self.filter_xpath     = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[4]"
        self.filter_volations = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[1]/div[1]/app-filter-menu/div/div[2]/div[1]/button"
        self.filter_assets    = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[1]/div[2]/app-filter-menu/div/div[2]/div[1]/button"
        self.filter_operatios = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[1]/div[3]/app-filter-menu/div/div[2]/div[1]/button"
        self.filter_geofence  = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[1]/div[4]/app-filter-menu/div/div[2]/div[1]/button"
        self.filter_apply     = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[2]/button[1]"
        self.filter_reset     = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[1]/app-filter/div[2]/button[2]"
        self.geofence_xpath   = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[5]"
        self.geofence_enter_point_xpath = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[3]/app-menu/ul/li[4]/div"
        self.cancel_enter_point_xpath = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/app-geofence-manual-cord/div/div/div[2]"
        self.geofence_all     = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[3]/app-menu/ul/li[5]/div"
        self.notifications    = "/html/body/app-root/app-authenticated-pages/app-header/div/div[2]/app-menu/ul/li[6]"
        self.past_voilations  = "/html/body/app-root/app-authenticated-pages/app-header/app-slider/div[2]/button"
        self.reports_xpath = "/html/body/app-root/app-authenticated-pages/app-header/div/div[1]/app-nav-bar/div/a[2]/div"
        self.all_violation_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[2]/div[1]/label[1]"
        self.assets_involved_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[2]/div[2]/label[2]"
        self.operators_involved_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[2]/div[3]/label[2]"
        self.violation_by_asset_type_xpath = "//*[@id='raphael-paper-466']/g[1]/g[2]/rect"
        self.dropdown_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[1]/p-dropdown/div/label"
        self.weekly_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[1]/p-dropdown/div/div[4]/div/ul/li[2]/span"
        self.monthly_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[1]/p-dropdown/div/div[4]/div/ul/li[3]/span"
        self.yearly_xpath = "/html/body/app-root/app-authenticated-pages/app-reports/app-report-dashboard/div/div[1]/p-dropdown/div/div[4]/div/ul/li[4]/span"


    def cial_login_page(self):
        try:
            img = self.driver.find_element_by_class_name("login__container__title__logo").is_displayed
            print("Welcome you are at CIAL Login Page, Please enter your Credentials....")
            print("cial_login_page : Test PASS")
        except:
            print("Sorry this is not the CIAL Login Page....")
            print("cial_login_page : Test FAIL")
            raise

    def enter_username(self,username):
        print("Entering the Login USERNAME....")
        self.driver.find_element_by_xpath(self.login_username_xpath).clear()
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)

    def enter_password(self,password):
        print("Entering the Login PASSWORD....")
        self.driver.find_element_by_xpath(self.login_password_xpath).clear()
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(password)

    def click_login_button(self):
        print("Clicking on the Login Button....")
        self.driver.find_element_by_xpath(self.login_button).click()

    def click_full_screen(self):
        try:
            print("Maximizing the login screen size....")
            self.driver.find_element_by_xpath(self.fullscreen).click()
            print("click_full_screen : Test PASS")
        except:
            print("click_full_screen : Test FAIL")
            raise

    def check_time_clock(self):
        try:
            print("Checking the Date and Time Clock....")
            elem = self.driver.find_element_by_xpath(self.time_clock)
            if 'ng-hide' in elem.get_attribute('class'):
                print('Date Time Clock is not visible on screen')
                print("check_time_clock: Test FAIL")
            else:
                print('Date Time Clock is visible on screen')
                print("check_time_clock : Test PASS")
        except:
            print("check_time_clock : Test FAIL")
            raise

    def search_box(self):
        try:
            print("Clicking on the Search button....")
            for i in range(2):
                self.driver.find_element_by_xpath(self.search_box_xpath).click()
                print("search_box : Test PASS")
                time.sleep(2)
        except:
            print("search_box : Test FAIL")
            raise


    def enter_in_search(self):
        try:
            self.search_box()
            print("Searching for the vehicle Name....")
            #self.driver.find_element_by_xpath(self.search_box_xpath).clear()
            var = self.driver.find_element_by_xpath(self.enter_search).send_keys("manu")
            print("enter_in_search : Test PASS")
            time.sleep(2)
        except:
            print("enter_in_search : Test FAIL")
            raise

    def invalid_vehicle_search(self,name):
        try:
            self.search_box()
            self.driver.find_element_by_xpath(self.enter_search).send_keys(name)
            element = self.driver.find_element_by_tag_name("span").text
            print(element)
            if element == "No results Found!!!":
                print("Vehicle Number is Incorrect..")
                print("invalid_vehicle_search : Test PASS")
                self.driver.find_element_by_xpath(self.enter_search).clear()
                time.sleep(2)
            else:
                print("Vehicle Number is Correct....")
                print("invalid_vehicle_search : Test FAIL")
        except:
            print("invalid_vehicle_search : Test FAIL")
            raise

    def valid_vehicle_search(self,name2):
        try:
            self.search_box()
            var = self.driver.find_element_by_xpath(self.enter_search).send_keys(name2)
            print("Exclusive checking the Valid vehicle....")
            #var = self.driver.find_element_by_xpath(self.enter_search).send_keys("A8500")
            #time.sleep(2)
            element = self.driver.find_element_by_tag_name("span").text
            print(element)
            if element == var:
                print("Vehicle Number is Incorrect..")
                print("valid_vehicle_search : Test FAIL")
                time.sleep(2)
            else:
                print("Vehicle Number is Correct....")
                time.sleep(5)
                self.driver.find_element_by_xpath(self.enter_search).send_keys(Keys.ENTER)
                print("valid_vehicle_search : Test PASS")
                time.sleep(2)
        except:
            print("invalid_vehicle_search : Test FAIL")
            raise


    def search_point_button(self):
        try:
            print("Clicking on the Search Points Button....")
            self.driver.find_element_by_xpath(self.search_points).click()
            print("search_point_button : Test PASS")
            time.sleep(3)
        except:
            print("search_point_button : Test FAIL")
            raise


    def search_point_showAll(self):
        try:
            self.search_point_button()
            print("Clicking on the ShowAll button inside Search Points Button....")
            self.driver.find_element_by_xpath(self.search_showall).click()
            time.sleep(5)
            print("Clicking on the Search Points Button to close the showing searches....")
            self.search_point_button()
            time.sleep(2)
            print("search_point_showAll : Test PASS")
        except:
            print("search_point_showAll : Test FAIL")
            raise

    def search_point_Add_button(self):
        try:
            time.sleep(5)
            self.search_point_button()
            print("Clicking on the Add Point button inside Search Points Button....")
            #self.search_point_button()
            self.driver.find_element_by_xpath(self.search_point_add).click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='map']").click()
            time.sleep(3)
            print("search_point_Add_button : Test PASS")
        except:
            print("search_point_Add_button : Test FAIL")
            raise


    def add_new_search_point_without_name(self):
        try:
            self.driver.find_element_by_xpath(self.save_and_add).click()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            time.sleep(2)
            print("To close the wizard, Clicking on close button....")
            self.driver.find_element_by_xpath(self.sp_close_button).click()
            #TODO Fiish button need to use
            print("add_new_search_point_without_name : Test PASS")
        except:
            print("add_new_search_point_without_name : Test FAIL")
            raise


    def add_new_search_point(self,name):
        try:
            self.search_point_Add_button()
            #self.search_point_Add_button().send_keys("manu")
            #self.driver.find_element_by_xpath(self.add_new_search).click()
            self.driver.find_element_by_xpath(self.add_new_search).send_keys(name)
            time.sleep(2)
            self.driver.find_element_by_xpath(self.save_and_add).click()
            time.sleep(2)
            message = self.driver.find_element_by_class_name("popup__message").text
            print(message)
            if message == "Search Point Created Successfully...":
                print("New Search Point is been Added and Saved Successfully....")
                # TODO close button
                time.sleep(2)
            print("add_new_search_point : Test PASS")
        except:
            print("add_new_search_point : Test FAIL")
            raise

    def delete_added_search_point(self):
        try:
            self.search_point_button()
            print("Clicking on the ShowAll button inside Search Points Button....")
            self.driver.find_element_by_xpath(self.search_showall).click()
            time.sleep(2)
            #message = self.driver.find_element_by_class_name("search__point__list__item").text
            message = self.driver.find_element_by_css_selector("div.search__point__list").text
            mm = message.split('\n')
            if 'manu' in mm:
                print("Sample Sp is Present")
                indx = mm.index('manu')
                print(indx)
                if indx == 1:
                    self.driver.find_element_by_xpath(self.delete1).click()
                elif indx == 3:
                    self.driver.find_element_by_xpath(self.delete2).click()
                elif indx == 5:
                    self.driver.find_element_by_xpath(self.delete3).click()
                elif indx == 7:
                    self.driver.find_element_by_xpath(self.delete4).click()
                elif indx == 9:
                    self.driver.find_element_by_xpath(self.delete5).click()
                elif indx == 11:
                    self.driver.find_element_by_xpath(self.delete6).click()
                elif indx == 13:
                    self.driver.find_element_by_xpath(self.delete7).click()
            else:
                print("Search Point is not Present")
            print("delete_added_search_point : Test PASS")
        except:
            print("delete_added_search_point : Test FAIL")
            raise

    def notam_button(self):
        try:
            print("Clicking on NOTAM button....")
            self.driver.find_element_by_xpath(self.notam_button_xpath).click()
            time.sleep(2)
            notam_message = self.driver.find_element_by_class_name("notam__active__title").text
            print(notam_message)
            if notam_message == "ACTIVE NOTAM":
                print("Active Notam is being displayed....")
                print("notam_button : Test PASS")
        except:
            print("notam_button : Test FAIL")
            raise

    def check_the_notam(self):
        try:
            self.driver.find_element_by_xpath(self.notam_button_xpath).click()
            time.sleep(2)
            print("Notam Information will be expanded....")
            self.driver.find_element_by_xpath(self.check_notam).click()
            time.sleep(2)
            print("click_the_notam : Test PASS")
        except:
            print("click_the_notam : Test FAIL")
            raise

    def filter_button(self):
        try:
            print("Clicking on the Filters Button....")
            self.driver.find_element_by_xpath(self.filter_xpath).click()
            time.sleep(2)
            filter_options = ['VIOLATIONS','ASSETS','OPERATORS','GEOFENCE']
            #filter_options = ['ASSETS','OPERATORS','GEOFENCE']
            for i in filter_options:
                if i == 'VIOLATIONS':
                    print("Select Violations....")
                    self.driver.find_element_by_xpath(self.filter_volations).click()
                if i == 'ASSETS':
                    print("Select Assets....")
                    self.driver.find_element_by_xpath(self.filter_assets).click()
                if i == 'OPERATORS':
                    print("Select Operatios....")
                    self.driver.find_element_by_xpath(self.filter_operatios).click()
                if i == 'GEOFENCE':
                    print("Select Geofence....")
                    self.driver.find_element_by_xpath(self.filter_geofence).click()
                    time.sleep(2)
            self.driver.find_element_by_xpath(self.filter_apply).click()
            print("filter_button : Test PASS")
        except:
            print("filter_button : Test FAIL")
            raise


    def filter_reset_button(self):
        try:
            print("Clicking on the Filters Reset Button....")
            self.driver.find_element_by_xpath(self.filter_xpath).click()
            time.sleep(2)
            print("Select Violations....")
            self.driver.find_element_by_xpath(self.filter_volations).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.filter_reset).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.filter_apply).click()
            time.sleep(2)
            print("filter_reset_button : Test PASS")
        except:
            print("filter_reset_button : Test FAIL")
            raise


    def geofence_button(self):
        try:
            print("Clicking on the Geofence Button....")
            self.driver.find_element_by_xpath(self.geofence_xpath).click()
            time.sleep(2)
            print("geofence_button : Test PASS")
        except:
            print("geofence_button : Test FAIL")
            raise

    def geofence_enter_points_button(self):
        self.geofence_button()
        try:
            print("Clicking on the Geofence Enter Point Button....")
            self.driver.find_element_by_xpath(self.geofence_enter_point_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.cancel_enter_point_xpath).click()
            print("geofence_button : Test PASS")
        except:
            print("geofence_button : Test FAIL")
            raise



    def geofence_showall(self):
        try:
            print("Clicking on the Show all Button inside GeoFence Button....")
            self.geofence_button()
            self.driver.find_element_by_xpath(self.geofence_all).click()
            time.sleep(2)
            self.geofence_button()
            print("geofence_showall : Test PASS")
        except:
            print("geofence_showall : Test FAIL")
            raise

    def notification(self):
        try:
            print("Clicking on the Notifications Button....")
            self.driver.find_element_by_xpath(self.notifications).click()
            time.sleep(2)
            print("notification : Test PASS")
        except:
            print("notification : Test FAIL")
            raise

    def mute_unmute_notifications(self):
        try:
            self.notification()
            print("Clicking on the Mute and Unmute Button and checking its Mute or Unmute....")
            notification_volume = self.driver.find_element_by_tag_name("span").text
            print(notification_volume)
            if notification_volume == 'Mute':
                print("Notification Sound is Unmute Now, please check the sound in headsets")
                print("mute_unmute_notifications : Test PASS")
            else:
                print("Notification Sound is mute Now, will not be able to hear notificatio sound")
        except:
            print("mute_unmute_notifications : Test FAIL")
            raise

    def check_notificatios(self):
        try:
            self.notification()
            print("Checking the notificatios if any notification is present or not....")
            check_notification = self.driver.find_element_by_class_name("notifications__empty").text
            print(check_notification)
            if check_notification == 'No Notifications':
                print("There is no new Notification, you can view Past Voilations")
                print("check_notificatios : Test PASS")
            self.driver.find_element_by_xpath(self.notifications).click()
        except:
            print("check_notificatios : Test FAIL")
            raise


    def past_violations_button(self):
        try:
            self.notification()
            print("Checking the past voilations notifications....")
            self.driver.find_element_by_xpath(self.past_voilations).click()
            time.sleep(10)
            print("past_voilations_button : Test PASS")
        except:
            print("past_voilations_button : Test FAIL")
            raise

    def past_violations_close_button(self):
        try:
            self.notification()
            print("Checking the past voilations notifications....")
            self.driver.find_element_by_xpath(self.past_voilations).click()
            time.sleep(10)
            self.driver.find_element_by_class_name("close__past__violation__list").click()
            time.sleep(2)
            print("past_voilations_button : Test PASS")
            self.notification()
        except:
            print("past_voilations_button : Test FAIL")
            raise


    def arinc_logo(self):
        print("Checking the Arinc Logo is present on the screen or not....")
        try:
        #img = self.driver.find_element_by_xpath(self.arinc_logo_xpath).is_displayed
            img = self.driver.find_element_by_class_name("arinc-logo").is_displayed
            print("Aricn Logo Found on the UI")
            print("arinc_logo : Test PASS")
        except Exception:
            print("Arinc logo did not find on UI")
            print("arinc_logo : Test FAIL")
            raise

    def cial_logo_on_header(self):
        print("Checking the CIAL Logo is present on the screen or not....")
        try:
        #img = self.driver.find_element_by_xpath(self.arinc_logo_xpath).is_displayed
            img = self.driver.find_element_by_class_name("header__left__logo").is_displayed
            print("CIAL Logo Found on the header of UI")
            print("cial_logo_on_header : Test PASS")
        except Exception:
            print("CIAL logo did not find on the header of UI")
            print("cial_logo_on_header : Test FAIL")
            raise

    def check_reports(self):
        try:
            print("Clicking on the report page to visualize the reports....")
            self.driver.find_element_by_xpath(self.reports_xpath).click()
            time.sleep(10)
            print("check_reports : Test PASS")
        except:
            print("check_reports : Test FAIL")
            raise

    def all_violations(self):
        self.check_reports()
        try:
            print("Clicking on the All Violations to visualize the Violations....")
            self.driver.find_element_by_xpath(self.all_violation_xpath).click()
            time.sleep(5)
            print("all_violations : Test PASS")
        except:
            print("all_violations : Test FAIL")
            raise

    def assets_involved(self):
        self.check_reports()
        try:
            print("Clicking on the assets involved to visualize the assets involved in violations....")
            self.driver.find_element_by_xpath(self.assets_involved_xpath).click()
            time.sleep(5)
            print("assets_involved : Test PASS")
        except:
            print("assets_involved : Test FAIL")
            raise

    def operators_involved(self):
        self.check_reports()
        try:
            print("Clicking on the opeartors involved to visualize the operators involved in violations....")
            self.driver.find_element_by_xpath(self.operators_involved_xpath).click()
            time.sleep(5)
            print("operators_involved : Test PASS")
        except:
            print("operators_involved : Test FAIL")
            raise

    def violation_by_asset_type(self):
        self.check_reports()
        try:
            print("Clicking on the report page to visualize the reports....")
            #self.driver.find_element_by_xpath(self.violation_by_asset_type_xpath).click()
            self.driver.find_element_by_class_name("raphael-group-1609-caption").click()
            time.sleep(5)
            print("violation_by_asset_type : Test PASS")
        except:
            print("violation_by_asset_type : Test FAIL")
            raise

    def reports_weekly(self):
        self.check_reports()
        try:
            print("Clicking on the report dropdown to visualize the reports on Weekly basis....")
            self.driver.find_element_by_xpath(self.dropdown_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.weekly_xpath).click()
            time.sleep(7)
            print("reports_weekly : Test PASS")
        except:
            print("reports_weekly : Test FAIL")
            raise

    def reports_monthly(self):
        self.check_reports()
        try:
            print("Clicking on the report dropdown to visualize the reports on Monthly basis....")
            self.driver.find_element_by_xpath(self.dropdown_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.monthly_xpath).click()
            time.sleep(7)
            print("reports_monthly : Test PASS")
        except:
            print("reports_monthly : Test FAIL")
            raise

    def reports_yearly(self):
        self.check_reports()
        try:
            print("Clicking on the report dropdown to visualize the reports on Yearly basis....")
            self.driver.find_element_by_xpath(self.dropdown_xpath).click()
            time.sleep(2)
            self.driver.find_element_by_xpath(self.yearly_xpath).click()
            time.sleep(7)
            print("reports_yearly : Test PASS")
        except:
            print("reports_yearly : Test FAIL")
            raise




# driver = webdriver.Chrome(executable_path=r'C:\Users\mmalvi\Desktop\chromedriver.exe')
# print ("I am in top_bar_element file")
#
# driver.maximize_window()
# driver.get("http://inl00085/")
# # top_bar_element = top_bar_element(driver)
# #next_elements = next_elements(driver)
# # top_bar_element.cial_login_page()
# # time.sleep(2)
# top_bar_element.enter_username("avatar")
# time.sleep(2)
# top_bar_element.enter_password("qwerty")
# time.sleep(2)
# top_bar_element.click_login_button()
# time.sleep(2)
# # top_bar_element.click_full_screen()
# # time.sleep(2)
# # top_bar_element.cial_logo_on_header()
# # time.sleep(2)
# # top_bar_element.arinc_logo()
# # time.sleep(2)
# # top_bar_element.check_time_clock()
# # time.sleep(2)
# # top_bar_element.search_box()
# # time.sleep(2)
# # top_bar_element.enter_in_search()
# # time.sleep(2)
# # top_bar_element.invalid_vehicle_search()
# # time.sleep(2)
# # top_bar_element.valid_vehicle_search()
# # time.sleep(2)
# # top_bar_element.search_point_button()
# # time.sleep(2)
# # top_bar_element.search_point_showAll()
# # time.sleep(2)
# # top_bar_element.search_point_Add_button()
# # # top_bar_element.add_new_search_point_without_name()
# # # top_bar_element.add_new_search_point()
# # # top_bar_element.save_and_add_button()
# # top_bar_element.notam_button()
# # time.sleep(2)
# # top_bar_element.check_the_notam()
# # time.sleep(2)
# # top_bar_element.filter_button()
# # time.sleep(2)
# # top_bar_element.filter_reset_button()
# # time.sleep(2)
# # top_bar_element.geofence_showall()
# # time.sleep(2)
# # top_bar_element.notification()
# # time.sleep(2)
# # top_bar_element.mute_unmute_notifications()
# # time.sleep(2)
# # top_bar_element.check_notificatios()
# # time.sleep(2)
# # top_bar_element.past_voilations_button()
# # time.sleep(2)
# # top_bar_element.check_reports()
#
# driver.close()
