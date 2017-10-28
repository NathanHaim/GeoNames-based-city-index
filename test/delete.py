
import unittest
import filecmp
import glob, os
import src.data_processing.delete as delete

class CitiesDeleteTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/delete_cities*.txt"):
			os.remove(f)

    def test_delete_cities1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/delete_cities1.txt'
        name_file_out = 'test/files_out/delete_cities1.txt'
        name_file_expected = 'test/files_expected/delete_cities1.txt'
        delete.delete_information_cities(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

    def test_delete_cities2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
    	out : cities2.txt
    	expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_cities2.txt'
        name_file_out = 'test/files_out/delete_cities2.txt'
        name_file_expected = 'test/files_expected/delete_cities2.txt'
        delete.delete_information_cities(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


class AlterDeleteTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
        for f in glob.glob("test/files_out/delete_alter_names*.txt"):
            os.remove(f)

    def test_delete_alter1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/delete_alter_names1.txt'
        name_file_out = 'test/files_out/delete_alter_names1.txt'
        name_file_expected = 'test/files_expected/delete_alter_names1.txt'
        delete.delete_information_alternate_names(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

    def test_delete_alter2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_alter_names2.txt'
        name_file_out = 'test/files_out/delete_alter_names2.txt'
        name_file_expected = 'test/files_expected/delete_alter_names2.txt'
        delete.delete_information_alternate_names(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


    def test_delete_alter3(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_alter_names3.txt'
        name_file_out = 'test/files_out/delete_alter_names3.txt'
        name_file_expected = 'test/files_expected/delete_alter_names3.txt'
        delete.delete_information_alternate_names(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


    def test_delete_alter4(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_alter_names4.txt'
        name_file_out = 'test/files_out/delete_alter_names4.txt'
        name_file_expected = 'test/files_expected/delete_alter_names4.txt'
        delete.delete_information_alternate_names(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

class CountrieDeleteTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
        for f in glob.glob("test/files_out/delete_cities*.txt"):
            os.remove(f)

    def test_delete_country1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_country_info1.txt'
        name_file_out = 'test/files_out/delete_country_info1.txt'
        name_file_expected = 'test/files_expected/delete_country_info1.txt'
        delete.delete_information_countries(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

    def test_delete_country2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_country_info2.txt'
        name_file_out = 'test/files_out/delete_country_info2.txt'
        name_file_expected = 'test/files_expected/delete_country_info2.txt'
        delete.delete_information_countries(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


class PostCodeDeleteTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
        for f in glob.glob("test/files_out/delete_postcodes*.txt"):
            os.remove(f)

    def test_delete_country1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_postcodes1.txt'
        name_file_out = 'test/files_out/delete_postcodes1.txt'
        name_file_expected = 'test/files_expected/delete_postcodes1.txt'
        delete.delete_information_postcode(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

    def test_delete_country2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
        out : cities2.txt
        expected : cities2.txt"""
        name_file_in = 'test/files_in/delete_postcodes1.txt'
        name_file_out = 'test/files_out/delete_postcodes1.txt'
        name_file_expected = 'test/files_expected/delete_postcodes1.txt'
        delete.delete_information_postcode(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


if __name__ == '__main__':
	unittest.main()