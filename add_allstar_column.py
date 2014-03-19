def add_allstar_column(regular_season_path, allstar_path):
    # opening files
    regular_file = open(regular_season_path, 'r')
    allstar_file = open(allstar_path, 'r')

    # read files to memory as lists
    allstar = allstar_file.readlines()
    regular = regular_file.readlines()

    # closing files
    allstar_file.close()
    regular_file.close()

    # delete first line (headers) in both files
    del allstar[0]
    #store this line to use as header in the output file
    output_header = regular.pop(0).strip() + ",allstar\n"


    # start reading files
    print 'processing...'

    output_players = []
    for regular_line in regular:
        # player is initially not considered allstar
        is_allstar = 'NO'

        # geting regular season player info
        regular_player = regular_line.strip().split(',')
        regular_name = regular_player[0].upper()
        regular_year = regular_player[1]

        for allstar_line in allstar:
            # geting allstar player info
            allstar_player = allstar_line.split(',')
            allstar_name = allstar_player[0].upper()
            allstar_year = allstar_player[1]

            # if player of regular season was in allstar in that year change tag
            if regular_name == allstar_name and regular_year == allstar_year:
                is_allstar = 'YES'
                break

        # add the modified player line to the output list of players
        output_players.append(regular_line.strip() + "," + is_allstar + "\n")


    # write on output file and close program
    output_file = open('output.csv', 'w')
    output_file.write(output_header)
    output_file.writelines(output_players) 
    output_file.close()                 
    print 'finished'

if __name__ == "__main__":
    add_allstar_column('nba_data/player_regular_season.csv',
                       'nba_data/player_allstar.csv')
