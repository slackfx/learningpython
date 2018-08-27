from unittest import TestCase
from unittest.mock import patch, call
from nose.tools import assert_equal, assert_list_equal
from filter_funcs import filter_ints, is_positive

class FilterIntsTestCase(TestCase):

#    @patch('filter_funcs.is_positive')
#    def test_filter_ints(self, is_positive_mock):
        # preparation
#        v = [3, -4, 0, 5, 8]

        # execution
#        filter_ints(v)

        # verification
#        assert_equal([call(3), call(-4), call(0), call(5), call(8)], is_positive_mock.call_args_list)


    def test_filter_ints_return_value(self):
        v = [3, -4, 0, -4, 5, 0, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]

        assert_list_equal([3, 5, 8], filter_ints(v))
        assert_list_equal([7, 9, 1], filter_ints(v2))

    def test_is_positive(self):
        assert_equal(False, is_positive(-1))
        assert_equal(False, is_positive(0))
        assert_equal(True, is_positive(1))
