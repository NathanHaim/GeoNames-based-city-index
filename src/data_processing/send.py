import pandas
from algoliasearch import algoliasearch




def send(file_to_send, application_id, admin_api_key, algolia_index):
	"""
	Goal : send file content to an Algolia Index
	Parameter 1 : path of the file to send
	Parameter 2 : application id provided by Algolia
	Parameter 3 : admin api key id provided by Algolia
	Parameter 4 : algolia index provided by Algolia
	return id of objects inserted
	"""
	data = pandas.read_csv(file_to_send, sep="\t", low_memory=False)
	list_dat = data.to_dict(orient='records')
	client = algoliasearch.Client(application_id,admin_api_key)
	index = client.init_index(algolia_index)
	res = index.add_objects(list_dat)
	return res
