import bs4
import requests
url = 'https://cooking.nytimes.com/recipes/1020631-thai-inspired-chicken-meatball-soup?action=click&module=Collection%20Page%20Recipe%20Card&region=Easy%20Weeknight%20Soups&pgType=collection&rank=15'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)

########## Ingredients List ##################
food_instructions = soup.find('div', class_= 'recipe-instructions')
quantity = food_instructions.find_all('span', class_= 'quantity')
food = food_instructions.find_all('span', class_= 'ingredient-name')

food_list = []
for green in food:
    fl_stripped = green.text.lstrip().rstrip()
    food_list.append(fl_stripped)

quantity_list = []
for blue in quantity:
    ql_stripped = blue.text.lstrip().rstrip()
    quantity_list.append(ql_stripped)

for qua, foo in zip(quantity_list, food_list):
    print(qua, foo)

print('============================================================================')
################## Instructions ##############
steps = food_instructions.find('section', class_= 'recipe-steps-wrap')
list = steps.find_all('li')
for red in list:
    print(red.text)