from hyperon import MeTTa, SpaceAtom

def initialize_metta():
    metta = MeTTa()
    metta.run("(import std)")
    return metta

def insert_proverb(metta, proverb):
    expr = f'(Proverb "{proverb.text}" "{proverb.meaning}" "{proverb.culture}")'
    metta.run(expr)
