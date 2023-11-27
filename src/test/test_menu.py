import pytest
from unittest.mock import patch
from src.menu import (
    show_menu,
    user_action,
    code_decode,
    write_or_append,
    get_filename,
    hand_writen,
)


class TestMenu:
    def test_show_menu_with_mock_print(self):
        with patch("builtins.print") as mock_print:
            show_menu()
            mock_print.assert_called_with(
                f"1.Show current in buffer\n"
                f"2.Encryption / Decryption\n"
                f"3.Load from file \n"
                f"4.Save data to file\n"
                f"5.Write text and choose rot\n"
                f"0.Exit"
            )

    def test_user_action_with_mock_input(self):
        with patch("builtins.input") as mock_input:
            user_action()

            mock_input.assert_called_with("\nWhich one?: ")

    def test_code_decode_with_mock_input(self):
        with patch("builtins.input") as mock_input:
            code_decode()

            mock_input.assert_called_with(
                "Choose which one to encrypt/decrypt: ",
            )

    def test_write_or_append_with_mock_input(self):
        with patch("builtins.input") as mock_input:
            write_or_append()

            mock_input.assert_called_with(
                "Write  or append to file?: ",
            )

    def test_get_filename_with_mock_input(self):
        with patch("builtins.input") as mock_input:
            get_filename()

            mock_input.assert_called_with(
                "Filename (without extension): ",
            )

    def test_hand_writen_with_mock_input(self):
        with patch("builtins.input") as mock_input:
            hand_writen()

            mock_input.assert_called_with(
                "Status encrypt/decrypt: ",
            )
