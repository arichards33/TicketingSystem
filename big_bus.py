import cmd
import ticket
import re
import datetime
import pickle

global all_tickets
all_tickets = []

class Big_Bus(cmd.Cmd):
    intro = "\nWelcome to Big Bus Ticket Sales!\nType `help` or `?` to list commands.\n"
    prompt = '> '
    event = None

    def do_program_startup(self, args):
        """Must be run to load up the program to keep track of where the program is all with all the varables\
        since the program was last ended"""
        self.route = ""
        try:
            import_file = open("stored_values.pkl", "r")
            global ticket_id_num
            ticket.ticket_id_num = pickle.load(import_file)
            global ticket_sales_count
            ticket.ticket_sales_count = pickle.load(import_file)
            global green_route_ticket
            ticket.green_route_ticket = pickle.load(import_file)
            global red_route_ticket
            ticket.red_route_ticket = pickle.load(import_file)
            global blue_route_ticket
            ticket.blue_route_ticket = pickle.load(import_file)
            global all_tickets
            all_tickets = pickle.load(import_file)
        except FileNotFoundError:
            print("Startup is not needed on the very first use of the application")
        print ticket.blue_route_ticket

    def do_quit(self, arg):
      """Quits program but saves all the necessary information for the next time the program is run"""
      global ticket_id_num
      global all_tickets
      global ticket_sales_count
      global green_route_ticket
      global red_route_ticket
      global blue_route_ticket
      filein = open("stored_values.pkl", "w")
      pickle.dump(ticket.ticket_id_num, filein)
      pickle.dump(ticket.ticket_sales_count, filein)
      pickle.dump(ticket.green_route_ticket, filein)
      pickle.dump(ticket.red_route_ticket, filein)
      pickle.dump(ticket.blue_route_ticket, filein)
      pickle.dump(all_tickets, filein)
      return True

    def do_buy(self, args):
        """Buy a Ticket"""
        self.all_tickets_sold = []
        try:
            if self.within_Date_Margin:
                for i in range(0, self.number_of_tickets):
                    newTicket = ticket.Ticket(self.year, self.month, self.day, self.discount, self.route)
                    self.all_tickets_sold.append(newTicket)
                    global all_tickets
                    all_tickets.append(newTicket)
                for i in range(0, len(self.all_tickets_sold)):
                    if self.all_tickets_sold[i].ticket_id_num != None:
                        print self.all_tickets_sold[i].get_ticket_info()
        except AttributeError as err:
            print("Need more infomation to buy a ticket")
            print err

    def do_refund(self, args):
        """Refund a Ticket"""
        if re.match("^\d\d\d\d\-\d\d\-\d\d", args):
            self.month = int(args[5:7])
            self.day = int(args[8:10])
            self.year = int(args[:4])
            remove_date = datetime.date(self.year, self.month, self.day)
            remove_id =  int(args[11:18])
            remove_route = args[19:]
            global all_tickets
            global ticket_sales_count
            for t in all_tickets:
                if t.date == remove_date and t.ticket_id_num == remove_id and t.route == remove_route:
                    all_tickets.remove(t)
                    ticket.ticket_sales_count -= 1
            if remove_route == "green":
                global green_route_ticket
                self.refund_from(ticket.green_route_ticket, remove_date)
            if remove_route == "red":
                global red_route_ticket
                self.refund_from(ticket.red_route_ticket, remove_date)
            if remove_route == "blue":
                global blue_route_ticket
                self.refund_from(ticket.blue_route_ticket, remove_date)
            print all_tickets
        else:
            print "Unable to refund that ticket"

    def refund_from(self, route_array, remove_date):
        for key, value in route_array.items():
            if key == remove_date:
                current_seats_sold = value - 1
                route_array[key] = current_seats_sold


    def do_date(self, args):
        """select the date the ticket is to be valid for"""
        self.within_Date_Margin = False
        margin = datetime.timedelta(days = 10)
        endDate = datetime.date.today() + margin
        if re.match("\d\d\d\d\-\d\d\-\d\d", args):
            self.month = int(args[5:7])
            self.day = int(args[8:10])
            self.year = int(args[:4])
            date = datetime.date(self.year, self.month, self.day)
            if date <= endDate:
                self.within_Date_Margin = True
        else:
            print("Please enter date in yyyy-mm-dd format")


    def do_create_tickets(self, args):
        """select the number of tickets to be made in the purchase -- max 4"""
        self.number_of_tickets = 0
        self.discount = False
        try:
            if int(args) > 4:
                print("Can only purchase 4 tickets at a time")
            elif int(args) == 4:
                self.discount = True
                self.number_of_tickets = int(args)
            else:
                self.number_of_tickets = int(args)
        except ValueError:
            print("Please enter the number of tickets to purchase")

    def do_sales_by_date(self, args):
        """checks all the ticket ids sold for a specific date"""
        self.count = 0
        if re.match("\d\d\d\d\-\d\d\-\d\d", args):
            self.month = int(args[5:7])
            self.day = int(args[8:10])
            self.year = int(args[:4])
            date = datetime.date(self.year, self.month, self.day)
            for i in all_tickets:
                if i.date == date:
                    self.count += 1
        else:
            print "Can't find sales for that date"
        print self.count

    def do_route(self, args):
        """select the route for the ticket"""
        route_selected = args.lower()
        try:
            if route_selected == "green":
                self.route = "green"
            elif route_selected == "red":
                self.route = "red"
            elif route_selected == "blue":
                self.route = "blue"
        except AttributeError:
            print("This is not a valid route")

    def do_check_status_of(self, args):
        """Can be used to check ticket sales overall and by route inclusive of the ticket id.  Helps for refunds"""
        if args == "tickets":
            global all_tickets
            print all_tickets
        elif args == "blue":
            global blue_route_ticket
            print ticket.blue_route_ticket
        elif args == "red":
            global red_route_ticket
            print ticket.red_route_ticket
        elif args == "green":
            global green_route_ticket
            print ticket.green_route_ticket
        elif args == "sales":
            global ticket_sales_count
            print ticket.ticket_sales_count
        else:
            print("Please enter: 'blue', 'green', 'red', 'sales', or 'tickets' and options to check")


if __name__ == '__main__':
    Big_Bus().cmdloop()
