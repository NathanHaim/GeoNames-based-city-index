import pandas
import numpy


def merge_cities(name_file_in1, name_file_in2, name_file_in3, name_file_in4, name_file_out):
	"""
	Goal : Merge data from different sources
	Param 1 : cities informations file path
	Param 2 : alter_name informations file path
	Param 3 : countries informations file path
	Param 4 : postcodes informations file path
	Param 5 : merged file output path
	"""
	colomn1 =  ["geonameid", "city_name" ,"latitude","longitude","country_code","population"]
	colomn2 = ["alternateNameId", "geonameid", "alterName", "isPrefered"]
	colomn3 = ["country_code","Country","Capital"]
	colomn4 = ["country_code","postal code","city_name"]
	merge_columns1 = ["geonameid"]
	merge_columns2 = ["country_code"]
	merge_columns3 = ["city_name","country_code"]
	data_file1 = pandas.read_csv(name_file_in1, sep="\t", header = None, low_memory=False)
	data_file2 = pandas.read_csv(name_file_in2, sep="\t", header = None, low_memory=False)
	data_file3 = pandas.read_csv(name_file_in3, sep="\t", header = None, low_memory=False)
	data_file4 = pandas.read_csv(name_file_in4, sep="\t", header = None, low_memory=False)
	data_file1.columns = colomn1
	data_file2.columns = colomn2
	data_file3.columns = colomn3
	data_file4.columns = colomn4
	result = pandas.merge(data_file1, data_file4, on=merge_columns3)
	result = pandas.merge(result, data_file3, on=merge_columns2)
	result = pandas.merge(result, data_file2, on=merge_columns1)
	result.dropna(axis=0, how='all', subset=["geonameid", "Country", "city_name" ,"alterName","latitude","longitude","country_code","population","postal code"])
	result.sort_values(["city_name"], inplace=True)
	result.to_csv(name_file_out, encoding='utf8', sep='\t', index=False)

def group_preparation_to_send(name_file_in, name_file_out):
	"""
	Goal : Prepare data to be send to the Algolia Index
	Param 1 : cities informations file path
	Param 2 : file output path
	"""
	data = pandas.read_csv(name_file_in, sep="\t", low_memory=False)
	data['prefered_name'] = numpy.where(data["isPrefered"] == 1.0, data["alterName"],data["city_name"])
	data['is_capital'] = numpy.where(data["city_name"] == data["Capital"], 1.0, 0.0)
 	data = data.groupby(['geonameid',"city_name","Country"],as_index=False)
 	data = data.agg({
 					'latitude' :lambda x: x.iloc[0],
 					'longitude':lambda x: x.iloc[0],
 					'country_code':lambda x: x.iloc[0],
 					'population':lambda x: x.iloc[0],
 					'postal code':lambda x: x.iloc[0],
 					"Capital" :lambda x: x.iloc[0],
 					"prefered_name":lambda x: x.iloc[0],
 					"is_capital":lambda x: x.iloc[0],
 					"alterName": lambda x: ','.join(x)})
	data.to_csv(name_file_out, encoding='utf8', sep='\t', index=False)