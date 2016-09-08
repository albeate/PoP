
class State(object):
    """The state base class""" 
    def __init__(self, stateName):
        self.stateName = stateName
           
    def handleRequest(self, params):
        """Let the state do some work"""
        pass
        
    def onEnter(self):
        """Called on entering the state: 
        Do some initialization of the state"""
        pass
        
    def onLeave(self):
        """Called on leaving the state:
        Do some clean-up of the state"""
        pass
        
    def getStateName(self):
        return self.stateName


class StateMachine(object):
    """The state machine base class"""
    def __init__(self):
        self.m_currentState = None
        self.m_stateDict = {}
        self.m_stateTransitions = {}
        
    def request(self, params):
        if self.m_currentState:
            self.m_currentState.handleRequest(params)
        
    def switchToState(self, newState):
        if self.m_currentState:
            self.m_currentState.onLeave()        
        self.m_currentState = newState
        if self.m_currentState:
            self.m_currentState.onEnter()
    
    def addState(self, stateName, state):
        self.m_stateDict[stateName] = state
        
    def addStateTransition(self, fromStateName, toStateName):
        if self.m_stateTransitions.has_key(fromStateName):
            self.m_stateTransitions[fromStateName].append(toStateName)
        else:
            self.m_stateTransitions[fromStateName] = [toStateName]
            

class Slukket(State):
    """Slukket tilstand"""
    def handleRequest(self, params):
        pass # Do something
        
    def onEnter(self):
        print "Slukket.onEnter kaldt"
        
    def onLeave(self):
        print "Slukket.onLeave kaldt"
        
    def __str__(self):
        return "Kontakten er slukket"
        
class Taendt(State):
    """Taendt tilstand"""
    def handleRequest(self, params):
        pass # Do something
        
    def onEnter(self):
        print "Taendt.onEnter kaldt"

    def onLeave(self):
        print "Taendt.onLeave kaldt"

    def __str__(self):
        return "Kontakten er taendt"

class Stikkontakt(StateMachine):
    def request(self, params):
        if self.m_currentState:
            self.m_currentState.handleRequest(params)
            # Do the actual state transition
            newStateName = self.m_stateTransitions[self.m_currentState.getStateName()][0]
            newState = self.m_stateDict[newStateName]
            self.switchToState(newState)
    

# Initialisering
maskine = Stikkontakt()
slukketTilstand = Slukket("Slukket")
taendtTilstand = Taendt("Taendt")
maskine.addState("Taendt", taendtTilstand)
maskine.addState("Slukket", slukketTilstand)
maskine.addStateTransition("Slukket", "Taendt")
maskine.addStateTransition("Taendt", "Slukket")
maskine.switchToState(slukketTilstand)

print maskine.m_currentState
for i in range(5):
    maskine.request(None)
    print maskine.m_currentState
