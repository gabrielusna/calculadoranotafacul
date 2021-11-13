aprovados = []
reprovados = []

while True:
  aluno = str(input("Qual é seu nome ?: "))
  while True: 
    ativ1 = float(input("NOTA [0,1] Atividade Online Pontuada 1: "))
    if ativ1  < 0.0 or ativ1 > 1.0:
      print("Nota Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    ativ2 = float(input("NOTA [0,2] Atividade Online Pontuada 2: "))
    if ativ2  < 0.0 or ativ2 > 2.0:
      print("Nota Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    ativ3 = float(input("NOTA [0,1] Atividade Online Pontuada 3: "))
    if ativ3  < 0.0 or ativ3 > 1.0:
      print("Nota Incorreta, Tente Novamente!")
    else: 
      break

  while True:
    provaregular = float(input("NOTA [0,6] Prova Regular: "))
    if provaregular  < 0.0 or provaregular > 6.0:
      print("Nota Incorreta, Tente Novamente!")
    else: 
      break
  media = (ativ1 + ativ2 + ativ3 + provaregular) 
  if (media >=7):
    print(f"O aluno {aluno} foi APROVADO com {media} pontos")
    aprovados.append(aluno)
  if (media <=6):
    print(f"O aluno {aluno} ficou com {media} pontos, e não atingiu a média!, Agora precisa fazer a recuperação!") 
    recuperacao = float(input("Nota recuperação: "))
    if recuperacao >= 5.0:
      print(f"O aluno {aluno} ficou com {recuperacao} pontos na recuperação, e foi APROVADO!") 
      aprovados.append(aluno)
    else:
      print(f"O aluno {aluno} ficou com {recuperacao} pontos na recuperação, e foi REPROVADO!")
      reprovados.append(aluno)

      print("-" * 48)
  while True:
   continuar = str(input("Gostaria de calcular mais uma nota? [s/n] "))
   if continuar == "s":                                                              
      break
   elif continuar == "n":
      break
  if continuar == "n":
     break
print("-" * 48)

total_alunos = len(aprovados) + len(reprovados)
aprovados_pcento = (100 / total_alunos) * len(aprovados)
reprovados_pcento = (100 / total_alunos) * len(reprovados)

print("{:.2f}% alunos foram APROVADOS e {:.2f}% ficaram REPROVADOS".format(aprovados_pcento, reprovados_pcento))
 
