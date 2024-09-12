# THIS FILE IS "WIP", IT'S NOT WORKING CORRECTLY OR AT ALL
def main():
    price_count = int(input())
    # price_list represents prices in chronological order
    # ticket_list represents amount of tickets that can be spent the very same day Pete makes an order
    price_list = []
    ticket_list = []
    ticket_amount = 0
    for id_pair in range(price_count):
        price = 0
        try:
            price = int(input())
            price_list.append(price)
            ticket_list.append(ticket_amount)
            if price > 100:
                ticket_amount += 1
        except ValueError:
            print("Not a Number!")
            return 0
    print(f"Price List {price_list}\nTicket List {ticket_list}\n")
    pass


if __name__ == '__main__':
    main()
