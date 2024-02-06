from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight or a knave but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is a knight his sentence is true:
    Implication(AKnight, And(AKnave, AKnight)),
    # If A is a knave his sentence is false:
    Implication(AKnave, Not(And(AKnave, AKnight))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are knights or a knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a knight, then A and B are both knaves:
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, his statement is false:
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are knights or knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a knight, A and B are both the same:
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave, his statement is false:
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight, A and B are not the same:
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave, his statement is false:
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B and C are knights or a knaves but not both:
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If C is a knight, A is a knight:
    Implication(CKnight, AKnight),
    # If C is a knave, A is a knave:
    Implication(CKnave, AKnave),
    # If B is a knight, C is a knave, and A said 'I am a knave':
    Implication(BKnight, CKnave),
    Implication(
        BKnight,
        And(
            Implication(AKnight, AKnave),
            Implication(AKnave, Not(AKnave)),
        ),
    ),
    # If B is a knave, C is a knight, and A said 'I am a knight':
    Implication(BKnave, CKnight),
    Implication(
        BKnave, And(Implication(AKnight, AKnight), Implication(AKnave, Not(AKnight)))
    ),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
