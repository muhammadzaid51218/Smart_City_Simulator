class TrafficLight:

    #Constructor
    def __init__(self,location ,state):
      # Class Variables
        self.location = location 
        # States ( Red ,Yellow ,Green )
        self.state = state

    # for change state.
    def change_state(self,new_state):
        self.state = new_state
    
    #( Dunder Method ) __str__ for show current State
    def __str__(self):
        return "Current Sate is {}".format(self.state)