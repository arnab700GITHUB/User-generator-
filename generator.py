from random import randrange
import csv

users = []

first_names = open("dataset/f_name.txt", "r").readlines()
last_names = open("dataset/l_name.txt", "r").readlines()
addresses = open("dataset/address.txt", "r").readlines()

def generate_user(user_no):
    for i in range(1, user_no+1):
        user = {}
        fn = first_names[randrange(0, len(first_names)-1)]
        ln = last_names[randrange(0, len(last_names)-1)]
        addr = addresses[randrange(0, len(addresses)-1)]

        fn = fn.replace("\n", " ")
        ln = ln.replace("\n", "")
        addr = addr.replace("\n", "")

        user["id"] = i    
        user["name"] = "{} {}".format(fn, ln)
        user["address"] = addr

        users.append(user)
        i += 1

def make(user_no):
    with open("file.csv", "w") as file:
        file.close()
    generate_user(user_no)
    with open("users.csv", "a", newline='') as file:
        fieldnames = ['id', 'name', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for i in users:
            writer.writerow({'id': i["id"], 'name': i['name'], 'address': i['address']})

        return file