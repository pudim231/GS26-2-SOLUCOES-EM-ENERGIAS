class CitizenEnergyAdvisor:
    """
    Módulo de análise energética e recomendações sustentáveis
    para integração ao Citizen Assist AI.
    """

    def __init__(self, tarifa_kwh: float = 0.85):
        self.tarifa_kwh = tarifa_kwh
        # Fator médio de emissão SIN (MCTI) em kg CO2 / kWh
        self.fator_co2 = 0.0385

    def calcular_cenario(
        self,
        moradores: int,
        minutos_banho: int,
        potencia_watts: int,
        tipo_imovel: str,  # "casa_propria" ou "apartamento_alugado"
    ) -> dict:
        # 1. Cálculo do Cenário Atual (30 dias)
        horas_dia = (moradores * minutos_banho) / 60.0
        potencia_kw = potencia_watts / 1000.0
        kwh_mes = round(potencia_kw * horas_dia * 30, 2)
        custo_mes = round(kwh_mes * self.tarifa_kwh, 2)
        custo_ano = round(custo_mes * 12, 2)
        co2_ano = round(kwh_mes * 12 * self.fator_co2, 2)

        # 2. Alternativa A: Eficiência Energética (Chuveiro Eletrônico 3500W)
        potencia_eficiente_kw = 3.5
        kwh_mes_alt_a = round(potencia_eficiente_kw * horas_dia * 30, 2)
        economia_mes_a = round((kwh_mes - kwh_mes_alt_a) * self.tarifa_kwh, 2)
        investimento_a = 220.00
        payback_meses_a = round(investimento_a / economia_mes_a, 1) if economia_mes_a > 0 else 0

        # 3. Alternativa B: Renovável (Solar Fotovoltaica On-Grid)
        # Custo estimado proporcional ao kWh/mês (~R$ 44 por kWh/mês instalado)
        investimento_b = round(kwh_mes * 44.0, 2)
        # Desconta ~R$ 15/mês referente à taxa mínima / Fio B
        economia_mes_b = round(max(custo_mes - 15.0, 0), 2)
        payback_anos_b = round((investimento_b / (economia_mes_b * 12)), 1) if economia_mes_b > 0 else 0

        # 4. Lógica de Recomendação Contextualizada
        if tipo_imovel == "apartamento_alugado" or potencia_watts <= 3500:
            recomendacao = (
                "Alternativa A (Eficiência Energética - Chuveiro Eletrônico 3.500W): "
                "Ideal para seu perfil por não exigir obras no telhado, ter baixo custo inicial "
                f"(~R$ {investimento_a:.2f}) e se pagar em aproximadamente {payback_meses_a} meses."
            )
        else:
            recomendacao = (
                "Alternativa B (Energia Solar Fotovoltaica) como solução definitiva, ou "
                "Alternativa A (Chuveiro Eletrônico) como passo imediato. Como você reside em casa própria, "
                f"a energia solar zera praticamente todo o custo do banho (economia de ~R$ {economia_mes_b:.2f}/mês) "
                f"e evita {co2_ano} kg de CO2/ano, com retorno estimado em {payback_anos_b} anos."
            )

        return {
            "diagnostico_atual": {
                "consumo_kwh_mes": kwh_mes,
                "custo_mensal_rs": custo_mes,
                "custo_anual_rs": custo_ano,
                "emissao_co2_anual_kg": co2_ano,
            },
            "alternativa_eficiencia": {
                "nome": "Chuveiro Eletrônico 3.500W",
                "novo_consumo_kwh_mes": kwh_mes_alt_a,
                "economia_mensal_rs": economia_mes_a,
                "investimento_rs": investimento_a,
                "payback_meses": payback_meses_a,
            },
            "alternativa_renovavel": {
                "nome": "Sistema Solar Fotovoltaico On-Grid",
                "economia_mensal_rs": economia_mes_b,
                "investimento_estimado_rs": investimento_b,
                "payback_anos": payback_anos_b,
                "co2_evitado_anual_kg": co2_ano,
            },
            "recomendacao_principal": recomendacao,
            "aviso_limitacoes": (
                "ESTIMATIVA: Cálculos baseados em tarifa média de R$ 0,85/kWh (ANEEL) e "
                "fator de emissão SIN de 0,0385 kg CO2/kWh (MCTI). Resultados reais variam "
                "conforme irradiação solar local, bandeira tarifária e hábitos de uso."
            ),
        }


# Exemplo de execução e saída integrada ao assistente
if __name__ == "__main__":
    advisor = CitizenEnergyAdvisor()
    resultado = advisor.calcular_cenario(
        moradores=4,
        minutos_banho=12,
        potencia_watts=5500,
        tipo_imovel="casa_propria",
    )
    import json
    print(json.dumps(resultado, indent=2, ensure_ascii=False))