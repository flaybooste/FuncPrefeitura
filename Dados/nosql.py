from pymongo import MongoClient

def start():
    client = MongoClient("localhost", 27017)
    return client

def insertOne(dt):
    client = start()
    folhapagamento = client.folhapagamento.folhapag
    folhapagamento_id = folhapagamento.insert_one(dt)
    print("completo")
