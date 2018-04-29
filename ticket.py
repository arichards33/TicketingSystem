import datetime

global ticket_id_num
ticket_id_num = 1000000
global green_route_ticket
green_route_ticket = {}
global red_route_ticket
red_route_ticket = {}
global blue_route_ticket
blue_route_ticket = {}
global ticket_sales_count
ticket_sales_count = 0
global GREEN_SEATS
GREEN_SEATS = 356
global RED_SEATS
RED_SEATS = 445
global BLUE_SEATS
BLUE_SEATS = 178



class Ticket:


    def __init__(self, year, month, day, discount, route):
        global ticket_id_num
        if ticket_id_num == 9999999:
            ticket_id_num = 1000000
        self.ticket_id_num = None
        self.date = datetime.date(year, month, day)
        self.route = route
        self.check_seats()
        self.set_ticket_num()
        self.set_ticket_cost(discount)


    def set_ticket_num(self):
        """creates a unique ticket id"""
        global ticket_id_num
        ticket_id_num += 1
        self.ticket_id_num = ticket_id_num
        global ticket_sales_count
        ticket_sales_count += 1

    def set_ticket_cost(self, discount):
        """determine the cost of the ticket based on the day of the week it's valid for"""
        day_wk = self.date.weekday()
        if day_wk == 4 or day_wk == 5 or day_wk == 6:
            if discount:
                self.cost = 10 - (10 * .1)
            else:
                self.cost = 10
        else:
            if discount:
                self.cost = 8 - (8 * .1)
            else:
                self.cost = 8

    def check_seats(self):
        if self.route == 'green':
            self.seat_on_bus(green_route_ticket, GREEN_SEATS)
        elif self.route == 'red':
            self.seat_on_bus(red_route_ticket, RED_SEATS)
        elif self.route == 'blue':
            self.seat_on_bus(blue_route_ticket, BLUE_SEATS)


    def seat_on_bus(self, tickets_sold_route, seats_available):
        if not tickets_sold_route:
            tickets_sold_route[self.date] = 1
        else:
            for key, value in tickets_sold_route.items():
                if key == self.date:
                    current_seats_sold = int(value)
                    current_seats_sold += 1
                    if current_seats_sold < seats_available:
                        tickets_sold_route[self.date] = current_seats_sold
                    else:
                        print("This route is sold out for this ticket_date")
                else:
                    tickets_sold_route[self.date] = 1

    def get_ticket_info(self):
        """prints out info on a ticket"""
        return "ticket ID: " + str(self.ticket_id_num) + " Date: " + str(self.date) + " Cost: " + str(self.cost)
