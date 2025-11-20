from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="crud-ms-account-load-fdr")

FDR = {
    "ACC1001": {"accountId": "ACC1001", "status": "ACTIVE", "balance": 15000.5, "accountType": "SAVINGS"},
    "ACC2002": {"accountId": "ACC2002", "status": "ACTIVE", "balance": 8200.0, "accountType": "CHECKING"}
}

class FDRResp(BaseModel):
    accountId: str
    status: str
    balance: float
    accountType: str

@app.get("/fdr/account/{accountId}", response_model=FDRResp)
def get_account(accountId: str):
    return FDR.get(accountId, {
        "accountId": accountId,
        "status": "NOT_FOUND",
        "balance": 0.0,
        "accountType": "UNKNOWN"
    })

@app.get("/health")
def health():
    return {"status": "crud-fdr-up"}
