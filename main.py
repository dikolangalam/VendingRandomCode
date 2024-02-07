import tkinter as tk

class VendingMachine:
    def __init__(self):
         self.chips = {
            1: {"name": " Lays ", "stock  ": 20, "price": 30},
            2: {"name": " Chippy", "stock  ": 15, "price": 25},
            3: {"name": " Piattos", "stock  ": 25, "price": 20},
            4: {"name": " V-Cut", "stock  ": 10, "price": 15},
            5: {"name": " Mr. Chips", "stock  ": 40, "price": 25},
            6: {"name": " Nova", "stock  ": 30, "price": 20},
            7: {"name": " Clover", "stock  ": 20, "price": 20},
            8: {"name": " Pic-A", "stock  ": 40, "price": 30},
            9: {"name": " Doritos", "stock  ": 10, "price": 15},
            10: {"name": "Mang Juan", "stock  ": 20, "price": 20},
        }

    def display_chips(self):
        display_text = f"{'Chips':<15}{'Number of Stock':<20}{'Price'}\n"
        for key, chip in self.chips.items():
            name = chip['name']
            stock = str(chip['stock  '])
            price = str(chip['price'])

            display_text += f"[{key}] {name:<15} {stock:<20} {price}\n"
        return display_text

    def buy_chips(self, choice, quantity, payment):
        if choice in self.chips:
            chip = self.chips[choice]
            if chip["stock  "] >= quantity:
                total_price = chip["price"] * quantity
                if payment >= total_price:
                    change = payment - total_price
                    chip["stock  "] -= quantity
                    return f"Change: {change}\nThank you! You've purchased {quantity} {chip['name']}(s)."
                else:
                    return "Insufficient payment."
            else:
                return f"Insufficient stock for {chip['name']}."

class VendingMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vending Machine")

        self.vending_machine = VendingMachine()

        self.display = tk.Text(self.root, height=15, width=50, bg="lightgray", font=("Bookman Old Style", 12))
        self.display.pack()

        self.display_chips()

        self.choice_label = tk.Label(self.root, text="Select Chips (enter the number):", font=("Bookman Old Style", 10, "bold"))
        self.choice_label.pack()
        self.choice_entry = tk.Entry(self.root, font=("Bookman Old Style", 10))
        self.choice_entry.pack()

        self.quantity_label = tk.Label(self.root, text="Enter the quantity you want to buy:", font=("Bookman Old Style", 10, "bold"))
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root, font=("Bookman Old Style", 10))
        self.quantity_entry.pack()

        self.payment_label = tk.Label(self.root, text="Enter Payment:", font=("Bookman Old Style", 10, "bold"))
        self.payment_label.pack()
        self.payment_entry = tk.Entry(self.root, font=("Bookman Old Style", 10))
        self.payment_entry.pack()

        self.buy_button = tk.Button(self.root, text="Buy", command=self.buy_chips, bg="green", fg="white", font=("Bookman Old Style", 10))
        self.buy_button.pack()

        self.another_purchase_button = tk.Button(self.root, text="Another Purchase", command=self.another_purchase, bg="blue", fg="white", font=("Bookman Old Style", 10))
        self.another_purchase_button.pack()

    def display_chips(self):
        chips_info = self.vending_machine.display_chips()
        self.display.insert(tk.END, chips_info)

    def buy_chips(self):
        choice_entry_value = self.choice_entry.get()
        quantity_entry_value = self.quantity_entry.get()
        payment_entry_value = self.payment_entry.get()

        # Check if input contains any letter
        if not (choice_entry_value.isdigit() and quantity_entry_value.isdigit() and payment_entry_value.isdigit()):
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, "Please use the corresponding number to choose.\n\n")
            self.display.insert(tk.END, self.vending_machine.display_chips())
            return

        # If all inputs are digits, proceed with purchase
        choice = int(choice_entry_value)
        quantity = int(quantity_entry_value)
        payment = int(payment_entry_value)

        purchase_result = self.vending_machine.buy_chips(choice, quantity, payment)
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, purchase_result)
        self.display.insert(tk.END, "\n\n")
        self.display.insert(tk.END, self.vending_machine.display_chips())  # Show updated inventory

    def another_purchase(self):
        self.display.delete(1.0, tk.END)
        self.choice_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.payment_entry.delete(0, tk.END)
        self.display_chips()

root = tk.Tk()
app = VendingMachineGUI(root)
root.mainloop()
