import statistics


def analyser_ventes(transactions):
    # Nettoyage : garder uniquement les valeurs strictement positives
    ventes_valides = [montant for montant in transactions if montant > 0]

    # Vérification : aucune transaction valide
    if not ventes_valides:
        return {
            "nombre_transactions": 0,
            "somme_totale": 0,
            "moyenne": 0,
            "mediane": 0,
            "ecart_type": 0,
            "maximum": 0,
            "minimum": 0,
            "outliers": []
        }

    # Calculs statistiques
    nombre_transactions = len(ventes_valides)
    somme_totale = sum(ventes_valides)
    moyenne = somme_totale / nombre_transactions
    mediane = statistics.median(ventes_valides)
    ecart_type = statistics.stdev(ventes_valides) if nombre_transactions > 1 else 0
    maximum = max(ventes_valides)
    minimum = min(ventes_valides)

    # Détection des outliers
    outliers = [montant for montant in ventes_valides if montant > 2 * moyenne]

    return {
        "nombre_transactions": nombre_transactions,
        "somme_totale": somme_totale,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "maximum": maximum,
        "minimum": minimum,
        "outliers": outliers
    }