from decimal import Decimal, ROUND_HALF_UP
def loan_repayment(principal: float, annual_rate: float, months: int) -> dict[str, float]:
    """
    Loan formula:
        M = P x [ r(1+r)^n / ((1+r)^n - 1) ]
    Loan fomula in python code:
        M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
        

    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate as a percentage.
        months (int): The number of months for repayment.

    Returns:
        dict[str, float]: JSON format: Monthly repayment, total repayment amount, total interest paid
    """
    
    if principal <= 0:
        raise ValueError("Loan amount must be greater than 0.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if months <= 0:
        raise ValueError("Months must be greater than 0.")
    
    P = Decimal(str(principal))
    annual_rate_decimal = Decimal(str(annual_rate)) / Decimal("100")
    monthly_rate = annual_rate_decimal / Decimal("12")
    
    if monthly_rate == 0:
        monthly_repayment = P / months
    else:
        # Loan formula
        monthly_repayment = P * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    
    total_repayment = monthly_repayment * months
    total_interest= total_repayment - P
    
    
    penny = Decimal("0.01")
    return {
        "monthly_repayment": float(monthly_repayment.quantize(penny, ROUND_HALF_UP)),
        "total_repayment_amount": float(total_repayment.quantize(penny, ROUND_HALF_UP)),
        "total_interest_paid": float(total_interest.quantize(penny, ROUND_HALF_UP)),
    }
    
    
    