


from Arvore import Arvore

raiz = Arvore(25)

raiz.add_no(15)
raiz.add_no(50)
raiz.add_no(20)
raiz.add_no(10)
raiz.add_no(55)
raiz.add_no(45)
raiz.add_no(60)
raiz.add_no(5)

print(
   """
                    {}
               {}         {}
            {}     {}   {}     {}
        {}                           {}
    """
    .format(raiz.valor,
    raiz.no_esq.valor, raiz.no_dir.valor,
    raiz.no_esq.no_esq.valor, raiz.no_esq.no_dir.valor,
    raiz.no_dir.no_esq.valor, raiz.no_dir.no_dir.valor,
    raiz.no_esq.no_esq.no_esq.valor, raiz.no_dir.no_dir.no_dir.valor
    )
    )

print(raiz.count())
print((raiz.level()))