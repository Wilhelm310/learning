piston = int(input("Enter input limit:"))
force = int(input("Enter number"))

if piston >= force:
    print("Running")
elif piston < force:
    print("Exceed")