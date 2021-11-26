import unittest

import filters
from processor import DatasetFilter


class MyTestCase(unittest.TestCase):

    def test_filtering(self):

        filters_list = ["filter_odd", "filter_alphakeys", "filter_notempty"]

        _filters = [filters.__dict__.get(value) for value in filters_list]
        dataset = {"first": 1, "second": 2, "third": None, "@qw": 4}
        res = DatasetFilter(dataset=dataset, filters=_filters).apply()
        self.assertEqual(res, {"SECOND": 2})


if __name__ == '__main__':
    unittest.main()
