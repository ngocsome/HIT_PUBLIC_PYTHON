# quy_doi.py

import ty_gia

def doi_sang_usd(vnd):
    return vnd / ty_gia.USD_RATE

def doi_sang_eur(vnd):
    return vnd / ty_gia.EUR_RATE

def doi_sang_jpy(vnd):
    return vnd / ty_gia.JPY_RATE
