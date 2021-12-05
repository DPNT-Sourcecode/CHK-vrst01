from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution

#TODO:This could potentially be improved with more focus on helper functions, but this is sufficient
class TestCHK():
    def test_chk(self):
        assert checkout_solution.checkout("AAABCBAD") == 260
    def test_non_string(self):
        assert checkout_solution.checkout(1) == -1
    def test_unpermitted_value(self):
        assert checkout_solution.checkout("AAADq") == -1
    def test_E_offer(self):
        assert checkout_solution.checkout("ABBEE") == 160
    def test_7_As(self):
        assert checkout_solution.checkout("AAAAA") == 200
    def test_basic_F_offer(self):
        assert checkout_solution.checkout("AFFF") == 70
    def test_5_Fs_offer(self):
        assert checkout_solution.checkout("AFFFFF") == 90
    def test_6_Fs_offer(self):
        assert checkout_solution.checkout("AFFFFFF") == 90
    def test_6_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUU") == 250
    def test_7_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUUU") == 290
    def test_8_Us_offer(self):
        assert checkout_solution.checkout("AUUUUUUUU") == 290
    def test_R_Q_offer(self):
        assert checkout_solution.checkout("ARRRQQQ") == 260
    def test_R_offer_Q_offer(self):
        assert checkout_solution.checkout("ARRRQQQQ") == 280
    def test_mix_and_match_offer(self):
        assert checkout_solution.checkout("ZYXTTTTS") == 127
    def test_R_offer_Q_offer_and_mix_and_match_offer(self):
        assert checkout_solution.checkout("ARRRZQQSQQYXTTTT") == 407
    def test_R_offer_Q_offer_mix_and_match_offer_and_7Us_offer(self):
        assert checkout_solution.checkout("AUUUUUUUARRRZQQSQQYXTTTT") == 697
    def test_simplest_mix_and_match_offer(self):
        assert checkout_solution.checkout("STXSTX") == 90





