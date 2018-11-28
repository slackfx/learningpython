import unittest
from math import sqrt
from random import randint, sample

from mock import patch
from nose.tools import (
        assert_equal,
        assert_list_equal,
        assert_not_in
)

from karma import nt, utils
