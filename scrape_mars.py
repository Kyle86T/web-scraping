from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pymongo
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)
#executable_path = {'executable_path': 'C:\webdrivers\chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    mars_soup = bs(html, "html.parser")

    # Get the content_title
    content_title = mars_soup.find("div", class_="content_title").text
    latest_content_title=content_title.strip('\n\n')
    # Get the paragraph for the body
    paragraphs = mars_soup.find('div',class_="rollover_description_inner").text
    latest_paragraph= paragraphs.strip('\n\n')
    # Get the img
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(image_url)

    browser.click_link_by_id('full_image')
    browser.click_link_by_partial_text('more info')
    #Getting the featured image
    image_html = browser.html
    mars_image_soup = bs(image_html, 'html.parser')
    image = mars_image_soup.body.find("figure", class_="lede")
    #I want just the image inside the a tag
    link = image.find('a')
    href = link['href']
    base_url='https://www.jpl.nasa.gov'
    #Getting the final url string and saving to variable:
    featured_image_url = base_url + href
    featured_image_url

    time.sleep(1)

    mars_url = "https://space-facts.com/mars/"
    #Reading the facts table into Pandas 
    mars_table = pd.read_html(mars_url)
    df_mars_table = mars_table[0]
    df_mars_table.columns = ["Description", "Value"]
    # df_mars_table
    mars_facts_table=df_mars_table.to_html()
    mars_facts_table

    time.sleep(1)

    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemisphere_url)
    browser.click_link_by_partial_text('Cerberus')
    browser.click_link_by_partial_text('Open')
    hemispheres_html = browser.html
    cerberus_soup = bs(hemispheres_html, 'html.parser')
    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']
    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    cerberus_hemisphere_url = hemisphere_base_url + cerberus_img

    time.sleep(1)

    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemisphere_url)
    browser.click_link_by_partial_text('Schiparelli')
    browser.click_link_by_partial_text('Open')
    hemispheres_html = browser.html
    schiaparelli_soup = bs(hemispheres_html, 'html.parser')
    schiaparelli = schiaparelli_soup.body.find('img', class_ = 'wide-image')
    schiaparelli_img = schiaparelli['src']
    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    schiaparelli_hemisphere_url = hemisphere_base_url + schiaparelli_img

    time.sleep(1)

    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemisphere_url)
    browser.click_link_by_partial_text('Syrtis')
    browser.click_link_by_partial_text('Open')
    hemispheres_html = browser.html
    syrtis_soup = bs(hemispheres_html, 'html.parser')
    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = syrtis['src']
    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    syrtis_hemisphere_url = hemisphere_base_url + syrtis_img

    time.sleep(1)

    mars_hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemisphere_url)
    browser.click_link_by_partial_text('Valles')
    browser.click_link_by_partial_text('Open')
    hemispheres_html = browser.html
    valles_soup = bs(hemispheres_html, 'html.parser')
    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']
    hemisphere_base_url = 'https://astrogeology.usgs.gov'
    valles_hemisphere_url = hemisphere_base_url + valles_img

    hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_hemisphere_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_hemisphere_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_hemisphere_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_hemisphere_url}
    ]
    hemispheres_image_urls

    #Adding in the others in the dictionary
    Mars_dictionary = {
        "latest_title": latest_content_title,
        "latest_paragraph": latest_paragraph,
        "featured_image_url": featured_image_url,
        "mars_facts_table": mars_facts_table,
        # "title": "Valles Marineris Hemisphere", "img_url": valles_hemisphere_url,
        # "title": "Cerberus Hemisphere", "img_url": cerberus_hemisphere_url,
        # "title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_hemisphere_url,
        # "title": "Syrtis Major Hemisphere", "img_url": syrtis_hemisphere_url       
    }
    Mars_dictionary

    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_dictionary
