import pandas as pd
import unittest
from match_files import match_files

class TestMatchFiles(unittest.TestCase):
    def test_match_files_inner_join(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        merged_df = match_files(left_df, right_df, on='A', how='inner')
        expected_df = pd.DataFrame({'A': [2, 3], 'B': ['b', 'c'], 'C': ['x', 'y']})
        pd.testing.assert_frame_equal(merged_df, expected_df)

    def test_match_files_left_join(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        merged_df = match_files(left_df, right_df, on='A', how='left')
        expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [np.nan, 'x', 'y']})
        pd.testing.assert_frame_equal(merged_df, expected_df)

    def test_match_files_right_join(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        merged_df = match_files(left_df, right_df, on='A', how='right')
        expected_df = pd.DataFrame({'A': [2, 3, 4], 'B': ['b', 'c', np.nan], 'C': ['x', 'y', 'z']})
        pd.testing.assert_frame_equal(merged_df, expected_df)

    def test_match_files_outer_join(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        merged_df = match_files(left_df, right_df, on='A', how='outer')
        expected_df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', np.nan], 'C': [np.nan, 'x', 'y', 'z']})
        pd.testing.assert_frame_equal(merged_df, expected_df)

    def test_match_files_no_common_columns(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'C': ['x', 'y', 'z'], 'D': [4, 5, 6]})
        with self.assertRaises(ValueError):
            match_files(left_df, right_df)

    def test_match_files_multiple_common_columns(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [7, 8, 9]})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'B': ['x', 'y', 'z'], 'C': [10, 11, 12]})
        with self.assertRaises(ValueError):
            match_files(left_df, right_df)

    def test_match_files_no_on(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        with self.assertRaises(ValueError):
            match_files(left_df, right_df, on=None)

    def test_match_files_invalid_how(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'A': [2, 3, 4], 'C': ['x', 'y', 'z']})
        with self.assertRaises(ValueError):
            match_files(left_df, right_df, on='A', how='invalid')

    def test_match_files_missing_columns(self):
        left_df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        right_df = pd.DataFrame({'D': [2, 3, 4], 'E': ['x', 'y', 'z']})
        with self.assertRaises(ValueError):
            match_files(left_df, right_df, on='A', how='inner')

if __name__ == '__main__':
    unittest.main()

# **./.**


