"""
Lab 3: Program 1 (Questions 1 - 5)

"""

def main():
    request = "Enter number of tickets required: "
    tickets = get_number_from_user(request)
    full_price = get_ticket_price(tickets, 15)
    discount = get_discount(tickets, full_price)
    display_ticket_price(tickets, full_price, discount)
    
def display_ticket_price(tickets, price, discount):    
    print("*"*20)
    print("Tickets:", tickets)
    print("Price: $",price - discount," (discount included: $",discount,").",sep="")
    print("GST included: $",get_gst_amount(price - discount),sep="")
    print("*"*20)
    return()

def get_gst_amount(price):
    gst = round(price * 0.15, 2)
    return gst

def get_discount(number_of_tickets, total_price):
    discount_number = round(max(number_of_tickets * 4,total_price*0.1))
    return discount_number

def get_ticket_price(number_of_tickets, ticket_price):
    total_price = round(number_of_tickets*ticket_price)
    return total_price

def get_number_from_user(prompt):
    num = int(input(prompt))
    return num
    

main()








