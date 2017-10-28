import pandas
import numpy


def clean_file_cities(name_file_in,name_file_out):
	""" File : cities1000.txt
	Parameter 1 : path of file to clean
	Parameter 2 : path to save file cleaned
    Task to clean data """ 
	columns = ["geonameid", "name", "asciiname", "alternatenames", "latitude", "longitude","feature class","feature code" ,
	            		"country code", "cc2","admin1 code","admin2 code","admin3 code","admin4 code" ,"population" ,
	            		"elevation" ,"dem" ,"timezone","modification date" ]
	columns_unusable = ['name','cc2','admin1 code','admin2 code','admin3 code','admin4 code','elevation']
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	for col in columns_unusable:
		del data[col]
	data.to_csv(name_file_out, encoding='utf8', sep="\t", header= False, index=False)


def clean_file_countries(name_file_in, name_file_out):
	""" File : countryInfo.txt
	Parameter 1 : path of file to clean
	Parameter 2 : path to save file cleaned
    Task to clean data """ 
	columns = ["ISO","ISO3","ISO-Numeric","fips","Country","Capital", "Area","Population",
	          	"Continent","tld","CurrencyCode","CurrencyName","Phone","Postal Code Format",
	            "Postal Code Regex","Languages","geonameid","neighbours","EquivalentFipsCode"]            
	columns_unusable =  ["ISO3","ISO-Numeric","fips","Area","Population",
	            			"Continent","tld","CurrencyCode","CurrencyName","Phone","Postal Code Format",
	            			"Postal Code Regex","Languages","geonameid","neighbours","EquivalentFipsCode"]
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	for col in columns_unusable:
		del data[col]
	data.to_csv(name_file_out, encoding='utf8', sep="\t", header= False, index=False)


def clean_file_alter(name_file_in,name_file_out):
	""" File : alterNames.txt
	Parameter 1 : path of file to clean
	Parameter 2 : path to save file cleaned
    Task to clean data """ 
	columns = ["alternateNameId", "geonameid", "isolanguage", "alterName","isPrefered","u2","u3","u4"]
	columns_unusable = ["isolanguage","u2","u3","u4"]
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	data = data[data.isolanguage != "link"]
	data = data[data.isolanguage != "post"]
	for col in columns_unusable:
		del data[col]
	data['isPrefered'].fillna(0, inplace=True)
	data.to_csv(name_file_out, encoding='utf8', sep="\t", header= False, index=False)


def clean_file(name_file_in, name_file_out, columns, columns_unusable):
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	for col in columns_unusable:
		del data[col]
	data.to_csv(name_file_out, encoding='utf8', sep="\t", header= False, index=False)


def clean_file_postcode(name_file_in, name_file_out):
	""" File : postcodes.txt
	Parameter 1 : path of file to clean
	Parameter 2 : path to save file cleaned
    Task to clean data """ 
	columns = ["country code","postal_code","place name","admin name1","admin code1","admin name2","admin code2","admin name3","admin code3","latitude","longitude","accuracy"]         
	columns_unusable = ["admin name1","admin code1","admin name2","admin code2","admin name3","admin code3","latitude","longitude","accuracy"]
	data = pandas.read_csv(name_file_in, sep="\t", header = None, low_memory=False)
	data.columns = columns
	data = data.applymap(str)
	data = data[~data.postal_code.str.contains("CEDEX")]
	data = data.drop_duplicates(["place name","admin name1"])
	for col in columns_unusable:
		del data[col]
	data.to_csv(name_file_out, encoding='utf8', sep="\t", header= False, index=False)     
     	

      
     



            
    
          
     
