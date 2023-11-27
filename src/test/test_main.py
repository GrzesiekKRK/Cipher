import pytest
from unittest.mock import patch
from src import main


class TestMain:
    def test_main_with_mock(self):
        with patch("src.main.main") as mock_main:
            main.main()

            mock_main.assert_called_once()
