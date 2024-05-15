{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPkS7/kJ8biMb5jqVc4iDJM"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["###**BOLETIM**"],"metadata":{"id":"LDQn3iPLNfU9"}},{"cell_type":"markdown","source":["* <code>len</code> (lenght) = *tamanho*\n","* [] = matriz/array\n","* {} = dicionário"],"metadata":{"id":"KqqsHZlCPzIK"}},{"cell_type":"markdown","source":["<b> trocando o 'for i in range(2) para range(4)', ele repete para 4 notas pra cada disciplina </b>"],"metadata":{"id":"6jLjpJr-ZMCI"}},{"cell_type":"code","execution_count":null,"metadata":{"id":"RdiD2KtONVVb"},"outputs":[],"source":["# Função para calcular a média das notas\n","# len (lenght) = tamanho\n","# [] = matriz/array\n","\n","def calcular_media(notas):\n","    soma = sum(notas)\n","    quantidade = len(notas) # conta a quantidade de notas\n","    return soma / quantidade\n","\n","# Lista de disciplinas\n","\n","disciplinas = [\"Fundamentos de Banco de Dados\", \"Programação de Computadores\"]\n","\n","# Dicionário para armazenar as notas de cada disciplina\n","\n","notas_por_disciplina = {}\n","\n","# Solicitar e armazenar as notas de cada disciplina\n","\n","for disciplina in disciplinas:\n","    notas_disciplina = []\n","\n","    for i in range(4):  # Limitado a quatro notas por disciplina.\n","        nota = float(input(f\"Digite a nota {i+1} de {disciplina}: \"))\n","        notas_disciplina.append(nota)\n","    notas_por_disciplina[disciplina] = notas_disciplina\n","\n","# Calcular a média geral e médias por disciplina.\n","\n","medias_por_disciplina = {disciplina: calcular_media(notas) for disciplina, notas in notas_por_disciplina.items()}\n","media_geral = calcular_media(list(medias_por_disciplina.values()))\n","\n","# Imprimir o boletim escolar\n","\n","print(\"\\n BOLETIM ESCOLAR\")\n","print(\"===============================================================================\")\n","print(\"{:<30} {:<10} {:<10} {:<10} {:<10} {:<10}\".format(\"Disciplina\", \"Nota 1\", \"Nota 2\", \"Nota 3\", \"Nota 4\", \"Média\"))\n","print(\"-------------------------------------------------------------------------------\")\n","for disciplina, notas in notas_por_disciplina.items():\n","    print(\"{:<30} {:<10} {:<10} {:<10} {:<10} {:<10.2f}\".format(disciplina, notas[0], notas[1], notas[2], notas[3], medias_por_disciplina[disciplina]))\n","print(\"----------------------------------------------------------------------------------\")\n","print(\"{:<30} {:<10.2f}\".format(\"Média Geral\", media_geral))\n","print(\"====================================================================================\")"]}]}