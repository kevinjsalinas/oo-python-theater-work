from .audition import Audition

# role ---<  # audition 

class Role:

    def __init__(self, character_name):
        self.name = character_name
        
    # Roles should only have a character_name (string) and have many auditions.
    # Role#auditions returns ALL OF THE AUDITIONS associated with this role.
    
    @property
    def auditions(self):
        return [a for a in Audition.all_audition_instances if a.role == self] 

    #INVOKKKEEEEEEEEEEE DAMMMMMIT OR USE PROPERTies IF NEEDED
    def actors(self):
        return [a.actor for a in self.auditions()]

    def locations(self):
        return [a.location for a in self.auditions()]

    def lead(self):
        hired_instance = ""
        for a in self.auditions:
            if a.hired == True:
                hired_instance = a
                return hired_instance
            else:
                print("no actor has been hired for this role")
        # return hired_instance 


        # for a in self.auditions:
        #     if a.hired == True:
        #         hired_instance = a.actor
        #     else:
        #         print("No actor has been hired for this role")
        # return hired_instance

      





