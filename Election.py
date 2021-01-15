


def FileInitialize():
    input_filename = input("Enter file name:")
    # Output filename
    output_filename = "REPORT-" + input_filename
    # Both filees for read and writ o-peration
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    # Sum of all years percentage of registered
    total_registered_percent = 0.0
    # Year count
    years_counter = 0
    # Year less than 60% of registered casted votes
    years_LT60_percent = 0
    # Years more than 80% of registered casted votes
    years_MT80_percent = 0

    ballots_count = 0
    
    
    
    
    def Calculation():
        while True:
            year = input_file.readline().rstrip('\n')
            if (year == ''):
             break
            eligible_voters = int(input_file.readline())
            registered_voters = int(input_file.readline())
            ballot_casted = int(input_file.readline())
            registered_percent = registered_voters / eligible_voters * 100
            voted_percent = ballot_casted / eligible_voters * 100
            if ballot_casted < 60 / 100 *registered_voters:
                years_LT60_percent += 1

            elif ballot_casted > 80 / 100 * registered_voters:
                years_MT80_percent += 1

        print("The total Number of years listed:", years_counter)
        print("Total ballots cast in all these years:{:,}".format(ballots_count))
        print("Average percnt of eligible voters registred: {:.2f} %".format(total_registered_percent / years_counter))
        print("Number of years with less than 60% of registered casting ballots:", years_LT60_percent)
        print("Percentage of Years with more than 80% of Registered voters casting ballots:{:.1f}%".format(years_MT80_percent / years_counter * 100) )
        print("An output file:", output_filename,"has been created")




    def FileOP():
        Calculation()
        
        output_filename = "REPORT-" + input_filename
        # Both filees for read and writ o-peration
        input_file = open(input_filename, 'r')
        output_file = open(output_filename, 'w')

        output_line = 'In {}, {:.2f} % registered and {:.2f}%voted.\n'.format(year, registered_percent, voted_percent)

        output_file.write(output_line)

        years_counter += 1
        ballots_count += ballot_casted
        total_registered_percent += registered_percent
        input_file.close()
        output_file.close()





