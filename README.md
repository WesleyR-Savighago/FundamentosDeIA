# FundamentosDeIA

Este repositório documenta as atividades práticas realizadas durante o curso Fundamentos de IA: explorando a estrutura e abordagens de sistemas inteligentes. Aqui, estão incluídos conceitos, códigos e experimentos feitos ao longo do aprendizado.

# Atividade de Recomendação

Construir o sistema de recomendação utilizando o algoritmo A\* com as seguintes etapas:

1 - Definir os produtos:

Cada produto possui um nome, categoria e probabilidade de conversão.
Crie uma classe Produto para representar esses atributos.

2 - Criar o sistema de recomendação:

Desenvolva uma classe AStarRecommendation que implementa:
Um grafo simplificado onde cada produto se conecta a todos os outros.
O algoritmo A\* para calcular o melhor caminho entre dois produtos.
3 - Implementar a heurística:

Crie uma função de heurística baseada na probabilidade de conversão do produto (quanto maior, melhor).
4 - Testar o sistema:

Insira exemplos de produtos.
Use o sistema para encontrar o melhor caminho entre dois produtos.

# Atividade de Previsão do tempo

Implementar o modelo de previsão de clima

# Atividade de Sistema especialista

1 - Definir a base de conhecimento:

Crie uma estrutura para armazenar:
Fatos: Informações fornecidas pelo paciente (ex.: febre alta, tosse, dificuldade para respirar).
Regras: Relações entre os fatos que indicam possíveis diagnósticos (ex.: "Se febre alta e tosse, então infecção respiratória").
Implemente a base de conhecimento como uma classe chamada BaseDeConhecimento que gerencie os fatos e as regras.

2 - Desenvolver o mecanismo de inferência:

Implemente uma classe chamada SistemaEspecialista que:
Receba a base de conhecimento.
Utilize lógica proposicional para inferir conclusões com base nos fatos e regras fornecidos.
Use uma abordagem que permita aplicar as regras sequencialmente até chegar a um diagnóstico.
3 - Implementar os diagnósticos:

Insira exemplos de fatos (sintomas relatados por um paciente).
Use as regras da base de conhecimento para deduzir diagnósticos, explicando o raciocínio seguido.
4 - Testar o sistema
