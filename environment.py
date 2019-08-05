from selenium import webdriver

def before_scenario(context, scenario):
  import ipdb; ipdb.set_trace()
  if 'web' in context.tags:
    # context.browser = webdriver.Firefox()
    context.browser = webdriver.Chrome('tests/resource/drivers/chromedriver')
    context.browser.implicitly_wait(10)

def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()