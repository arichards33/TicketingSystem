# Homework #2 Big Bus Ticketing Revamped

This application is for an on-street sales staff at a Big Bus location.

Customers can arrive at a corner and expect to be able to perform the following transactions with the salesperson:

- Buy tickets for an all-day pass up to 10 days in advance
- Get a refund for a ticket that was sold for a future date (i.e. not today)

The application can

- Sell tickets for any bus route, for today or for any date up to 10 days from now
- Issue refunds for future tickets
- Generate a report of the number of tickets sold today for a given route
- Generate a report of the total number of tickets sold on any given date (for all routes)

# How It Works

To run the application you will need to run the 'big_bus.py' file to start up. Once the application is running the first command you need to run is always "program_startup".  This will make sure any previous sales that were made are accounted for and keeps track of tickets if any refunds need to be made, this command will also ensure that ticket IDs remain unique between application sessions. After 'program_startup' if someone wants to buy a ticket the salesperson will need to collect the following information: # of tickets to be purchased, the date the ticket is to be used, and the route. These will all be collected with separate commands.  
- 'create_tickets' = enter the number of tickets to be purchased
- 'date' = enter the date the ticket is to be used
- 'route' = enter the color of the route to be run

After all 3 items have been entered, run the command 'buy' to complete the sale.

Outline of steps that must be run:
1. 'program_startup'
2. 'create_tickets (#)'
3. 'date (yyyy-mm-dd)'
4. 'route (color)'
5. 'buy'

Other commands that the program runs are to check the total sales and sales per route and make refunds to unused tickets.

- The 'sales_by_date' command takes a date as an input and will return the total number of tickets sold for any given day
- The 'refund' command takes a date, ticket ID, and route color as inputs
- The 'check_status_of' command takes an input of what you want to check. Options include: "blue", "green", "red", "sales", "tickets".  The colors return the tickets sold for that specific route, tickets returns all the tickets sold inclusive of the ticket ID, and sales returns the total number of sales.

Outline of how these commands are run:
1. 'sale (yyyy-mm-dd)'
2. 'refund (yyyy-mm-dd ticketID route)'
3. 'check_status_of (option)'

** parenthesis are not needed around any args for any of the commands in the application **

# Version

Version 1.1

# Author

Alex Richards
