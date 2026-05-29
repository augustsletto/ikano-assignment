from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.schemas import LoanRequest, LoanResponses, FibonacciRequest, FibonacciResponse, FactorialRequest, FactorialResponse
from app.calculations.loan_repayment import loan_repayment
from app.calculations.fibonacci import fibonacci
from app.calculations.factorial import factorial

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/fibonacci", response_model=FibonacciResponse)
def calculate_fibonacci(request: FibonacciRequest):
    try:
        
        return FibonacciResponse(result=fibonacci(request.fibonacci_integer))
    except (ValueError, OverflowError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/factorial", response_model=FactorialResponse)
def calculate_factorial(request: FactorialRequest):
    try:
        return FactorialResponse(result=factorial(request.factorial_integer))
    except (ValueError, OverflowError) as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/loan", response_model=LoanResponses)
def calculate_loan(request: LoanRequest):
    try:
        result = loan_repayment(
            principal=request.principal,
            annual_rate=request.annual_rate,
            months=request.months
        )
        
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))