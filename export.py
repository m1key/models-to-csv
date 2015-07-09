from py2neo import Graph, Path
import unicodecsv as csv

get_all_models_and_categories_and_prices = """
MATCH (price:Price)<-[:COSTS]-(product:Product)-[:IS_OF_CATEGORY]->(model_category:ModelCategory)<-[:DOES1]-(model:Model)
MATCH (model_category)-[:DOES2]-(category:Category)
RETURN model.name as model_name, category.name as category_name, price.amount as price_amount ORDER BY model_name, category_name
"""

graph = Graph()

with open('result.csv', 'w') as fp:
	writer = csv.writer(fp, delimiter = ',')
	for record in graph.cypher.execute(get_all_models_and_categories_and_prices):
        	# print record.model_name + '::' + record.category_name + '::' + str(record.price_amount)
		writer.writerow(record)
