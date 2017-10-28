import pandas
import shutil

def delete_information_cities(name_file_in, name_file_out):
	"""delete data currently useless, duplicates and cities with less than 2001 peoples"""
	columns = ["geonameid", "asciiname", "alternatenames", "latitude", "longitude","feature class","feature code" ,
	                "country code" ,"population" ,"dem" ,"timezone","modification date" ]
	columns_useless = ["alternatenames","feature class","feature code" , "dem" ,"timezone","modification date"]
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	for col in columns_useless:
		del data[col]
	data = data[data.population > 2000]
	data = data.drop_duplicates()
	data.to_csv(name_file_out, encoding='utf8', sep='\t', header= False, index=False)


def delete_information_alternate_names(name_file_in, name_file_out):
	"""delete data currently useless and duplicates"""
	columns = ["alternateNameId", "geonameid", "alterName","isPrefered"]
	column_match_drop = ["geonameid", "alterName"]
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	data.sort_values(["isPrefered"],  ascending=False, inplace=True)
	data = data.drop_duplicates(column_match_drop)
	data.to_csv(name_file_out, encoding='utf8', sep='\t', header= False, index=False)

def delete_information_countries(name_file_in, name_file_out):
	"""just copy the file ready for the enxt step"""
	shutil.copyfile(name_file_in,name_file_out)


def delete_information_postcode(name_file_in, name_file_out):
	"""just copy the file ready for the enxt step"""
	shutil.copyfile(name_file_in,name_file_out)