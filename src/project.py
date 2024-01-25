
# TODO: DDL, milestones
class Project:
    import bson
    def __init__(self, name, pic:bson.ObjectId, members:list[bson.ObjectId]) -> None:
        self.name = name
        self.pic = pic
        self.members = members