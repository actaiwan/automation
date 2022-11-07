class Container(object):
    def __init__(self, id_, message):
        self.id = id_
        self.message = message

class Principle(Container):
    def __init__(self, id_, message, guidelines):
        Container.__init__(self, id_, message)
        self.guidelines = guidelines

class Guideline(Container):
    def __init__(self, id_, message, criterias):
        Container.__init__(self, id_, message)
        self.criterias = criterias

class Criteria(Container):
    def __init__(self, id_, message, inspections, evaluations):
        Container.__init__(self, id_, message)
        self.inspections = inspections
        self.evaluations = evaluations

class Code(Container):
    def __init__(self, id_, message, rule, example):
        Container.__init__(self, id_, message)
        self.rule = rule
        self.example = example

class InspectionCode(Code):
    pass
class EvaluationCode(Code):
    pass
