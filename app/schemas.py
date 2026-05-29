from pydantic import BaseModel, Field



class FibonacciRequest(BaseModel):
    fibonacci_integer: int = Field(ge=0, description="Position in the Fibonacci sequence")


class FibonacciResponse(BaseModel):
    result: int
    
class FactorialRequest(BaseModel):
    factorial_integer: int = Field(ge=0, description="Integer to factorial")


class FactorialResponse(BaseModel):
    result: int
    


class LoanRequest(BaseModel):
    principal: float = Field(gt=0, description="Loan amount")
    annual_rate: float = Field(ge=0, description="Annual interest rate as a percentage")
    months: int = Field(gt=0, description="Loan term in months")
    

class LoanResponses(BaseModel):
    monthly_repayment: float
    total_repayment_amount: float
    total_interest_paid: float
    
    