import model
from model import whole_foods_sale
from model import aldis_au_sale
from model import aldis_us_sale
from model import aldis_uk_sale


def go(inputs, store_name):
	if store_name == 'WholeFoods':
		final_df = whole_foods_sale.items_on_sale()
	elif store_name == 'Aldi AU':
		final_df = aldis_au_sale.items_on_sale()
	elif store_name == 'Aldi US':
		final_df = aldis_us_sale.items_on_sale()
	elif store_name == 'Aldi UK':
		final_df = aldis_uk_sale.items_on_sale()
	return final_df.to_html()
	