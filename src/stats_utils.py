import pandas as pd


def analyser_ventes(transactions):
    """Analyse une liste de montants de ventes (en euros) avec pandas."""

    # 1. Création du DataFrame
    df = pd.DataFrame({"montant": transactions})

    # 2. Nettoyage : valeurs négatives ou nulles -> NaN, puis suppression
    df["montant"] = df["montant"].where(df["montant"] > 0)
    df_propre = df.dropna()

    # Si aucune transaction valide, on évite les erreurs de calcul
    if df_propre.empty:
        return {"erreur": "Aucune transaction valide"}

    # 3. Calculs statistiques avec describe()
    stats = df_propre["montant"].describe()

    # 4. Anomalies : transactions > 2 x la moyenne
    seuil = 2 * stats["mean"]
    anomalies = df_propre[df_propre["montant"] > seuil]

    # 5. Format de sortie : un dictionnaire
    return {
        "nombre_transactions": int(stats["count"]),
        "somme_totale": float(df_propre["montant"].sum()),
        "moyenne": round(float(stats["mean"]), 2),
        "mediane": float(stats["50%"]),
        "ecart_type": round(float(stats["std"]), 2),
        "minimum": float(stats["min"]),
        "maximum": float(stats["max"]),
        "seuil_anomalie": float(seuil),
        "nombre_anomalies": len(anomalies),
        "anomalies": anomalies["montant"].tolist(),
    }


    # bloc test
    donnees_test = [150, 200, 175, -50, 0, 3200, 220, 180, 195, 160]

    resultats = analyser_ventes(donnees_test)

    print("=== ANALYSE VENTES ===")
    for cle, valeur in resultats.items():
        print(f"{cle} : {valeur}")