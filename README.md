# Compresseurs

Implémentations et explorations de certains algorithmes de compression. Implémentation naïves ne servant que d'exercices, à ne pas utiliser dans un projet sérieux.

Liste des algorithmes implémentés:

1. [Lempel-Ziv-Welch](/zip-comp)

L'[algorithme de Lempel-Ziv-Welch](https://fr.wikipedia.org/wiki/Lempel-Ziv-Welch) est un algorithme de compression de données sans perte. L'algorithme de compression est le suivant :

``` algorithm
FONCTION LZW_Compresser(Texte, dictionnaire)

    w ← ""

    TANT QUE (il reste des caractères à lire dans Texte) FAIRE
       c ← Lire(Texte)
       p ← Concaténer(w, c)
       SI Existe(p, dictionnaire) ALORS
          w ← p
       SINON
          Ajouter(p, dictionnaire)
          Écrire dictionnaire[w]
          w ← c
    FIN TANT QUE
```

Tandis que celui de décompression est :

``` algorithm
FONCTION LZW_Décompresser(Code, dictionnaire)

     n ← |Code|
     v ← Lire(Code)
     Écrire dictionnaire[v]
     w ← chr(v)

     POUR i ALLANT DE 2 à n FAIRE
        v ← Lire(Code)
        SI Existe(v, dictionnaire) ALORS
          entrée ← dictionnaire[v]
        SINON entrée ← Concaténer(w, w[0])
        Écrire entrée
        Ajouter(Concaténer(w,entrée[0]), dictionnaire)
        w ← entrée
     FIN POUR
```
