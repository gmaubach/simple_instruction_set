import unittest
import pandas as pd
import os
import tempfile
from io import StringIO
from unittest.mock import patch
from source import get_file

class TestGetFile(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = os.path.join(self.temp_dir.name, "test_file.csv")
        self.data = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
        self.data.to_csv(self.temp_file, index=False)
        
    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_csv_file(self):
        # test reading a csv file
        df = get_file(self.temp_file, usecols=['col1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape, (3, 1))
        self.assertEqual(df.columns.tolist(), ['col1'])
        self.assertEqual(df['col1'].tolist(), [1, 2, 3])

    def test_read_excel_file(self):
        # test reading an excel file
        with patch('pandas.read_excel') as mock_read_excel:
            mock_read_excel.return_value = self.data
            df = get_file('test_file.xlsx', usecols=['col1'])
            mock_read_excel.assert_called_once_with(
            'test_file.xlsx',
            engine='openpyxl',
            usecols=['col1'])
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape, (3, 1))
        self.assertEqual(df.columns.tolist(), ['col1'])
        self.assertEqual(df['col1'].tolist(), [1, 2, 3])

    def test_invalid_file_format(self):
        # test invalid file format
        with self.assertRaises(ValueError):
            get_file('test_file.invalid')
            
    def test_print_vars(self):
        # test print_vars argument
        with patch('sys.stdout', new=StringIO()) as fake_out:
            get_file(self.temp_file, print_vars=True)
            expected_output = "Variable names:\n['col1', 'col2']\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

' **./.**

