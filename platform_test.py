import big_bus
import pytest
import datetime
import pickle


@pytest.fixture
def ticket1():
        return 2

def test_buy_ticket1(ticket1):
    BB = big_bus.Big_Bus()
    tickets = BB.do_create_tickets(ticket1)
    assert BB.number_of_tickets == 2
    assert BB.discount == False

@pytest.fixture
def ticket2():
        return 4

def test_buy_ticket2(ticket2):
    BB = big_bus.Big_Bus()
    tickets = BB.do_create_tickets(ticket2)
    assert BB.number_of_tickets == 4
    assert BB.discount == True

@pytest.fixture
def ticket3():
        return 5

def test_buy_ticket3(ticket3):
    BB = big_bus.Big_Bus()
    tickets = BB.do_create_tickets(ticket3)
    assert BB.number_of_tickets == 0
    assert BB.discount == False

@pytest.fixture
def ticket4():
        return ""

def test_buy_ticket4(ticket4):
    BB = big_bus.Big_Bus()
    tickets = BB.do_create_tickets(ticket4)
    assert BB.number_of_tickets == 0
    assert BB.discount == False

@pytest.fixture
def date1():
        return "2018-05-01"

def test_set_date1(date1):
    BB = big_bus.Big_Bus()
    BB.do_date(date1)
    assert BB.month == 05
    assert BB.day == 01
    assert BB.year == 2018
    assert BB.within_Date_Margin == True

@pytest.fixture
def date2():
        return "2018-05-22"

def test_set_date2(date2):
    BB = big_bus.Big_Bus()
    BB.do_date(date2)
    assert BB.month == 05
    assert BB.day == 22
    assert BB.year == 2018
    assert BB.within_Date_Margin == False

@pytest.fixture
def route1():
        return "green"

def test_route1(route1):
    BB = big_bus.Big_Bus()
    BB.do_route(route1)
    assert BB.route == "green"

@pytest.fixture
def route2():
        return "red"

def test_route2(route2):
    BB = big_bus.Big_Bus()
    BB.do_route(route2)
    assert BB.route == "red"

@pytest.fixture
def route3():
        return "blue"

def test_route3(route3):
    BB = big_bus.Big_Bus()
    BB.do_route(route3)
    assert BB.route == "blue"

@pytest.fixture
def route3():
        return "Blue"

def test_route3(route3):
    BB = big_bus.Big_Bus()
    BB.do_route(route3)
    assert BB.route == "blue"

@pytest.fixture
def route4():
        return ""

def test_route4(route4):
    BB = big_bus.Big_Bus()
    BB.do_route(route4)
    assert "This is not a valid route"

@pytest.fixture
def buy1():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 01
    BB.route = "blue"
    BB.number_of_tickets = 2
    BB.discount = False
    BB.within_Date_Margin = True
    return BB

def test_buy_ticket(buy1):
    buy1.do_buy("")
    assert len(buy1.all_tickets_sold) == 2
    assert len(big_bus.all_tickets) == 2


@pytest.fixture
def buy2():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 28
    BB.route = "green"
    BB.number_of_tickets = 1
    BB.discount = False
    BB.within_Date_Margin = False
    return BB

def test_buy_ticket2(buy2):
    buy2.do_buy("")
    assert "Need more infomation to buy a ticket"

@pytest.fixture
def buy3():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 01
    BB.route = ""
    BB.number_of_tickets = 1
    BB.discount = False
    BB.within_Date_Margin = True
    return BB

def test_buy_ticket3(buy3):
    buy3.do_buy("")
    assert "Need more infomation to buy a ticket"

@pytest.fixture
def buy4():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 01
    BB.route = "red"
    BB.number_of_tickets = 4
    BB.discount = True
    BB.within_Date_Margin = True
    return BB

def test_buy_ticket4(buy4):
    big_bus.all_tickets = []
    buy4.do_buy("")
    assert len(buy4.all_tickets_sold) == 4
    assert len(big_bus.all_tickets) == 4

@pytest.fixture
def big_bus1():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 01
    BB.route = "red"
    BB.number_of_tickets = 4
    BB.discount = True
    BB.within_Date_Margin = True
    return BB

@pytest.fixture
def big_bus2():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "red"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1


def test_check_system(big_bus1, big_bus2):
    big_bus.all_tickets = []
    big_bus1.do_buy("")
    big_bus2.do_buy("")
    big_bus2.do_check_status_of("red")
    assert len(big_bus.ticket.red_route_ticket) == 2

@pytest.fixture
def big_bus3():
    BB = big_bus.Big_Bus()
    BB.year = 2018
    BB.month = 05
    BB.day = 02
    BB.route = "blue"
    BB.number_of_tickets = 4
    BB.discount = True
    BB.within_Date_Margin = True
    return BB

@pytest.fixture
def big_bus4():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1


def test_check_system1(big_bus3, big_bus4):
    big_bus.ticket.green_route_ticket = {}
    big_bus.ticket.blue_route_ticket = {}
    big_bus3.do_buy("")
    big_bus4.do_buy("")
    big_bus4.do_check_status_of("blue")
    big_bus4.do_check_status_of("green")
    assert len(big_bus.ticket.green_route_ticket) == 1
    assert len(big_bus.ticket.blue_route_ticket) == 1

