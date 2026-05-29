import pytest
from app.calculations.loan_repayment import loan_repayment

def test_basic_loan():
    result = loan_repayment(100_000, 5, 48) # 100,000, 5%, 48 months
    assert result["monthly_repayment"] == 2302.93
    
def test_zero_interest():
    result = loan_repayment(12_000, 0, 12) # 12,000, 0%, 12 months
    assert result["monthly_repayment"] == 1000.00
    assert result["total_interest_paid"] == 0.00
    
def test_negative_principal():
    with pytest.raises(ValueError):
        loan_repayment(-1000, 5, 12)
        

def test_negative_interest():
    with pytest.raises(ValueError):     
        loan_repayment(50_000, -10, 24)
    
def test_zero_months():
    with pytest.raises(ValueError):
        loan_repayment(100_000, 5, 0)
        
def test_total_greater_than_principal():
    result = loan_repayment(100_000, 5, 48)
    assert result["total_repayment_amount"] > 100_000
    assert result["total_interest_paid"] > 0