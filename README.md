# GS26-2-SOLUCOES-EM-ENERGIAS

Módulo de Eficiência Energética e Renováveis
Integrante:
Rubens Henrique Cordeiro dos Santos
RM:572667

# 1.1. Definição do Contexto e Público-Alvo
Público-alvo: Famílias residentes em áreas urbanas (apartamentos ou casas populares/classe média) no Brasil, especificamente na região Sudeste (referência: Grande São Paulo).

Necessidade energética: Redução do custo da fatura de energia elétrica sem perda de conforto térmico, atacando o principal vilão do consumo residencial brasileiro: o chuveiro elétrico.

Contribuição do Assistente: O Citizen Assist AI atua como um consultor acessível que diagnostica o gasto atual do usuário com base em hábitos simples (tempo de banho e potência) e recomenda alternativas viáveis (eficiência energética vs. energia solar), traduzindo conceitos técnicos (kW, kWh, payback, emissões de 
CO 
2
​
 ) em linguagem clara e transparente.

# 1.2. Análise de Consumo (Premissas e Dados)
Para garantir rigor técnico, utilizamos uma residência padrão de 4 pessoas como linha de base (baseline) para um período de 1 mês (30 dias) e 1 ano (12 meses).

Equipamento Base: Chuveiro elétrico convencional de 5.500 W (
5,5 kW) na posição "Inverno" (potência nominal comum segundo dados do PROCEL/INMETRO).

Hábito de Uso (Estimado): 4 banhos diários de 12 minutos cada (
0,2 horas por banho) = 
0,8 horas/dia (
24 horas/m 
e
ˆ
 s).

Tarifa de Energia (Dado Público de Referência): R$ 0,85 / kWh (valor médio estimado já considerando impostos ICMS/PIS/COFINS e bandeira verde/amarela para consumidores residenciais B1 no Sudeste, referência ANEEL).

Fator de Emissão do Sistema Interligado Nacional - SIN (Dado Público): 
0,0385 kg CO 
2
​
 /kWh (referência média anual MCTI - Ministério da Ciência, Tecnologia e Inovação).

Cálculo da Linha de Base (Situação Atual):
Energia Mensal (kWh)=Pot 
e
ˆ
 ncia (kW)×Tempo (h/dia)×30 dias
E 
atual
​
 =5,5 kW×0,8 h/dia×30=132 kWh/m 
e
ˆ
 s(ou 1.584 kWh/ano)
Custo Mensal Atual: 
132 kWh×R$ 0,85=R$ 112,20/m 
e
ˆ
 s (
R$ 1.346,40/ano)

Impacto Ambiental Atual: 
1.584 kWh/ano×0,0385 kg CO 
2
​
 =60,98 kg CO 
2
​
 /ano

# 1.3. Comparação de Alternativas (Mesmo Período e Necessidade)
Comparamos 3 cenários para atender à mesma demanda de 4 banhos diários de 12 minutos:

# Alternativa A (Eficiência Energética - Baixo Custo): Substituição por chuveiro híbrido/eletrônico com controle gradual de temperatura + redutor de vazão + redução da potência média de operação para 3.500 W (
3,5 kW).

# Alternativa B (Fonte Renovável - Energia Solar Fotovoltaica): Instalação de um microsistema fotovoltaico on-grid (ou assinatura de energia solar compartilhada/GD) dimensionado para compensar exatamente os 
132 kWh/m 
e
ˆ
 s do chuveiro (sistema de aproximadamente 
1,2 kWp).

# Alternativa C (Fonte Renovável - Aquecedor Solar Térmico): Sistema de coletor solar térmico com reservatório (boiler) de 200 litros e apoio elétrico apenas em dias nublados (reduz o consumo elétrico do banho em 75%, segundo dados do PROCEL/DASOL).

# 1.4. Justificativas, Referências e Limitações
Lógica de Recomendação do Assistente:

Se o usuário mora em apartamento ou imóvel alugado, ou tem orçamento restrito: o assistente recomenda a Alternativa A (retorno em menos de 6 meses, sem necessidade de obras).

Se o usuário mora em casa própria com telhado disponível e busca descarbonização máxima e economia de longo prazo: o assistente recomenda a Alternativa B (Fotovoltaica, pela facilidade de instalação elétrica sem quebra-quebra hidráulico e compensação integral).

# Limitações Explícitas (Exibidas nas respostas da IA):

Os valores são estimativas baseadas na tarifa média de R$ 0,85/kWh e não representam garantia de economia.

Sistemas solares dependem da irradiação solar local, orientação do telhado e ausência de sombreamento.

No sistema fotovoltaico on-grid, permanece a cobrança do custo de disponibilidade da rede (taxa mínima) e encargos da Lei 14.300 (Fio B).

# Referências Verificáveis:

PROCEL / INMETRO: Tabelas de Consumo e Eficiência Energética (Chuveiros Elétricos). Disponível em: gov.br/inmetro

ANEEL (Agência Nacional de Energia Elétrica): Ranking de Tarifas Residenciais (Grupo B1). Disponível em: gov.br/aneel

MCTI: Fatores de Emissão de 
CO 
2
​
  pela geração de energia elétrica no Sistema Interligado Nacional (SIN). Disponível em: gov.br/mcti

EPE (Empresa de Pesquisa Energética): Balanço Energético Nacional (BEN) e Atlas Brasileiro de Energia Solar. Disponível em: epe.gov.br
