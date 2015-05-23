(let[S"DATA"L(vec(.split S"\t"))I(.indexOf L(first *command-line-args*))](print(str(get L(+ I 1))(.replace(.replace(.replace(.replace S"\\""\\\\")"\t""\\t")"\n""\\n")"\"""\\\"")(get L(+ I 2)))))
