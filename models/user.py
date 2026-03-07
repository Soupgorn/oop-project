class User :
    def __init__(self,username,password,Ticket = None):
        self.__username = username
        self.__password = password
        self.__ticket_List = []

    @property
    def username (self) : return self.__username

    @property
    def ticket_list (self) : return self.__ticket_List

