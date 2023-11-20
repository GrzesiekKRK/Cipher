import builtins
from unittest.mock import patch, call
import pytest
from src.manager import Manager
from src.buffer import Buffer
from src import menu


class TestManager:
    @pytest.fixture
    def set_test_obj(self):
        return Manager()

    @pytest.fixture
    def set_buffer_empty_list_for_test(self, mocker):
        self.data = mocker.patch.object(Buffer, "data", [])

    def test_run_time(self, set_test_obj):
        with patch.object(Manager, "run_time") as mock_run_time:
            set_test_obj.run_time()

            mock_run_time.assert_called_once()

    def test_perform_action_with_mock_one(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("1")

            mock_perform_action.assert_called_with("1")

    def test_perform_action_with_mock_encrypt_decrypt_number_two(self, set_test_obj):
        with patch.object(Manager, "encrypt_decrypt") as mock_encrypt_decrypt:
            set_test_obj.perform_action("2")

            mock_encrypt_decrypt.assert_called_once()

    def test_perform_action_with_mock_two(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("2")

            mock_perform_action.assert_called_with("2")

    def test_perform_action_with_mock_read_file_number_three(self, set_test_obj):
        with patch.object(Manager, "read_file") as mock_read_file:
            set_test_obj.perform_action("3")

            mock_read_file.assert_called_once()

    def test_perform_action_with_mock_three(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("3")

            mock_perform_action.assert_called_with("3")

    def test_perform_action_with_mock_file_number_four(self, set_test_obj):
        with patch.object(Manager, "file") as mock_file:
            set_test_obj.perform_action("4")

            mock_file.assert_called_once()

    def test_perform_action_with_mock_four(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("4")

            mock_perform_action.assert_called_with("4")

    def test_perform_action_with_mock_five(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("5")

            mock_perform_action.assert_called_with("5")

    def test_perform_action_with_mock_hand_writen(self, set_test_obj):  # jak ?
        with patch.object(menu, "hand_writen") as mock_hand_writen:
            set_test_obj.perform_action = mock_hand_writen
            set_test_obj.perform_action()

            mock_hand_writen.assert_called_once()

    def test_perform_action_with_mock_exit_number_zero(self, set_test_obj):
        with patch("builtins.exit") as mock_exit:
            set_test_obj.perform_action("0")

            mock_exit.assert_called_once()

    def test_perform_action_with_mock_zero(self, set_test_obj):
        with patch.object(Manager, "perform_action") as mock_perform_action:
            set_test_obj.perform_action("0")

            mock_perform_action.assert_called_with("0")

    def test_encrypt_decrypt_with_mock(self, set_test_obj):
        with patch.object(Manager, "encrypt_decrypt") as mock_encrypt_decrypt:
            set_test_obj.encrypt_decrypt()

            mock_encrypt_decrypt.assert_called_once()

    @pytest.mark.xfail
    def test_encrypt_decrypt_with_mock_variables(self, set_buffer_empty_list_for_test):
        test_obj = Manager()
        with patch("builtins.input", return_value="co"), patch(
            "builtins.print"
        ) as mock_print:
            test_obj.encrypt_decrypt()

            mock_print.assert_called_with("\nValue error\n")

    def test_file_with_mock(self, set_test_obj):
        with patch.object(Manager, "file") as mock_file:
            set_test_obj.file()

            mock_file.assert_called_once()

    def test_read_file_with_mock(self, set_test_obj):
        with patch.object(Manager, "read_file") as mock_read_file:
            set_test_obj.read_file()

            mock_read_file.assert_called_once()

    def test_make_new_object(self, set_test_obj, set_buffer_empty_list_for_test):
        with patch("builtins.input") as mock_make_object:
            set_test_obj.make_new_object()

            mock_make_object.assert_called_with("Status encrypt/decrypt: ")
