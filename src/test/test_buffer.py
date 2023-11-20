import builtins
from unittest.mock import patch
from src.buffer import Buffer, Text
import pytest


class TestBuffer:
    @pytest.fixture
    def set_buffer_list_for_test(self, mocker):
        self.data = mocker.patch.object(
            Buffer,
            "data",
            [
                Text(
                    "If you are smartest person in the room, then you are in the wrong room",
                    13,
                    "Decrypted",
                )
            ],
        )

    @pytest.fixture
    def set_list_empty_list_for_test(self, mocker):
        self.data = mocker.patch.object(Buffer, "data", [])

    def test_show_buffer_call_with_mock_print(self, set_buffer_list_for_test):
        with patch("builtins.print") as mock_print:
            Buffer.show_buffer()

            mock_print.assert_called_with(
                "1. Text(contents='If you are smartest person in the room,"
                " then you are in the wrong room', rot_type=13, status='Decrypted')\n"
            )

    def test_show_buffer_with_set_buffer_list_for_test(self, set_buffer_list_for_test):
        assert len(self.data) == 1

    def test_add_func_by_append_str_to_set_buffer_list_for_test_logic(
        self, set_buffer_list_for_test
    ):
        Buffer.add(
            Text("I don't now you then you are in the wrong room", 13, "Decrypted")
        )
        assert len(self.data) == 2

    def test_add_call(self, set_buffer_list_for_test):
        with patch.object(Buffer, "add") as mock_add:
            Buffer.add(
                Text("I don't now you then you are in the wrong room", 13, "Decrypted")
            )

            mock_add.assert_called_once()

    def test_convert_with_set_buffer_list_for_test_logic(
        self, set_buffer_list_for_test
    ):
        assert Buffer.convert() == [
            {
                "contents": "If you are smartest person in the room, then you are in the wrong room",
                "rot_type": 13,
                "status": "Decrypted",
            }
        ]

    def test_load_from_dict_call_with_logic(self, set_list_empty_list_for_test):
        test_data = {
            "data": [
                {
                    "contents": "If you are smartest person in the room, then you are in the wrong room",
                    "rot_type": 47,
                    "status": "Decrypted",
                }
            ]
        }
        with patch.object(Buffer, "load_from_dict") as mock_load_from_dict:
            Buffer.load_from_dict(test_data)

            mock_load_from_dict.assert_called_once_with(test_data)
