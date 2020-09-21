# Import dependencies
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser

def init_browser():
    
    # chrome driver path for mac you will have to find yours
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # create dictionary for mongo
    mars_data = {}

    nasa_url = 'https://mars.nasa.gov/news/'
    browser.visit(nasa_url)
    time.sleep(3)
    
    # scrape page
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # get the latest news title and paragraph text - assign variables
    nasa_title = soup.body.find_all('div',class_='content_title')[1].text
    nasa_para = soup.body.find('div',class_='article_teaser_body').text

    #add data to dictionary
    mars_data["nasa_title"] = nasa_title
    mars_data["nasa_para"] = nasa_para

    # Visit the url for JPL Featured Space Image https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars.
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    time.sleep(3)
    # use splinter to click the botton and bring up image    
    results = browser.find_by_id('full_image').first.click()
    time.sleep(5)

    # 
    html = browser.html
    soup = bs(html, 'html.parser')
    img_url = soup.find('img', class_='fancybox-image')['src']
    feature_img_url = 'http://jpl.nasa.gov' + img_url

    # add to dictionary
    mars_data["featured_img_url"] = feature_img_url

    # 
    sp_facts_url = 'https://space-facts.com/mars/'
    browser.visit(sp_facts_url)
    time.sleep(3)
    # read data table with pandas remove unwanted values
    table = pd.read_html(sp_facts_url)
    df = table[0]
    html_table = df.to_html()
    sp_facts_html = html_table.replace('\n', '')

    # add to dictionary
    mars_data["sp_facts_html"] = mars_facts

    # Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
    astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)
    time.sleep(3)

    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.
    hemisphere_image_urls = []

    # use splinter to click link to image and title
    link_list = browser.click_link_by_partial_text('Cerberus')
    time.sleep(3)
   
    # scrape and use soup to find title and image save to variables
    html = browser.html
    soup = bs(html, 'html.parser')
    title_one = soup.body.find('h2', class_='title').text
    img_url = soup.find('img', class_='wide-image')['src']
    cereberus_img = base_url + img_url
    time.sleep(3)

    # save to dictionary
    dictionary = {}
    dictionary["title"] = title_one
    dictionary["img_url"] = cereberus_img
    hemisphere_image_urls.append(dictionary)
    
    # second image and title
    browser.visit(astro_url)
    time.sleep(3)

    # use splinter to click link to image and title
    link_list = browser.click_link_by_partial_text('Schiaparelli')
    time.sleep(3)
   
    # scrape and use soup to find title and image save to variables
    html = browser.html
    soup = bs(html, 'html.parser')
    title_one = soup.body.find('h2', class_='title').text
    img_url = soup.find('img', class_='wide-image')['src']
    schiaparelli_img = base_url + img_url
    time.sleep(3)

    # save to dictionary
    dictionary = {}
    dictionary["title"] = title_two
    dictionary["img_url"] = schiaparelli_img
    hemisphere_image_urls.append(dictionary)

    # third image and title
    browser.visit(astro_url)
    time.sleep(3)

    # use splinter to click link to image and title
    link_list = browser.click_link_by_partial_text('Syrtis')
    time.sleep(3)
   
    # scrape and use soup to find title and image save to variables
    html = browser.html
    soup = bs(html, 'html.parser')
    title_one = soup.body.find('h2', class_='title').text
    img_url = soup.find('img', class_='wide-image')['src']
    syrtis_img = base_url + img_url
    time.sleep(3)

    # save to dictionary
    dictionary = {}
    dictionary["title"] = title_three
    dictionary["img_url"] = syrtis_img
    hemisphere_image_urls.append(dictionary)

    # forth image and title
    browser.visit(astro_url)
    time.sleep(3)

    # use splinter to click link to image and title
    link_list = browser.click_link_by_partial_text('Valles')
    time.sleep(3)
   
    # scrape and use soup to find title and image save to variables
    html = browser.html
    soup = bs(html, 'html.parser')
    title_one = soup.body.find('h2', class_='title').text
    img_url = soup.find('img', class_='wide-image')['src']
    valles_img = base_url + img_url
    time.sleep(3)

    # save to dictionary
    dictionary = {}
    dictionary["title"] = title_four
    dictionary["img_url"] = Valles_img
    hemisphere_image_urls.append(dictionary)

    # 






   
    



    

    
