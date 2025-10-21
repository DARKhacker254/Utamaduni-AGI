from hyperon import MeTTa

metta = MeTTa()

def init_rules():
    metta.run('(:= (interpret (proverb patience)) (lesson "Patience leads to blessing"))')
    metta.run('(:= (interpret (proverb wisdom)) (lesson "Wisdom guides life"))')

def run_rule(intent, concept):
    try:
        result = metta.run(f"(interpret ({intent} {concept}))")
        return result if result else "No direct rule found."
    except Exception as e:
        return str(e)

init_rules()
