import xmlrpc.client
import csv

host = '127.0.0.1'
port = 8016
db = 'mfh'
user = 'observer'
password = 'observer'
# noinspection PyStringFormat
url = 'http://%s:%d/xmlrpc/2/' % (host, port)

common_proxy = xmlrpc.client.ServerProxy(url + 'common')
object_proxy = xmlrpc.client.ServerProxy(url + 'object')

uid = common_proxy.login(db, user, password)
if uid:
    print("I can connect to the db!")


def _create(state):
    print("=1=")
    print(state)
    if state is True:
        archive = csv.DictReader(open('data.csv'))
        cont = 0
        for field in archive:
            _name = field['name'].strip()
            _email = field['email'].strip()
            _phone = field['phone'].strip()

            vals = {'name': _name, 'email': _email, 'phone': _phone, 'active': True}

            print(vals)

            # Validation. Registry doesn't exist
            _id = object_proxy.execute_kw(db, uid, password, 'res.partner', 'search', [[['name', '=', _name]]])
            if _id:
                print('The registry does exist!')
            else:
                new_partner = object_proxy.execute(db, uid, password, 'res.partner', 'create', vals)
                if new_partner:
                    cont += 1
                    print("New partner created successfully!")
                else:
                    print("New partner was not created!")
        cont = str(cont)
        print(cont + ' new partners where created')

def main():
    print("The process started")
    _create(True)
    print("The process finished")
main()
