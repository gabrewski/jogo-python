# combat_interface.py
import curses
import time
from Entity.player import Player

def safe_addstr(win, y, x, text, max_width=None):
    """Adiciona texto de forma segura na janela com verificação de limites"""
    if max_width is None:
        max_width = win.getmaxyx()[1] - x - 1
    try:
        win.addstr(y, x, text[:max_width])
    except curses.error:
        pass

def combat(stdscr, player, enemy):
    # Configurações iniciais do curses
    curses.curs_set(0)  # Esconde o cursor
    stdscr.clear()
    stdscr.refresh()
    
    # Cria a janela principal
    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)    # Habilita teclas especiais
    win.nodelay(False)  # Entrada bloqueante
    win.leaveok(False)  # Mantém a posição do cursor

    # Posições fixas para as mensagens
    ACAO_LINHA = 8
    RESULTADO_LINHA = 10
    INIMIGO_ACAO_LINHA = 9
    INIMIGO_RESULTADO_LINHA = 11
    FIM_BATALHA_LINHA = 13

    def limpar_linhas():
        """Limpa as linhas de mensagens de ação"""
        for linha in [ACAO_LINHA, RESULTADO_LINHA, INIMIGO_ACAO_LINHA, INIMIGO_RESULTADO_LINHA]:
            try:
                win.move(linha, 0)
                win.clrtoeol()
            except curses.error:
                pass

    while True:
        # Obtém o tamanho atual do terminal
        height, width = stdscr.getmaxyx()
        
        # Desenha a interface básica
        win.erase()
        safe_addstr(win, 0, 0, f"Jogador: {player.name} | HP: {player.hp}/{player.hp_max}")
        safe_addstr(win, 0, width-30, f"Inimigo: {enemy.name} | HP: {enemy.hp}/{enemy.hp_max}")
        
        # Desenha o menu de opções
        opcoes = [
            "O que deseja fazer?",
            "1. Atacar",
            "2. Defender",
            "3. Curar",
            "4. Fugir"
        ]
        for i, texto in enumerate(opcoes):
            safe_addstr(win, 2+i, 0, texto)

        win.refresh()

        # Obtém a entrada do jogador
        while True:
            try:
                tecla = win.getch()
                if tecla in [ord('1'), ord('2'), ord('3'), ord('4')]:
                    break
            except:
                tecla = -1
        
        limpar_linhas()
        
        # Lida com a ação do jogador
        if tecla == ord('1'):  # Atacar
            safe_addstr(win, ACAO_LINHA, 0, f"{player.name} atacou!")
            dano_ataque, critico = player.attack(enemy)
            if critico:
                safe_addstr(win, RESULTADO_LINHA, 0, f"Ataque crítico! {dano_ataque} de dano!")
            else:
                safe_addstr(win, RESULTADO_LINHA, 0, f"Causou {dano_ataque} de dano!")

        elif tecla == ord('2'):  # Defender
            safe_addstr(win, ACAO_LINHA, 0, f"{player.name} defendeu!")
            dano_defesa, defendeu = player.defend(enemy)
            if defendeu:
                safe_addstr(win, RESULTADO_LINHA, 0, f"Defendeu o ataque! Levou {dano_defesa} de dano.")
            else:
                safe_addstr(win, RESULTADO_LINHA, 0, f"Não conseguiu defender! Levou {dano_defesa} de dano.")

        elif tecla == ord('3'):  # Curar
            pocoes = player.inventory.get_consumables()
            if pocoes:
            # Limpa e mostra a lista de poções
                limpar_linhas()
                safe_addstr(win, ACAO_LINHA, 0, "Escolha uma poção:")
                for i, poco in enumerate(pocoes):
                    safe_addstr(win, ACAO_LINHA+i+1, 0, f"{i+1}. {poco.name} ({poco.quantity})")
                win.refresh()

        # Loop de seleção corrigido
                while True:
                    try:
                        key = win.getch()
                # Tecla ESC (27) para cancelar
                        if key == 27:
                            limpar_linhas()
                            safe_addstr(win, RESULTADO_LINHA, 0, "Seleção cancelada!")
                            break
                
                # Converter para número
                        escolha = key - ord('1')
                        if 0 <= escolha < len(pocoes):
                            selecionada = pocoes[escolha]
                            if selecionada.quantity > 0:
                                # Aplica cura
                                cura = selecionada.healing_points
                                player.hp = min(player.hp + cura, player.hp_max)
                                selecionada.quantity -= 1

                                # Atualiza interface
                                limpar_linhas()
                                safe_addstr(win, RESULTADO_LINHA, 0, f"Recuperou {cura} HP!")
                                win.refresh()

                                # Remove se acabou
                                if selecionada.quantity <= 0:
                                    player.inventory.remove(selecionada)
                                break
                            else:
                                safe_addstr(win, RESULTADO_LINHA, 0, "Poção esgotada!")
                        else:
                            safe_addstr(win, RESULTADO_LINHA, 0, "Opção inválida!")
                
                        win.refresh()
                    except:
                        pass
                break  # Sai do loop de seleção de poção
            else:
                safe_addstr(win, RESULTADO_LINHA, 0, "Não há poções disponíveis!")

        elif tecla == ord('4'):  # Fugir
            if player.flee():
                safe_addstr(win, ACAO_LINHA, 0, "Fugiu com sucesso!")
                win.refresh()
                time.sleep(1)
                break
            else:
                safe_addstr(win, RESULTADO_LINHA, 0, "Fuga malsucedida!")

        win.refresh()
        time.sleep(1)

        # Turno do inimigo
        if enemy.hp > 0:
            safe_addstr(win, INIMIGO_ACAO_LINHA, 0, f"{enemy.name} está atacando!")
            dano_ataque, critico = enemy.attack(player)
            if critico:
                safe_addstr(win, INIMIGO_RESULTADO_LINHA, 0, f"Ataque crítico! Levou {dano_ataque} de dano!")
            else:
                safe_addstr(win, INIMIGO_RESULTADO_LINHA, 0, f"Levou {dano_ataque} de dano!")
            win.refresh()
            time.sleep(1)

        # Verifica condições de fim de batalha
        if enemy.hp <= 0:
            safe_addstr(win, FIM_BATALHA_LINHA, 0, f"Vitória! {enemy.name} foi derrotado!")
            break
        elif player.hp <= 0:
            safe_addstr(win, FIM_BATALHA_LINHA, 0, f"Derrota! {player.name} foi derrotado!")
            break

    # Mensagem final da batalha
    win.erase()
    safe_addstr(win, height//2, (width-20)//2, "A batalha terminou!")
    win.refresh()
    time.sleep(2)

def start_combat(player, enemy):
    curses.wrapper(combat, player, enemy)