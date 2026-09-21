class goa:
    name=""
    drink=""
    def party():
        print("lets party..")
        def beach():
            print("Enjoy the beach")
ramesh=goa()
suresh=goa()

ramesh.name="ramesh"
ramesh.drink="Yes"
suresh.name="suresh"
suresh.drink="No"

print(ramesh.name)
print("Drink:", ramesh.drink)
print(suresh.name)
print("Drink:", suresh.drink)

ramesh.party()
suresh.party()


