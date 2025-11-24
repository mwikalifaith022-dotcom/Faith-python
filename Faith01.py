import time
import os

class AttributeSet:
    def __init__(self, categoryName, traits):
        self.categoryName = categoryName
        self.traits = traits

def clearScreen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def displaySet(setObj):
    print("----------------------------------------")
    print(f"   SCANNING SECTOR: {setObj.categoryName}")
    print("----------------------------------------")
    for trait in setObj.traits:
        print(f" > {trait}")
    print("\n[Status] Processing next data packet...\n")

def main():
    roommateData = [
        AttributeSet(
            "IDENTIFICATION", [
                "Subject ID: 'The Roommate'",
                "Name: 'Maya'",
                "Age: 24",
                "Occupation: Architecture Student / Barista"
            ]
        ),
        AttributeSet(
            "PHYSICAL METRICS", [
                "Height: 5'7\" (170 cm)",
                "Build: Slender, poor posture from drafting tables",
                "Skin Tone: Warm Olive",
                "Hair: Dark brown, perpetually in a messy bun",
                "Eyes: Hazel, usually squinting at a screen"
            ]
        ),
        AttributeSet(
            "APPAREL & AESTHETIC", [
                "Top: Oversized vintage university sweatshirt (stolen)",
                "Bottoms: Black leggings (covered in cat hair)",
                "Footwear: Fuzzy socks inside Crocs",
                "Accessories: Blue light glasses, silver nose ring"
            ]
        ),
        AttributeSet(
            "BEHAVIORAL QUIRKS", [
                "Diet: 80% Iced Coffee, 20% Instant Ramen",
                "Sleep Cycle: Nocturnal (Active 11 PM - 4 AM)",
                "Volume Level: Hums lo-fi beats unconsciously",
                "Hazard Level: Leaves dishes in sink for 3-5 business days"
            ]
        )
    ]

    print("INITIALIZING ROOMMATE SURVEILLANCE PROTOCOL...")
    time.sleep(2)

    cycleCount = 1
    while True:
        clearScreen()
        print(f"=== CYCLE {cycleCount} IN PROGRESS ===")
        print("Target acquired.\n")

        for setObj in roommateData:
            displaySet(setObj)
            time.sleep(5)

        print("Cycle complete. Rebooting scan sequence...")
        time.sleep(2)
        cycleCount += 1

if __name__ == "__main__":
    main()
