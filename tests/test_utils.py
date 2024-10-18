import unittest
from ddt import data, ddt, unpack
from common import utils


@ddt
class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    @data(
        ([{'id': 'id1', 'name': 'file_name1.txt'}],
         'file_name1.txt',
         'id1')
    )
    @unpack
    def test_utils_get_file_id_for_name(self, items, file_name, expected):
        result = utils.get_file_id_for_name(items, file_name)
        assert result == expected
