from noledgetech import packet, generate_dictionary
import unittest
import re
import pathlib as pl


class TestCaseBase(unittest.TestCase):
    generate_dictionary('/Users/test/internship/dictionaries/PLtoEN.dsv',
                        '/Users/test/internship/dictionaries/ENtoIT.dsv')

    def test_packet_read_from_files(self):
        actual = [packet('/Users/test/internship/dictionaries/PLtoEN.dsv'),
                  packet('/Users/test/internship/dictionaries/ENtoIT.dsv')]
        for i in actual:
            self.assertTrue(re.match("^{(.*:+.*)+}$", str(i)),
                            msg="some file (PLtoEN.dsv or ENtoIT.dsv) is empty, or have wrong form")

    def test_returned_file_exist(self):
        path = '/Users/test/internship/dictionaries/output.dsv'
        actual = pl.Path(path).resolve().is_file()
        self.assertTrue(actual, msg=f"File does not exist: {path}")

    def test_packet_output_not_empty(self):
        self.assertNotEqual(str(packet('/Users/test/internship/dictionaries/output.dsv')).strip(), "{}",
                            msg="the returned file is empty")

    def test_answer_equals_polish_file(self):
        self.assertEqual(len(packet('/Users/test/internship/dictionaries/output.dsv')),
                         len(packet('/Users/test/internship/dictionaries/PLtoEN.dsv')),
                         msg="the returned file and polish file, have a different length")


if __name__ == "__main__":
    unittest.main()
