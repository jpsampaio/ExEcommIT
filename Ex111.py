from CeV.utilidadescev.moeda import resumo
                                       # Usam-se pontos para representar as barras no path.
                                       # Tive que especificar o DIRETÓRIO em que o pacote está! Sem isso, o programa não o reconhecia.
                            
q = float(input('Digite um valor:  R$'))
t = float(input('Digite a taxa (%): '))

resumo(q, t, True)