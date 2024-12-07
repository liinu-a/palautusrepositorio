from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan, Not, Or

class QueryBuilder:
    def __init__(self, query = None):
        if query is None:
            query = [All()]
        self.query = query

    def plays_in(self, team):
        return QueryBuilder(self.query + [(PlaysIn(team))])

    def has_at_least(self, value, attr):
        return QueryBuilder(self.query + [HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(self.query + [HasFewerThan(value, attr)])

    def negation(self, cond):
        return QueryBuilder(self.query + [Not(cond)])

    def one_of(self, *conditions):
        return QueryBuilder(self.query + [Or(*conditions)])

    def build(self):
        return And(*self.query)
    