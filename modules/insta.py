from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import time
import random
import os
import zipfile

class InstaBot():

	def __init__(self):
		self.home_url = 'https://www.instagram.com/'
		#self.driver = self.get_driver()
		

		

	def get_proxy(self, proxy):
		# PROXY_HOST = '149.56.44.45'
		# PROXY_PORT = str(random.randint(42000, 42197))
		# PROXY_USER = 'dvpatel7437@gmail.com'
		# PROXY_PASS = 'd0945hkild77'
		#proxy = {'address': PROXY_IP+':'+PORT, 'username': 'dvpatel7437@gmail.com', 'password': 'd0945hkild77'}
		manifest_json = """
			{
			    "version": "1.0.0",
			    "manifest_version": 2,
			    "name": "Chrome Proxy",
			    "permissions": [
			        "proxy",
			        "tabs",
			        "unlimitedStorage",
			        "storage",
			        "<all_urls>",
			        "webRequest",
			        "webRequestBlocking"
			    ],
			    "background": {
			        "scripts": ["background.js"]
			    },
			    "minimum_chrome_version":"22.0.0"
			}
			"""

		background_js = """
		var config = {
		        mode: "fixed_servers",
		        rules: {
		          singleProxy: {
		            scheme: "http",
		            host: "%s",
		            port: parseInt(%s)
		          },
		          bypassList: ["localhost"]
		        }
		      };

		chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

		function callbackFn(details) {
		    return {
		        authCredentials: {
		            username: "%s",
		            password: "%s"
		        }
		    };
		}

		chrome.webRequest.onAuthRequired.addListener(
		            callbackFn,
		            {urls: ["<all_urls>"]},
		            ['blocking']
		);
		""" % (proxy.get('PROXY_HOST'), proxy.get('PROXY_PORT'), proxy.get('PROXY_USER',''), proxy.get('PROXY_PASS',''))
		return manifest_json, background_js

	def get_driver(self, proxy=False):
		path = os.path.dirname(os.path.abspath(__file__))
		options = Options()
		# options.add_argument("headless")
		# options.add_argument("window-size=1920x1080")
		#options.set_headless(headless=True)
		#chrome_options.add_argument("--headless")  
		#chrome_options.add_argument('--disable-gpu')
		if proxy:
			print('getting proxy')
			manifest_json, background_js = self.get_proxy(proxy)
			pluginfile = 'proxy_auth_plugin.zip'
			with zipfile.ZipFile(pluginfile, 'w') as zp:
				zp.writestr("manifest.json", manifest_json)
				zp.writestr("background.js", background_js)
			options.add_extension(pluginfile)

		return webdriver.Chrome(r"./libs/chromedriver", chrome_options=options) #(service_args=service_args, executable_path='libs/phantomjs/phantomjs')


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


	def get_data_proxy(self, data):
		proxy = False
		try:
			p_ip_port = data.get('proxy_ip_port', False)
			if p_ip_port:
				proxy = {
					'PROXY_HOST':p_ip_port.split(':')[0],
					'PROXY_PORT':p_ip_port.split(':')[1],
					'PROXY_USER':'',
					'PROXY_PASS':''
				}
				p_un_pw = data.get('proxy_un_pw',':')
				proxy['PROXY_USER'] = p_un_pw.split(':')[0]
				proxy['PROXY_PASS'] = p_un_pw.split(':')[1]
		except Exception as ex:
			print('ex in get_data_proxy', ex)
			pass

		return proxy


	def run_bulk(self, rows):
		output = []
		c = 0
		for data in rows:
			response = self.run(data)
			output.append(response)
			# if response['success'] or 'proxy' in data.keys():
			# 	self.driver.quit()
			# 	self.driver = self.get_driver()

			c += 1

			# if c % 3 == 0:
			# 	self.driver.quit()
			# 	self.driver = self.get_driver()

		return output
	
	def run(self, data):
		proxy = self.get_data_proxy(data)
		self.driver = self.get_driver(proxy=proxy)
		output = {'email':data['email'], 'success':False, 'message':''}
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

		self.driver.quit()
		return output

# ib = InstaBot()
# ib.run()
