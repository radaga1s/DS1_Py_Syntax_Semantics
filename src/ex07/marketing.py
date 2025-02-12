import sys

def call_exception():
    raise Exception('Wrong task`s name')

def get_subtracted(a_set: set, b_set: set) -> list:
    return list(a_set - b_set)

def get_subtracted_intersected(a_set: set, b_set: set) -> list:
    return list(a_set - (a_set & b_set))

def main():
    if len(sys.argv) == 1:
        call_exception()
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)
    d = dict(call_center=(get_subtracted, clients_set, recipients_set),
             potential_clients=(get_subtracted, participants_set, clients_set),
             loyalty_program=(get_subtracted_intersected, clients_set, participants_set))
    for command in sys.argv[1:]:
       if command not in d:
           call_exception()
       func, *args = d[command]
       print(func(*args))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
