age = int(input("Enter your current age: "))

if age < 0:
    print("You have not been born yet")

else:
    if age in range(0,4):
        print("You are an Infant/Toddler")

    else:
        if age in range(4,7):
            print("You are in your Early stage of Childhood")

        else:
            if age in range(7,9):
                print("You're in your Middle stage of Childhood")

            else:
                if age in range(9,13):
                    print("You're in your Late stages of Chidhood")

                else:
                    if age in range(13,21):
                        print("You are in the stage of Adolescence")

                    else:
                        if age in range(21,36):
                            print("You are in the stage of Early Adulthood")

                        else:
                            if age in range(36,51):
                                print("You have reached Midlife")
                                
                            else:
                                if age in range(51,81):
                                    print("You are in the stage of Mature Adulthood")

                                else:
                                    if age in range(81,150):
                                        print("You have reached the stage of late adult hood")

                                    else:
                                        if age in range(151,1000):
                                            print("Dead")