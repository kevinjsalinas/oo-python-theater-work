

# role ---<  # audition 

class Audition:

    all_audition_instances = []

    def __init__(self, actor, location, hired, role_instance):
        self.actor = actor
        self.location = location
        self.hired = hired
        self.role = role_instance
        Audition.all_audition_instances.append(self)

    def role(self):
        return self.role

    def call_back(self):
        self.hired = True

