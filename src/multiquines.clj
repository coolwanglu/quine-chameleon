(let[S"DATA"L(vec(.split S"\t"))I(.indexOf L(first *command-line-args*))](print(str(get L(+ I 1))(clojure.string/escape S{\tab"\\t"\newline"\\n"\""\\\""\\"\\\\"})(get L(+ I 2)))))
