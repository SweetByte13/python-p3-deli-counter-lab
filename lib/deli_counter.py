katz_deli = []

def line(katz_deli):
    if katz_deli!=[]:
        names = ''
        for position, person in enumerate(katz_deli):
            names += f' {position+1}. {person}'
        print("The line is currently:" + names)
    else:
        return print("The line is currently empty.")
    
line(katz_deli)

def get_last_index (list) -> int:
    return len(list)-1

def take_a_number(katz_deli, new_customer):
    if new_customer != "":
        katz_deli.append(new_customer)
        spot_in_line=get_last_index(katz_deli)
        print(f"Welcome, {new_customer}. You are number {spot_in_line + 1} in line.")

take_a_number(katz_deli,"lim")
print(katz_deli)

def now_serving(queue):
    if queue != []:
        next_customer = queue[0]
        print(f"Currently serving {next_customer}.")
        queue.pop(0)
    else:
       print("There is nobody waiting to be served!")

now_serving(katz_deli)
print(katz_deli)