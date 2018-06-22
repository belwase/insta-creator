from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time

class InstaBot():

	def __init__(self):
		self.home_url = 'https://www.instagram.com/'
		options = Options()
		# options.add_argument("headless")
		# options.add_argument("window-size=1920x1080")
		# options.set_headless(headless=True)
		#chrome_options.add_argument("--headless")  
		#chrome_options.add_argument('--disable-gpu')
		self.driver = webdriver.Chrome(r"./libs/chromedriver", chrome_options=options) #(service_args=service_args, executable_path='libs/phantomjs/phantomjs')

	def waitElement(self, selector, by_type='CSS', _timeout=10):
		try:
			_by_type = By.CSS_SELECTOR
			if by_type == 'xpath':
				_by_type = By.XPATH
			element_present = EC.presence_of_element_located((_by_type, selector))
			WebDriverWait(self.driver, _timeout).until(element_present)
		except Exception as ex:
			print ("Timed out waiting for page to load", ex, selector)


	def fillText(self, name, value, regex=False):
	        element = False
	        if regex:
	            element = self.driver.find_element_by_css_selector("input[name^=%s]"%name)
	        else:
	            element = self.driver.find_element_by_css_selector("input[name=%s]"%name)
	        element.clear()
	        element.send_keys(value)

	def fillSelect(self, name, value, regex=False):
	        css = "select[name=%s] > option[value='%s']"%(name,value)
	        if regex:
	            css = "select[name^=%s] > option[value='%s']"%(name,value)
	        try:
	            self.driver.find_element_by_css_selector(css).click()
	        except:
	            pass

	def fillRadio(self,name=False, value=True):
		selector = "input[type='radio'][value='{}']".format(value)
		if name:
			selector = "input[name='{}'][value='{}']".format(name, value)
		try:
			self.driver.find_element_by_css_selector(selector).click()
		except:
			pass

	
	def run(self, data):

		output = {'success':False, 'message':''}
		try:
			# data = {
			# 	'email' : 'test@gmail.com', #'test13411@gmail.com',
			# 	'password' : '12eafe5678@12@',
			# 	'fullName' : 'test g'
			# 	}
			# data['username'] = data['email'].split('@')[0]

			self.driver.get(self.home_url)
			#time.sleep(2)
			
			self.waitElement("input[name=emailOrPhone]")
			self.fillText("emailOrPhone", data['email'])
			self.fillText("fullName", data['fullname'])
			self.fillText("username", data['username'])
			self.fillText("password", data['password'])

			self.driver.save_screenshot("screenshot.png")


			# button = WebDriverWait(self.driver, 20).until(
			# 	EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Sign up')]")));

			buttons = self.driver.find_elements_by_css_selector('button')#[class="_5f5mN       jIbKX KUBKM      yZn4P   "]')
			for button in buttons:
				if 'sign up' in button.text.lower():
					button.click()


			self.driver.save_screenshot("screenshot2.png")
			try:
				self.driver.save_screenshot("screenshot3.png")
				self.waitElement("a[href='/{}/']".format(data['username']))
				profile = self.driver.find_element_by_css_selector("a[href='/{}/']".format(data['username']))
				output['success'] = True
				print('account created')
				##success !! account created
				## <a class="Szr5J kIKUG coreSpriteDesktopNavProfile" href="/test13411/">Profile</a>
				# <a href="/accounts/activity/" class="_0ZPOP kIKUG coreSpriteDesktopNavActivity  "><span class="Szr5J">Activity Feed</span></a>

			except Exception as e:
				try:
					self.waitElement('p[id=ssfErrorAlert]', _timeout=5)
					error = self.driver.find_element_by_css_selector('p[id=ssfErrorAlert]')
					self.driver.save_screenshot("screenshot3.png")
					output['message'] = error.text
				except Exception as ex:
					output['message'] = 'Unable to create account'
					
				
		except Exception as ex:
			output['message'] = str(ex)

		return output

# ib = InstaBot()
# ib.run()
