
import unittest
import filecmp
import glob, os
import src.data_processing.clean as clean

class CitiesCleanTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/cities*.txt"):
			print f
			os.remove(f)

    def test_clean_cities1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/cities1.txt'
        name_file_out = 'test/files_out/cities1.txt'
        name_file_expected = 'test/files_expected/cities1.txt'
        clean.clean_file_cities(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))

    def test_clean_cities2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
    	out : cities2.txt
    	expected : cities2.txt"""
        name_file_in = 'test/files_in/cities2.txt'
        name_file_out = 'test/files_out/cities2.txt'
        name_file_expected = 'test/files_expected/cities2.txt'
        clean.clean_file_cities(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_in,name_file_expected))


class CountriesCleanTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/country_info*.txt"):
			print f
			os.remove(f)

    def test_clean_countries1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/country_info1.txt'
        name_file_out = 'test/files_out/country_info1.txt'
        name_file_expected = 'test/files_expected/country_info1.txt'
        clean.clean_file_countries(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))

    def test_clean_countries2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
    	out : cities2.txt
    	expected : cities2.txt"""
        name_file_in = 'test/files_in/country_info2.txt'
        name_file_out = 'test/files_out/country_info2.txt'
        name_file_expected = 'test/files_expected/country_info2.txt'
        clean.clean_file_countries(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))


class AlterNamesCleanTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/alter_names*.txt"):
			print f
			os.remove(f)

    def test_clean_aternames1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/alter_names1.txt'
        name_file_out = 'test/files_out/alter_names1.txt'
        name_file_expected = 'test/files_expected/alter_names1.txt'
        clean.clean_file_alter(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))

class PostCodesCleanTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.clean.clean_file_cities
    in  : cities1.txt
    out : cities1.txt
    expected : cities1.txt"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/postcodes*.txt"):
			print f
			os.remove(f)

    def test_clean_postcodes1(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities"""

        name_file_in = 'test/files_in/postcodes1.txt'
        name_file_out = 'test/files_out/postcodes1.txt'
        name_file_expected = 'test/files_expected/postcodes1.txt'
        clean.clean_file_postcode(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))

    def test_clean_postcodes2(self):
        """Test le fonctionnement de la fonction src.data_processing.clean.clean_file_cities
        in  : cities2.txt
    	out : cities2.txt
    	expected : cities2.txt"""
        name_file_in = 'test/files_in/postcodes2.txt'
        name_file_out = 'test/files_out/postcodes2.txt'
        name_file_expected = 'test/files_expected/postcodes2.txt'
        clean.clean_file_postcode(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))

if __name__ == '__main__':
	unittest.main()