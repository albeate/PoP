
class State(object):
    """The state base class"""
    def __init__(self, stateMachine):
        self.m_nextStateDict = {}
        self.m_stateMachine = stateMachine
    
    def addNextState(self, stateName, state):
        self.m_nextStateDict[stateName] = state
    
    def nextState(self, stateName):
        self.m_stateMachine.switchToState(self.m_nextStateDict[stateName])
        
    def handleRequest(self, params):
        pass


class StateMachine(object):
    """The state machine base class"""        
    def request(self, params):
        self.m_currentState.handleRequest(params)
        
    def switchToState(self, newState):
        self.m_currentState = newState


class Slukket(State):
    """Slukket tilstand"""    
    def handleRequest(self, params):
        self.nextState("Taendt")
        
    def __str__(self):
        return "Kontakten er slukket"
        
class Taendt(State):
    """Taendt tilstand"""
    def handleRequest(self, params):
        self.nextState("Slukket")

    def __str__(self):
        return "Kontakten er taendt"


# Initialisering
maskine = StateMachine()
slukketTilstand = Slukket(maskine)
taendtTilstand = Taendt(maskine)
slukketTilstand.addNextState("Taendt", taendtTilstand)
taendtTilstand.addNextState("Slukket", slukketTilstand)
maskine.switchToState(slukketTilstand)

print maskine.m_currentState
for i in range(5):
    maskine.request(None)
    print maskine.m_currentState
