import unittest

import steampi.api


class TestSteamPiMethods(unittest.TestCase):

    def test_main(self):
        self.assertTrue(steampi.main())


if __name__ == '__main__':
    unittest.main()
