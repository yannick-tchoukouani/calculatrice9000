import re

def calculatrice():
    while True:
        # Demander à l'utilisateur d'entrer une expression
        expression = input("Entrez une expression mathématique (ou 'exit' pour quitter) : ")

        # Vérifier si l'utilisateur souhaite quitter
        if expression.lower() == 'exit':
            break

        try:
            # Analyser l'expression
            result = evaluer_expression(expression)

            # Afficher le résultat
            print(f"Résultat : {result}")

        except (ValueError, ZeroDivisionError, SyntaxError) as e:
            print(f"Erreur : {e}")
            continue

def evaluer_expression(expression):
    # Vérifier si l'expression contient des caractères non autorisés
    if not re.match(r'^[0-9+\-*/.() ]+$', expression):
        raise ValueError("Caractères non autorisés dans l'expression")

    # Appliquer les priorités opératoires en utilisant la récursivité
    for operation in ('*/', '+-'):
        pattern = r'(\d+\.?\d*)[{}](-?\d+\.?\d*)'.format(re.escape(operation))
        while re.search(pattern, expression):
            expression = re.sub(pattern, lambda match: str(evaluer_operation(match.group(0))), expression)

    return float(expression)

def evaluer_operation(operation):
    # Évaluer une opération entre deux nombres
    op_match = re.match(r'(\d+\.?\d*)([+\-*/])(-?\d+\.?\d*)', operation)
    if op_match:
        num1 = float(op_match.group(1))
        op = op_match.group(2)
        num2 = float(op_match.group(3))

        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division par zéro")
            return num1 / num2

    raise SyntaxError("Opération invalide")

# Exécuter la calculatrice
calculatrice()
