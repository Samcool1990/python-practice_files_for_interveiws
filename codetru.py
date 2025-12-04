# Online Assessment:
# Appointment Management System:
from datetime import datetime

class Appointment:
    def __init__(self, start_time, end_time, description):
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def __str__(self):
        return f"{self.start_time} to {self.end_time}: {self.description}"

class AppointmentManager:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, start_time, end_time, description):
        # Check for overlapping appointments
        for appointment in self.appointments:
            if not (end_time <= appointment.start_time or start_time >= appointment.end_time):
                print("Error: Appointment overlaps with an existing appointment.")
                return

        new_appointment = Appointment(start_time, end_time, description)
        self.appointments.append(new_appointment)
        self.appointments.sort(key=lambda x: x.start_time)
        print("Appointment added successfully.")

    def delete_appointment(self, description):
        for appointment in self.appointments:
            if appointment.description == description:
                self.appointments.remove(appointment)
                print("Appointment deleted successfully.")
                return
        print("Error: Appointment not found.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def view_one_appointment(self, description):
        for appointment in self.appointments:
            if appointment.description == description:
                print(appointment)
                return
        print("Error: Appointment not found.")

# Main Program
if __name__ == "__main__":
    manager = AppointmentManager()

    while True:
        print("\nAppointment Management System")
        print("1. Add Appointment")
        print("2. Delete Appointment")
        print("3. View All Appointments")
        print("4. View One Appointment")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                start_time = datetime.strptime(input("Enter start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                end_time = datetime.strptime(input("Enter end time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                if end_time <= start_time:
                    print("Error: End time must be after start time.")
                    continue
                description = input("Enter appointment description: ")
                manager.add_appointment(start_time, end_time, description)
            except ValueError:
                print("Error: Invalid date format.")

        elif choice == "2":
            description = input("Enter the description of the appointment to delete: ")
            manager.delete_appointment(description)

        elif choice == "3":
            manager.view_appointments()

        elif choice == "4":
            description = input("Enter the description of the appointment to view: ")
            manager.view_one_appointment(description)

        elif choice == "5":
            print("Exiting Appointment Management System. Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please try again.")



#Question: Orders:
# Orders:
# orderid, customerid, date(yyyy-mm-dd) 
# Oder_Details:
# orderid, unirprice, quantity
# find the customerid who has the most amount of orders.
# output should be yyyy, mm, customerid, totalamountordered
# Note: orderid is linked with both tables.

# Answer: 
# SELECT
#     YEAR(o.date) AS yyyy,
#     MONTH(o.date) AS mm,
#     o.customerid,
#     SUM(od.unitprice * od.quantity) AS totalamountordered
# FROM
#     Orders o
# JOIN
#     Order_Details od
# ON
#     o.orderid = od.orderid
# GROUP BY
#     YEAR(o.date),
#     MONTH(o.date),
#     o.customerid
# ORDER BY
#     yyyy, mm, totalamountordered DESC
# LIMIT 1;



# SQL
# WITH monthly_customer_totals AS (
#   SELECT
#     EXTRACT(YEAR FROM o.date) AS yyyy,
#     EXTRACT(MONTH FROM o.date) AS mm,
#     o.customerid,
#     SUM(od.unitprice * od.quantity) AS totalamountordered
#   FROM Orders AS o
#   JOIN Order_Details AS od
#     ON od.orderid = o.orderid
#   GROUP BY
#     EXTRACT(YEAR FROM o.date),
#     EXTRACT(MONTH FROM o.date),
#     o.customerid
# )
# SELECT
#   yyyy,
#   mm,
#   customerid,
#   totalamountordered
# FROM (
#   SELECT
#     mct.*,
#     ROW_NUMBER() OVER (
#       PARTITION BY yyyy, mm
#       ORDER BY totalamountordered DESC, customerid
#     ) AS rn
#   FROM monthly_customer_totals AS mct
# ) AS ranked
# WHERE rn = 1
# ORDER BY yyyy, mm;
