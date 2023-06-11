#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8


import json
import requests
from bs4 import BeautifulSoup
import random
import urllib.request
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import streamlit as st

def get_adjectives():
    url = 'https://prowritingaid.com/art/2299/positive-adjectives.aspx'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        adjectives = []
        for li in soup.find_all('li'):
            adjective = li.get_text().strip()
            if adjective:
                adjectives.append(adjective)

        return adjectives
    else:
        st.error('Произошла ошибка при загрузке страницы')

def get_random_adjective(adjectives):
    filtered_adjectives = [adj for adj in adjectives if ':' in adj]
    new_adjectives = [adj.split(':')[0] for adj in filtered_adjectives if not adj.split(':')[0].isspace() and ' ' not in adj.split(':')[0]]
    return random.choice(new_adjectives)

def get_random_capybara_image(keyword='capybara', orientation='landscape', per_page=10, page=1):
    ACCESS_KEY = 'l8L7RtHq3zRZhCX3mAsCDek0MHx7G64LcQPAzb8sPxY'
    response = requests.get(f'https://api.unsplash.com/search/photos?query={keyword}&orientation={orientation}&per_page={per_page}&page={page}&client_id={ACCESS_KEY}')
    result = json.loads(response.text)
    photo = random.choice(result['results'])
    urllib.request.urlretrieve(photo['urls']['regular'], "example.jpg")
    return Image.open('example.jpg')

def create_capybara_image_with_text(adjective, image):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("midnight.otf", 77)
    text= f"Today you are {adjective.lower()} capybara!"
    text_width, text_height = draw.textsize(text, font=font)
    x = (width - text_width) / 2
    y = height - text_height - 50
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    #urllib.request.urlretrieve(photo['urls']['regular'], "example_with_text.jpg")
    #open('example.jpg', 'a').close()
    #img_with_text = Image.open('example.jpg').convert('RGB')
    image.save('example_with_text.jpg')
    #img_with_text.save('example.jpg')
    img_with_text = Image.open('example_with_text.jpg')
    return img_with_text


def main():
    st.title('Which capybara are you today? Daily horoscope')
    
    adjectives = get_adjectives()
    
    if st.button('Generate adjective'):
        random_adjective = get_random_adjective(adjectives)
        st.write(f'You are {random_adjective} today!')
        
    if st.button('Generate capybara'):
        capybara_image = get_random_capybara_image()
        st.image(capybara_image, caption='Random capybara', use_column_width=True)
        
    if st.button('Generate image with text'):
        random_adjective = get_random_adjective(adjectives)
        capybara_image = get_random_capybara_image()
        capybara_image_with_text = create_capybara_image_with_text(random_adjective, capybara_image)
        st.image(capybara_image_with_text, caption=f'Today you are {random_adjective} capybara!', use_column_width=True)


if __name__ == '__main__':
    main()

