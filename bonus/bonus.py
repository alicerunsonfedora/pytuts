# Objects (Basic)
# Objects can contain variables and methods alike.
# This can be used for several cases.


# Defining a class for an object
class BonusClass:
    # These vars are specific to this object
    isBonus = True
    bonusNumber = 1
    bonusName = ""

    # This function is required as this initializes the object
    def __init__(self, name_for_bonus):
        self.bonusName = name_for_bonus
        print("This bonus is called " + self.bonusName + ".")
        return

    # self is a required parameter so it can reference
    # things inside of itself.
    def report_bonus(self):
        if self.isBonus:
            print("This is a bonus. Number " + str(self.bonusNumber) + " , in fact.")


if __name__ == "__main__":
    # This class is now stored in an object
    bonus_container = BonusClass("Sierra")

    # We can call the functions inside of that class here.
    bonus_container.report_bonus()