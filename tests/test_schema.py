"""Minimal raw-schema tests."""

import unittest

from nifty_forecast.data import FUTURES_COLUMNS, OPTIONS_COLUMNS, SPOT_COLUMNS


class SchemaTest(unittest.TestCase):
    def test_spot_has_no_volume(self) -> None:
        self.assertNotIn("volume", SPOT_COLUMNS)

    def test_derivatives_have_volume_and_oi(self) -> None:
        for columns in (FUTURES_COLUMNS, OPTIONS_COLUMNS):
            self.assertIn("volume", columns)
            self.assertIn("oi", columns)

    def test_options_keep_contract_identity(self) -> None:
        for column in ("expiry", "strike", "option_type"):
            self.assertIn(column, OPTIONS_COLUMNS)


if __name__ == "__main__":
    unittest.main()
