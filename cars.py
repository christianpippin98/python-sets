showroom = set()

showroom.add("1967 Ford Mustang")
showroom.add("Tesla CyberTruck")
showroom.add("Toyota 4Runner")
showroom.add("Lamborghini Urus")
showroom.add("Lamborghini Urus")

showroom.update({"Porsche 911", "1969 Chevy Stingray"})

showroom.discard("Toyota 4Runner")

print("Showroom", showroom)

junkyard = {
    "Mini Cooper",
    "Tesla CyberTruck",
    "1969 Chevy Stingray",
    "Ford Expedition",
    "Toyota Corolla"
    }

print("Junkyard", junkyard)

cars_in_both = showroom.intersection(junkyard)

print("Cars In Both", cars_in_both)

showroom = showroom.union(junkyard)

showroom.discard("Mini Cooper")

print("New Showroom", showroom)

