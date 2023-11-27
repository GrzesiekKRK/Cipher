from unittest.mock import patch
import tempfile
import json
import pytest
import os
from src.file_handler import FileHandler


class TestFileHandler:
    @pytest.fixture
    def set_file_handler_for_test(self):
        content = {
            "data": [
                {
                    "contents": "If you are smartest person in the room, then you are in the wrong room",
                    "rot_type": 47,
                    "status": "Decrypted",
                }
            ]
        }
        return FileHandler("name", content)

    @pytest.fixture
    def set_test_file(self, set_file_handler_for_test):
        test_file = tempfile.NamedTemporaryFile(
            prefix="file_for_test", suffix=".json", dir=".", mode="w", delete=False
        )
        with test_file as file:
            json.dump(set_file_handler_for_test.contents, file, indent=4)
        return file.name

    def test_read_file_call(self, set_file_handler_for_test):
        with patch.object(FileHandler, "read_file") as mock_read_file:
            set_file_handler_for_test.read_file("name.json")

            mock_read_file.assert_called_once()

    def test_read_file_logic(self, set_file_handler_for_test, set_test_file):
        assert set_file_handler_for_test.read_file(set_test_file) == {
            "data": [
                {
                    "contents": "If you are smartest person in the room,"
                    " then you are in the wrong room",
                    "rot_type": 47,
                    "status": "Decrypted",
                }
            ]
        }

    def test_append_call(self, set_file_handler_for_test):
        with patch.object(
            FileHandler,
            "append",
        ) as mock_append:
            set_file_handler_for_test.append()

            mock_append.assert_called_once()

    def test_write_call(self, set_file_handler_for_test):
        with patch.object(
            FileHandler,
            "write",
        ) as mock_write:
            set_file_handler_for_test.write()

            mock_write.assert_called_once()

    def test_write_call_with_one(self, set_file_handler_for_test):
        with patch.object(
            FileHandler,
            "write",
        ) as mock_write:
            set_file_handler_for_test.write(1)

            mock_write.assert_called_once_with(1)
