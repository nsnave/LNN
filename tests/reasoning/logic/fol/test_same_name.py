from lnn import (Predicate, Variable, And, Not, Or, Bidirectional,
                 Exists, Implies, ForAll, Model, Fact, World, Proposition,
                 Equals)


model = Model(theories=['equality'])

dog = model.add_predicates(1, "dog")


# Our premises:
#   States that "Aggie" is a dog
#   and that "Aggie" is the same as "Fruton"
#   (i.e., "Aggie" and "Fruton" refer to the same object)
model.add_facts({
  dog.name: {
    'Aggie': Fact.TRUE
  },
  'equals': {
    ('Aggie', 'Fruton'): Fact.TRUE
  }
})


# The theorem we want to prove:
#   that "Fruton" is a dog
#
# We want to prove that the query Dog("Fruton")
# follows from our axioms and premises. To do so,
# we check to see if the negation of our query
# invokes a contradiction. Thus, we assume that
# the negated query is true.
model["query"] = Not(Equals('Fruton', 'Aggie'), world=World.AXIOM)

model.infer()

model.print()
print(model['query'].state())