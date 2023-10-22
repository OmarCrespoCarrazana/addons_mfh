#########################################################
#                                                       #
# Name: Observer                                        #
# Python Version: 3.11                                  #
# Author: Ing. Omar Crespo Carrazana                    #
# Purpose: Consult via Odoo's External API the model    #
# account.move in order to obtain the date of the last  #
# operation.                                            #
#                                                       #
#########################################################
import json
import random
import urllib.request
import datetime

# Parameters you can change
host = '127.0.0.1'
port = 8016
url = "http://%s:%d/jsonrpc" % (host, port)
database = 'mfh'
user = "observer"
password = "observer"
today = datetime.date.today()
file = open("mas de un mes.txt", 'a')


# Methods
def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type": "application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})


file.write(str(today) + " \n")

# Operations
print("La fecha actual es: " + str(today))

uid = call(url, "common", "login", database, user, password)

print(database)

last_operation_date = call(url, "object", "execute", database, uid, password, 'account.move', 'search_read', [],
                           ["date"])
print("Ultima operación contable: ")
if not last_operation_date:
    print("Aún no tiene operaciones. Está en implementación.")
else:
    print(last_operation_date[0])
    only_date = last_operation_date[0]['date']
    divided_date = only_date.split("-")
    last_op_date = datetime.datetime(int(divided_date[0]), int(divided_date[1]), int(divided_date[2]))
    diff_month = (today.year - last_op_date.year) * 12 + today.month - last_op_date.month
    if today.day < last_op_date.day:
        diff_month = diff_month - 1
    if diff_month > 1:
        line = "Van " + str(diff_month) + " meses desde la última operación contable en la base de datos " + database
        print(line)
        file.write(line)
        file.write("\n \n")
file.close()

# EoF
