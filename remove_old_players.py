#function that removes the players from older seasons that do not have all the data available...

def remove_players(regular_season_path, player_career):
    # opening files
    regular_file = open(regular_season_path, 'r')
    player_career_file = open(player_career, 'r')

    # read files to memory as lists
    player_career = player_career_file.readlines()
    regular = regular_file.readlines()

    # closing files
    player_career_file.close()
    regular_file.close()

    # start reading files
    print 'processing...'
    counter = 0
    output_players = []
    for player_career_line in player_career:
        # geting the player with the career data
        career_player = player_career_line.strip().split(',')
        player_c_name = career_player[0].upper().strip()
        for regular_line in regular:
            # geting regular season player name
            regular_player = regular_line.upper().strip()
            if player_c_name in regular_player:
                output_players.append(player_career_line.strip() + '\n')
                regular.pop(counter)
                counter = 0
                break
        #index to remove from list the already added player, to optimize the algorithm...
        counter += 1
    # write on output file and close program
    output_file = open('output2.csv', 'w')
    output_file.writelines(output_players) 
    output_file.close()                 
    print 'finished'

if __name__ == "__main__":
    remove_players('input_data.csv',
                       'nba_data/player_career.csv')
