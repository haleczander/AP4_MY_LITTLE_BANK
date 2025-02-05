from DTO import *
from repo import account_repo

def find_by_id(id):
    account_repo.find_by_id(id)