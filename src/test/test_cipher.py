from unittest.mock import patch
import pytest
import string
from src.cipher import Rot47, Rot13, RotCustomized
from src.buffer import Text


class TestCipher:
    @pytest.fixture
    def set_rot13_for_test(self):
        return Rot13()

    @pytest.fixture
    def set_text_obj_for_test(self):
        mock = Text(
            "If you are smartest person in the room, then you are in the wrong room",
            13,
            "Decrypted",
        )
        return mock

    def test_transform_mock_for_call(self, set_rot13_for_test):
        with patch.object(Rot13, "transform") as mock_transform:
            set_rot13_for_test.transform()

            mock_transform.assert_called_once()

    def test_transform_logic(self, set_rot13_for_test, set_text_obj_for_test):
        alphabet = string.ascii_lowercase
        char_table = alphabet[13:] + alphabet[:13]
        set_rot13_for_test.transform(char_table, alphabet, set_text_obj_for_test)
        assert (
            set_text_obj_for_test.contents
            == "vs lbh ner fznegrfg crefba va gur ebbz, gura lbh ner va gur jebat ebbz"
        )

    def test_encrypt_call(self, set_rot13_for_test, set_text_obj_for_test):
        with patch("builtins.print") as mock_print:
            set_rot13_for_test.encrypt(set_text_obj_for_test)

            mock_print.assert_called_once()

    def test_encrypt_logic(self, set_rot13_for_test, set_text_obj_for_test):
        set_rot13_for_test.encrypt(set_text_obj_for_test)
        assert set_text_obj_for_test.status == "Encrypted"

    def test_decrypt_call(self, set_rot13_for_test, set_text_obj_for_test):
        with patch("builtins.print") as mock_print:
            set_rot13_for_test.decrypt(set_text_obj_for_test)

            mock_print.assert_called_once()

    def test_decrypt_logic(self, set_rot13_for_test, set_text_obj_for_test):
        set_rot13_for_test.decrypt(set_text_obj_for_test)
        assert set_text_obj_for_test.status == "Decrypted"

    @pytest.fixture
    def set_rot47_for_test(self):
        return Rot47()

    @pytest.fixture
    def set_text_obj_for_test_47(self):
        mock = Text(
            "If you are smartest person in the room, then you are in the wrong room",
            47,
            "Decrypted",
        )
        return mock

    def test_transform_47_mock_for_call(self, set_rot47_for_test):
        with patch.object(Rot47, "transform") as mock_transform:
            set_rot47_for_test.transform()

            mock_transform.assert_called_once()

    def test_transform_47_logic(self, set_rot47_for_test, set_text_obj_for_test_47):
        alphabet = string.ascii_lowercase
        char_table = alphabet[21:] + alphabet[:21]
        set_rot47_for_test.transform(char_table, alphabet, set_text_obj_for_test_47)
        assert (
            set_text_obj_for_test_47.contents
            == "nk dtz fwj xrfwyjxy ujwxts ns ymj wttr, ymjs dtz fwj ns ymj bwtsl wttr"
        )

    def test_encrypt_47_call(self, set_rot47_for_test, set_text_obj_for_test_47):
        with patch("builtins.print") as mock_print:
            set_rot47_for_test.encrypt(set_text_obj_for_test_47)

            mock_print.assert_called_once()

    def test_encrypt_47_logic(self, set_rot47_for_test, set_text_obj_for_test_47):
        set_rot47_for_test.encrypt(set_text_obj_for_test_47)
        assert set_text_obj_for_test_47.status == "Encrypted"

    def test_decrypt_47_call(self, set_rot47_for_test, set_text_obj_for_test_47):
        with patch("builtins.print") as mock_print:
            set_rot47_for_test.decrypt(set_text_obj_for_test_47)

            mock_print.assert_called_once()

    def test_decrypt_47_logic(self, set_rot47_for_test, set_text_obj_for_test_47):
        set_rot47_for_test.decrypt(set_text_obj_for_test_47)
        assert set_text_obj_for_test_47.status == "Decrypted"

    @pytest.fixture
    def set_rot_custom_for_test(self):
        return RotCustomized()

    @pytest.fixture
    def set_text_obj_for_test_custom(self):
        mock = Text(
            "If you are smartest person in the room, then you are in the wrong room",
            3,
            "Decrypted",
        )
        return mock

    def test_transform_custom_for_logic_2(
        self, set_rot_custom_for_test, set_text_obj_for_test_custom
    ):
        with patch.object(RotCustomized, "_get_mode", return_value=3) as mode:
            alphabet = string.ascii_lowercase
            char_table = alphabet[mode:] + alphabet[:mode]
            set_rot_custom_for_test.transform(
                alphabet, char_table, set_text_obj_for_test_custom
            )
            assert (
                set_text_obj_for_test_custom.contents
                == "jg zpv bsf tnbsuftu qfstpo jo uif sppn, uifo zpv bsf jo uif xspoh sppn"
            )

    def test_encryption_custom_for_call_with_mock_print(
        self, set_rot_custom_for_test, set_text_obj_for_test_custom
    ):
        with patch("builtins.print") as mock_print:
            set_rot_custom_for_test.encryption(set_text_obj_for_test_custom)

            mock_print.assert_called_once()

    def test_encryption_custom_logic_with_mock_mode(
        self, set_rot_custom_for_test, set_text_obj_for_test_custom
    ):
        with patch.object(RotCustomized, "_get_mode", return_value=3):
            set_rot_custom_for_test.encryption(set_text_obj_for_test_custom)
            assert (
                set_text_obj_for_test_custom.contents
                == "li brx duh vpduwhvw shuvrq lq wkh urrp, wkhq brx duh lq wkh zurqj urrp"
            )

    def test_decrypted_custom_call(
        self, set_rot_custom_for_test, set_text_obj_for_test_custom
    ):
        with patch("builtins.print") as mock_print:
            set_rot_custom_for_test.decrypted(set_text_obj_for_test_custom)

            mock_print.assert_called_once()

    def test_decrypted_custom_logic_with_mock_mode(
        self, set_rot_custom_for_test, set_text_obj_for_test_custom
    ):
        with patch.object(RotCustomized, "_get_mode", return_value=3):
            set_rot_custom_for_test.decrypted(set_text_obj_for_test_custom)
            assert (
                set_text_obj_for_test_custom.contents
                == "fc vlr xob pjxoqbpq mboplk fk qeb ollj, qebk vlr xob fk qeb tolkd ollj"
            )
