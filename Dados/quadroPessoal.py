import xml.etree.ElementTree as ET
from nosql import insertOne

def start():
    tree = ET.parse("dados/FolhaPagamento.xml")
    return tree

def getAll():
    tree = start()
    i = 0
    doc = []
    while(i <= len(tree.getroot())):
        try:
            func = {
                "competencia":tree.getroot()[i][0].text,
                "lotacao":tree.getroot()[i][1].text,
                "cargo":tree.getroot()[i][2].text,
                "nome":tree.getroot()[i][3].text,
                "salariobase":tree.getroot()[i][4].text,
                "proventos":tree.getroot()[i][5].text,
                "vantagens":tree.getroot()[i][6].text,
                "vencimentos":tree.getroot()[i][7].text,
                "descontos":tree.getroot()[i][8].text,
                "liquido":tree.getroot()[i][9].text,
                }
            insertOne(func)
            i = i + 1
        except IndexError:
            pass
    print("Acabou aqui")

if __name__ == "__main__":
    getAll()
