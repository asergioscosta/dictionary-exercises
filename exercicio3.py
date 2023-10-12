meuset = {1, 2, 3, 4, 1}
meuset2 = set([1, 2, 8, 9, 10])

uniao = meuset.union(meuset2)
print("A união é: ", uniao)

intersecao = meuset.intersection(meuset2)
print ("A interseção é: ", intersecao)

diferenca = meuset.difference(meuset2)
print ("A diferença é: ", diferenca)

diferenca_simetrica = meuset.symmetric_difference(meuset2)
print ("A diferença simétrica é: ", diferenca_simetrica)