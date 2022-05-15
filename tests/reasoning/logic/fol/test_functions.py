from numpy import equal
from lnn import (Predicate, Variable, And, Not, Or, Bidirectional,
                 Exists, Implies, ForAll, Model, Fact, World, Proposition,
                 Equals, Function)


model = Model(theories=['functions'])

color = model.add_functions(1, "color")

# Our premises:
#   the color of the ocean is blue
#   the color of the sky is blue
#
#   color('ocean') maps to 'blue'
#   color('sky') maps to 'blue'
#
#   color('ocean', 'blue') is True
#   color('sky', 'blue') is True
#
#   Exists(x)(color('ocean', x) and x = 'blue')
#   Exists(x)(color('sky', x) and x = 'blue')
#
model.add_facts({
  color.name: {
    ('ocean', 'blue'): Fact.TRUE,
    ('sky', 'blue'): Fact.TRUE
  },
  'equals': {
    # For some reason, the LNN module gets mad without an entry
    ('foo', 'foo'): Fact.TRUE 
  }
})


# The theorem we want to prove:
#   the ocean and the sky are the same color
#
#   color('ocean') = color('sky')
#
#   Exists(x)(color('ocean', x) and x = color('sky'))
#   Exists(x, y)( color('ocean', x) and color('sky', y) and x = y)
#
#   Technically, we could replace "Exists" with "Forall"
#   and the "and x=y" with "implies x=y" since `color`
#   is functional.
#
x = Variable('x')
model["query"] = Not(Equals(color('ocean'), color('sky'), world=World.AXIOM), world=World.AXIOM)
model["query"].print()

model.print()

model.infer()

model.print()
print(model['query'].state())
