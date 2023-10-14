""" Implémentation naïve de l'algorithme LZW """

import sys

def main():
    if len(sys.argv) < 2:
        print("[ERREUR] No file argument were provided. Usage: \n\tnaivezip.py <file-to-compress>\n")
    else:
        filename = sys.argv[1]
        with open(filename) as f: contenu = f.read()
        compressed = lzw_compress(contenu)
        print(compressed)


def lzw_compress(content: str) -> list[bytes]:
    print("w\t c\t wc\t sortie\t dictionnaire ")
    w = ""
    # records = list()
    dico = dict()  # {c : str(ord(c)) for c in content}
    init = 254
    for c in content:
        p = w + c
        if p in dico.keys():
            w = p
        else:
            init += 1
            dico[p] = f"<{init}>" # "".join([str(ord(l)) for l in p])
            print(w, "\t", c, "\t", p, "\t", dico.get(w, w), "\t", p + "=" + dico[p])
            w = c
    # print(dico)

if __name__ == '__main__':
    main()