@pytest.fixture
def big_bus5():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1


def test_check_system2(big_bus5):
    big_bus.ticket.ticket_sales_count = 0
    big_bus5.do_buy("")
    big_bus5.do_check_status_of("sales")
    assert big_bus.ticket.ticket_sales_count == 2

@pytest.fixture
def big_bus_sales():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1

def test_check_sales_date(big_bus_sales):
    big_bus.all_tickets = []
    big_bus_sales.do_buy("")
    big_bus_sales.do_sales_by_date("2018-05-02")
    assert big_bus_sales.count == 2

@pytest.fixture
def big_bus_sales1():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1

def test_check_sales_date1(big_bus_sales1):
    big_bus.all_tickets = []
    big_bus_sales1.do_buy("")
    big_bus_sales1.do_sales_by_date("2018-05-04")
    assert big_bus_sales1.count == 0

@pytest.fixture
def refund():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1

def test_refund_ticket(refund):
    big_bus.all_tickets = []
    big_bus.ticket.ticket_sales_count = 0
    big_bus.ticket.ticket_id_num = 1000000
    refund.do_buy("")
    refund.do_refund("2018-05-02 1000001 green")
    assert len(big_bus.all_tickets) == 1
    assert big_bus.ticket.ticket_sales_count == 1

@pytest.fixture
def refund1():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "green"
    BB1.number_of_tickets = 3
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1

def test_refund_ticket1(refund1):
    big_bus.all_tickets = []
    big_bus.ticket.ticket_sales_count = 0
    big_bus.ticket.green_route_ticket = {}
    big_bus.ticket.ticket_id_num = 1000000
    refund1.do_buy("")
    refund1.do_refund("2018-05-02 1000001 green")
    assert len(big_bus.all_tickets) == 2
    assert big_bus.ticket.green_route_ticket[datetime.date(2018, 05, 02)] == 2
    assert big_bus.ticket.ticket_sales_count == 2

@pytest.fixture
def refund2():
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "red"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    return BB1

def test_refund_ticket2(refund2):
    big_bus.all_tickets = []
    big_bus.ticket.red_route_ticket = {}
    big_bus.ticket.ticket_id_num = 1000000
    refund2.do_buy("")
    refund2.do_refund("1000001 red")
    assert len(big_bus.all_tickets) == 2
    assert big_bus.ticket.red_route_ticket[datetime.date(2018, 05, 02)] == 2
    assert "Unable to refund that ticket"

@pytest.fixture
def quit_start():
    big_bus.all_tickets = []
    big_bus.ticket.red_route_ticket = {}
    big_bus.ticket.ticket_id_num = 1000000
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "red"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    BB1.do_buy("")
    BB1.do_quit("")


def test_startup(quit_start):
    BB1 = big_bus.Big_Bus()
    BB1.do_program_startup("")
    assert len(big_bus.all_tickets) == 2
    assert big_bus.ticket.red_route_ticket[datetime.date(2018, 05, 02)] == 2

@pytest.fixture
def quit_start():
    big_bus.all_tickets = []
    big_bus.ticket.red_route_ticket = {}
    big_bus.ticket.ticket_id_num = 1000000
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "red"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    BB1.do_buy("")
    BB1.do_quit("")


def test_startup(quit_start):
    BB1 = big_bus.Big_Bus()
    BB1.do_program_startup("")
    assert len(big_bus.all_tickets) == 2
    assert big_bus.ticket.red_route_ticket[datetime.date(2018, 05, 02)] == 2

@pytest.fixture
def quit_start1():
    reset_pickle()
    big_bus.all_tickets = []
    big_bus.ticket.red_route_ticket = {}
    big_bus.ticket.ticket_id_num = 1000000
    BB1 = big_bus.Big_Bus()
    BB1.year = 2018
    BB1.month = 05
    BB1.day = 02
    BB1.route = "red"
    BB1.number_of_tickets = 2
    BB1.discount = False
    BB1.within_Date_Margin = True
    BB1.do_buy("")
    BB1.do_quit("")
    BB2 = big_bus.Big_Bus()
    BB2.year = 2018
    BB2.month = 05
    BB2.day = 05
    BB2.route = "blue"
    BB2.number_of_tickets = 3
    BB2.discount = False
    BB2.within_Date_Margin = True
    BB2.do_buy("")
    BB2.do_quit("")


def test_startup1(quit_start1):
    BB1 = big_bus.Big_Bus()
    BB1.do_program_startup("")
    assert len(big_bus.all_tickets) == 5
    assert big_bus.ticket.red_route_ticket[datetime.date(2018, 05, 02)] == 2
    assert big_bus.ticket.blue_route_ticket[datetime.date(2018, 05, 05)] == 3

def reset_pickle():
    global ticket_id_num
    global all_tickets
    global ticket_sales_count
    global green_route_ticket
    global red_route_ticket
    global blue_route_ticket
    filein = open("stored_values.pkl", "w")
    pickle.dump(1000000, filein)
    pickle.dump(0, filein)
    pickle.dump({}, filein)
    pickle.dump({}, filein)
    pickle.dump({}, filein)
    pickle.dump([], filein)
