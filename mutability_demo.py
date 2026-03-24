from os import system

def curve_grades(grades: dict) -> dict:
    # Intention: create a NEW dictionary with +5 points
    curved = grades.copy()   # ❌ BUG: this variable still references the original gradebook!

    for student in curved:
        curved[student] += 5

    return curved




gradebook = {
    "Alice": 90,
    "Bob": 85,
    "Carlos": 78
}

while True:
    
    print("\nPowerSchool Command Line Version 1.0")
    print("\nMENU\n1 - View Gradebook\n2 – Curve Gradebook\n3 – Exit Program")
    command = input("\nWhat will you do? ")
    system("clear")
    if command == "1":
        print("\nCurrent Gradebook: ", gradebook)
    elif command == "2":
        print("\nOriginal Gradebook: ", gradebook)
        curved_gradebook = curve_grades(gradebook)
        print("\nNew Gradebook: ", curved_gradebook)
        command = input("\nAccept changes? Y/N ")
        if command == "Y":
            print("\nGradebook Updated")
            gradebook = curved_gradebook
        else:
            print("\nChanges Rejected")
    elif command == "3":
        print("Exiting program...")
        break
    else:
        print("\nCommand Not Recognized")
        