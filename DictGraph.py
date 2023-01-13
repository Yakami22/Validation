from Relation import TransitionRelation


class DictGraph(TransitionRelation):


    def __init__(self, roots: dict):
        '''
        Initialize the Dict with a dictionary

        This method should preferably not be used because there's an updated version of it
        :param roots: a graph on entry
        '''
        self.graph = roots

    def __init__(self, roots: dict, entry : list):
        '''
        Initialize the Dict with a dictionary and entry point

        :param roots: a dict to use
        :param entry: a list of entry point
        '''
        self.graph = roots
        self.entry = entry

    def getRoots(self):
        return self.entry

    def next(self, source):
        try:
            return self.graph[source]
        except KeyError:
            return []

