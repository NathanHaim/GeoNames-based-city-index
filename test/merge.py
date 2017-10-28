
import unittest
import filecmp
import glob, os
import src.data_processing.merge as merge

class CitiesMergeTest(unittest.TestCase):

    """Test case utilise pour tester la fonction src.data_processing.merge.merge_cities"""
    @classmethod
    def setUpClass(cls):
		for f in glob.glob("test/files_out/merge_cities*.txt"):
			os.remove(f)

    def test_merge_cities1(self):
        """Test le fonctionnement de la fonction src.data_processing.merge.merge_cities"""

        name_file_in1 = 'test/files_in/merge_cities1.txt'
        name_file_in2 = 'test/files_in/merge_alter_names1.txt'
        name_file_in3 = 'test/files_in/merge_country_info1.txt'
        name_file_in4 = "test/files_in/merge_postcodes1.txt"
        name_file_out = "test/files_out/merge_cities1.txt"
        name_file_expected = "test/files_expected/merge_cities1.txt"
        merge.merge_cities(name_file_in1, name_file_in2, name_file_in3, name_file_in4, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))

    def test_aggregat_cities1(self):
        """Test le fonctionnement de la fonction src.data_processing.merge.merge_cities"""

        name_file_in = 'test/files_in/aggregat_cities1.txt'
        name_file_out = 'test/files_out/aggregat_cities1.txt'
        name_file_expected = "test/files_expected/aggregat_cities1.txt"
        merge.group_preparation_to_send(name_file_in, name_file_out)
        self.assertTrue(filecmp.cmp(name_file_out,name_file_expected), "{} and {} are not similar".format(name_file_out,name_file_expected))




if __name__ == '__main__':
	unittest.main()