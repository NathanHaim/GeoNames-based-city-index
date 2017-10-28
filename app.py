import luigi
import src.data_processing.clean as clean
import src.data_processing.delete as delete
import src.data_processing.merge as merge
import src.data_processing.send as send

#### PIPES CLEANING FILES
class clean_data_cities(luigi.Task):
    """ File in: cities1000.txt
        File out: cleaned_cities1000.csv
        Task to clean data """ 
    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("pipe_files/cleaned_files/cleaned_cities1000.csv")
 
    def run(self):
        name_file_in = 'pipe_files/entrance_files/cities1000.txt'
        name_file_out = 'pipe_files/cleaned_files/cleaned_cities1000.csv'
        clean.clean_file_cities(name_file_in, name_file_out)


class clean_data_countries(luigi.Task):
    """ File in: countryInfo.txt
        File out: cleaned_countryInfo.csv
        Task to clean  data"""
    def requires(self):
        return []
 
    def output(self):
        return luigi.LocalTarget("pipe_files/cleaned_files/cleaned_countryInfo.csv")
 
    def run(self):
        name_file_in = 'pipe_files/entrance_files/countryInfo.txt'
        name_file_out = 'pipe_files/cleaned_files/cleaned_countryInfo.csv'
        clean.clean_file_countries(name_file_in, name_file_out)


class clean_data_alternate_names(luigi.Task):
    """ File in alternateNames.txt
        File out: cleaned_alternateNames.csv
        Task to clean  data"""
    def requires(self):
        return [clean_data_cities()]

    def output(self):
        return luigi.LocalTarget("pipe_files/cleaned_files/cleaned_alternateNames.csv")

    def run(self):
        name_file_in = 'pipe_files/entrance_files/alternateNames.txt'
        name_file_out = 'pipe_files/cleaned_files/cleaned_alternateNames.csv'
        clean.clean_file_alter(name_file_in, name_file_out)

class clean_data_postcodes(luigi.Task):
    """ File in: postcodes.txt
        File out: cleaned_postcodes.csv
        Task to clean  data"""
    def requires(self):
        return [clean_data_cities()]

    def output(self):
        return luigi.LocalTarget("pipe_files/cleaned_files/cleaned_postcodes.csv")

    def run(self):
        name_file_in = 'pipe_files/entrance_files/postcodes.txt'
        name_file_out = 'pipe_files/cleaned_files/cleaned_postcodes.csv'
        clean.clean_file_postcode(name_file_in, name_file_out)



#### PIPES FILTERING FILES
class delete_data_postcode(luigi.Task):
    """ File out: cleaned_postcodes.csv
        File out: processed_postcodes.csv
    Task to delete useless column and select only cities with population superior than 1000"""
    def requires(self):
        return [clean_data_postcodes()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/processed_files/processed_postcodes.csv")
 
    def run(self):
        name_file_in = 'pipe_files/cleaned_files/cleaned_postcodes.csv'
        name_file_out = 'pipe_files/processed_files/processed_postcodes.csv'
        delete.delete_information_postcode(name_file_in,name_file_out)


class delete_data_cities(luigi.Task):
    """ File in: cleaned_cities1000.csv
        File out: processed_cities1000.csv
        Task to delete useless column and select only cities with population superior than 1000"""
    def requires(self):
        return [clean_data_cities()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/processed_files/processed_cities1000.csv")
 
    def run(self):
        name_file_in = 'pipe_files/cleaned_files/cleaned_cities1000.csv'
        name_file_out = 'pipe_files/processed_files/processed_cities1000.csv'
        delete.delete_information_cities(name_file_in, name_file_out)


class delete_data_alternate_names(luigi.Task):
    """ File in : cleaned_alternateNames.csv
        File out : processed_alternateNames.csv
        Task to delete useless column"""
    def requires(self):
        return [clean_data_alternate_names()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/processed_files/processed_alternateNames.csv")
 
    def run(self):
        name_file_in = 'pipe_files/cleaned_files/cleaned_alternateNames.csv'
        name_file_out = 'pipe_files/processed_files/processed_alternateNames.csv'
        delete.delete_information_alternate_names(name_file_in, name_file_out)

class delete_data_countries_info(luigi.Task):
    """ File in: cleaned_countryInfo.csv
        File out : processed_countryInfo.csv
        Task to delete useless column"""
    def requires(self):
        return [clean_data_countries()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/processed_files/processed_countryInfo.csv")
 
    def run(self):
        name_file_in = 'pipe_files/cleaned_files/cleaned_countryInfo.csv'
        name_file_out = 'pipe_files/processed_files/processed_countryInfo.csv'
        delete.delete_information_countries(name_file_in, name_file_out)

#### PIPES MERGING FILES
class merge_data(luigi.Task):
    """ File in: processed_alternateNames.csv   processed_cities1000.csv processed_countryInfo.csv  processed_postcodes.csv
        File out: merge_cities.csv
    Task to merge files"""
    def requires(self):
        return [delete_data_countries_info(),delete_data_alternate_names(),delete_data_cities(),delete_data_postcode()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/merged_files/merge_cities.csv")
 
    def run(self):
        name_file_in1 = 'pipe_files/processed_files/processed_cities1000.csv'
        name_file_in2 = 'pipe_files/processed_files/processed_alternateNames.csv'
        name_file_in3 = 'pipe_files/processed_files/processed_countryInfo.csv'
        name_file_in4 = "pipe_files/processed_files/processed_postcodes.csv"
        name_file_out = "pipe_files/merged_files/merge_cities.csv"
        merge.merge_cities(name_file_in1, name_file_in2, name_file_in3, name_file_in4, name_file_out)

class aggregate(luigi.Task):
    """ File : merge_cities.csv
        File out : aggregat_ready_to_send.csv
    Task aggregate values"""
    def requires(self):
        return [merge_data()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/aggregat_preparation_to_send/aggregat_ready_to_send.csv")
 
    def run(self):
        name_file_in = "pipe_files/merged_files/merge_cities.csv"
        name_file_out = 'pipe_files/aggregat_preparation_to_send/aggregat_ready_to_send.csv'
        merge.group_preparation_to_send(name_file_in, name_file_out)

#### PIPES SENDING FILES
class main(luigi.Task):
    """ File in: aggregat_ready_to_send.csv
        File out: cities.txt
        Task send each row to the Algolia Index"""
    applicationid = luigi.Parameter()
    adminapikey = luigi.Parameter()
    algoliaindex = luigi.Parameter()

    def requires(self):
        return [aggregate()]
 
    def output(self):
        return luigi.LocalTarget("pipe_files/sended_files/cities.txt")
 
    def run(self):
        file_to_send = "pipe_files/aggregat_preparation_to_send/aggregat_ready_to_send.csv"
        res = send.send(file_to_send, self.applicationid, self.adminapikey, self.algoliaindex)
        print(type(res))
        with open("pipe_files/sended_files/cities.txt","w") as file:
            file.write(repr(res))





if __name__ == '__main__':
    luigi.run()



