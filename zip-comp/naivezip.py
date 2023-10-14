""" Implémentation naïve de l'algorithme LZW """

import sys

table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def main():
    if len(sys.argv) < 2:
        print("[ERREUR] No file argument were provided. Usage: \n\tnaivezip.py <file-to-compress>\n")
    else:
        filename = sys.argv[1]
        with open(filename) as f: contenu = f.read()
        compressed = lzw_compress(contenu)
        print("Compressed message :", compressed)
        

# TODO: Améliorer code pour comptabiliser dernière valeur de w
def lzw_compress(content: str) -> bytearray:
    print("w\t c\t wc\t sortie\t dictionnaire ")
    w = ""
    compressed_message = ""
    dico = dict()  # {c : str(ord(c)) for c in content}
    init = 255

    for c in content:
        p = w + c
        if p in dico.keys() or p in table:
            print(w, "\t", c, "\t", p, "\t", " ", "\t", " ")
            w = p
        else:
            init += 1
            dico[p] = f"<{init}>" # "".join([str(ord(l)) for l in p])
            print(w, "\t", c, "\t", p, "\t", dico.get(w, w), "\t", p + "=" + dico[p])
            compressed_message +=  dico.get(w, w)
            w = c

    if w in dico.keys() or w in table:
            print(w, "\t", " ", "\t", " ", "\t", dico.get(w, w), "\t"," ")
            compressed_message +=  dico.get(w, w)
    else:
        init += 1
        dico[w] = f"<{init}>" # "".join([str(ord(l)) for l in p])
        print(w, "\t", " ", "\t", " ", "\t", dico.get(w, w), "\t", w + "=" + dico[w])
        compressed_message +=  dico.get(w, w)

    return compressed_message


if __name__ == '__main__':
    main()