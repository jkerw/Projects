#import BeautifulSoup4 as bs4 
# https://www.penzeys.com/shop/spices/
spice_list = {} #creates empty dictionary
spice_history = spice_list

x = 0
is_stopped = False

while not is_stopped:
	spice_name = input('Item Name:\n')
	spice_quant = input('Quantity Needed:\n')
	spice_at_home = input('Quantity in Pantry:\n')
	spice_cost = input('Price per unit:\n')

	#creates key-value pairs for dictionary
	spice_list['name'] = spice_name
	spice_list['number'] = int(spice_quant)
	spice_list['price'] = float(spice_cost)

	spice_history[x] = spice_list.copy() #adds data to list
	exit = input("Forget anything?\nType \'c\' for continue or\'q\' to quit:\n" )
	if exit == 'q':
		is_stopped = True
	else: 
		x+= 1

	#calculate grand total of cost
	total = float(0.00)
	for z in range(0, len(spice_history)-1):
		try:
			item_total = int(spice_history[z].get('number'))*float(spice_history[z].get('price'))
		except KeyError:
			pass
		total += float(item_total)

		try: 
			print(str(spice_history[z]['number'])+' '+ str(spice_history[z]['name'])+'@ $' + str('%.2f' % spice_history[z]['price'])+' ea $'+ str('%.2f' % item_total))
		except KeyError:
			ignoreThis = 10
		item_total=0
	print(str('Grand Total: $%.2f' % total))
	

#webscrape penzey's website or another easy to navigate spice page, like mccormack

#for loop to append to empty list

#function to reset list as needed