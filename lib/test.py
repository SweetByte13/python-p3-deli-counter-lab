katz_deli = ["Logan", "jim", "kim", "wim"]

def line(katz_deli):
    if katz_deli != []:
        names = ''
        for position, person in enumerate(katz_deli):
            ##index = person.index()
            ##print(position+1, person)
            names += f' {position+1}. {person}'
        print("The line is currently:" + names)
    else:
        print("The line is currently empty.")

def get_last_index(list) -> int:
    return len(list) - 1

def take_a_number(katz_deli, new_customer):
    if new_customer != "":
        katz_deli.append(new_customer)
        newest_customer = katz_deli[-1]
        spot_in_line = get_last_index(katz_deli)
        print(f"Welcome, {new_customer}. You are number {spot_in_line+1} in line.")

def now_serving(queue):
    if katz_deli != []:
        next_customer = katz_deli[0]
        print("Currently serving " +next_customer + ".")
        katz_deli.pop(0)
    else:
        print("There is nobody waiting to be served!")

now_serving(katz_deli)
print(katz_deli)