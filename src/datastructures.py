
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        self._members.append(member)
        return True

    def delete_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                self._members.pop(i)
                return True
        return False
        
    def get_member(self, id):
        # fill this method and update the return
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                return self._members[i]
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the member with the given id
        for i in range(len(self._members)):
            if self._members[i] == member:
                self._members[i]["id"] = id
                return True
        return False
            