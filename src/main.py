'''main module functionality'''
import database


def create_competitor(first_name, last_name):
    '''dummy function for creating a competitor'''
    ftr = database.Competitor(first_name=first_name, last_name=last_name)
    database.create_competitor(ftr)

def log_fight():
    '''dummy function for logging a fight'''
    winner = "fb047af0-bbc7-42d9-8e5e-7c3f778d06ea"
    loser = "6af556e9-4fbe-44f7-8dfe-fb84698c1c9d"
    fight = database.Fight(winner=winner, loser=loser)
    database.log_fight(fight)

def update_elo(first_name, last_name, new_elo):
    '''dummy function for updating the elo of a competitor'''
    uid = query(first_name=first_name, last_name=last_name)
    database.update_elo(uid, new_elo)

def create_fight():
    '''dummy function for setting up a fight'''
    winner_uid = "e65a6c52-8849-416a-882c-021bcf38d087"
    loser_uid = "6a86117b-6682-4e5f-8020-3e44e364a827"

def query(first_name, last_name):
    '''dummy function for getting the uid from the name'''
    return database.query_by_full_name(first_name, last_name)

def main():
    '''main function'''
    create_competitor(first_name = "Miro", last_name = "Lahtela")

    # create_fight()
    # log_fight()
    # update_elo(first_name="Nikos", last_name="Kyriakopoulos", new_elo=1000)
    # query(first_name = "Nikos", last_name = "Kyriakopoulos")
    # edit a competitor and update the database
    # remove a competitor from the database

if __name__ == "__main__":
    main()
