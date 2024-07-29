import requests
from bs4 import BeautifulSoup

def adquirir_infos_da_pagina(ano: str | int):
    if type(ano) == int:
        ano = str(ano)
    todos_pontos = []
    todos_clubes = []
    todas_vitorias = []
    todos_empates = []
    todas_derrotas = []
    todos_gols_feitos = []
    todos_gols_sofridos = []
    todos_saldos_de_gols = []
    todos_cartoes_amarelos = []
    todos_cartoes_vermelhos = []
    todos_os_aproveitamentos = []

    listas_a_usar = [todas_vitorias, todos_empates, todas_derrotas, todos_gols_feitos, todos_gols_sofridos, todos_saldos_de_gols, todos_cartoes_amarelos, todos_cartoes_vermelhos, todos_os_aproveitamentos]

    url = f"https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/{ano}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.find('tbody')

        if tbody:
            if int(ano) < 2018:
                classe_tr = ""
            else:
                classe_tr = "expand-trigger"
            for tr in tbody.find_all('tr', class_=classe_tr):
                if len(tr.find_all('th')) == 1:
                    for th in tr.find_all('th'):
                        time_pontos = int(th.text.strip())
                        todos_pontos.append(time_pontos)

                todos_tds = tr.find_all('td')

                if len(todos_tds) > 2:
                    idx = 2
                    for secao in listas_a_usar:
                        dado = int(todos_tds[idx].text.strip())
                        secao.append(dado)
                        idx += 1
                    
                    td_com_nome_do_time = todos_tds[0]
                    for span in td_com_nome_do_time.find_all('span', class_='hidden-xs'):
                        nome_time = span.text.strip()
                        todos_clubes.append(nome_time)

        else:
            raise ConnectionError(f"O tbody no ano {ano} não foi encontrado.")
    else:
        raise ConnectionError(f"Erro ao acessar a página no ano {ano}: {response.status_code}")
    
    informacoes = {
        'Clubes': todos_clubes,
        'Pontos': todos_pontos,
        'Vitórias': todas_vitorias,
        'Empates': todos_empates,
        'Derrotas': todas_derrotas,
        'Gols Feitos': todos_gols_feitos,
        'Gols Sofridos': todos_gols_sofridos,
        'Saldos de Gols': todos_saldos_de_gols,
        'Cartões Amarelos': todos_cartoes_amarelos,
        'Cartões Vermelhos': todos_cartoes_vermelhos,
        'Aproveitamento': todos_os_aproveitamentos
    }
    return informacoes
