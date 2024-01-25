class DiscordGuildMember:
    def __init__(self, nick, name, id) -> None:
        self.nick = nick
        self.name = name
        self.id = id

class TeamMember:
    from enum import Enum

    class Rank(Enum):
        INTERVIEW_PASSED = "Interview Passed"
        TUTORIAL_PASSED = "Tutorial Passed"
        JUNIOR = "Junior"
        SENIOR = "Senior"

    class Department(Enum):
        ALGORITHM = "Algorithm"
        EMBEDDED = "Embedded"
        HARDWARE = "Hardware"
        MECHANIC = "Mechanic"
        MEDIA = "Media"
        OPERATION = "Operation"

    def __init__(self, rank:Rank, department:Department) -> None:
        self.rank = rank
        self.deparment = department
        pass
    

class HKUSTer:
    def __init__(self, itsc:str, itsc_email:str, major:str = None, school = None) -> None:
        self.itsc = itsc
        self.itsc_email = itsc_email
        self.major = major
        self.school = school


class Contact:
    def __init__(self, gmail, phone_hk = None, phone_mainland = None):
        self.gmail = gmail
        self.phone_hk = phone_hk
        self.phone_mainland = phone_mainland

class Person:
    def __init__(self, full_name, discord:dict = None, team:dict = None, university:dict = None, contact:dict = None) -> None:
        self.full_name = full_name
        self.discord = discord
        self.team = team
        self.university = university



    