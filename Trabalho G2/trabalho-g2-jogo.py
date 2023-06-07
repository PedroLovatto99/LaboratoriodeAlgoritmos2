import random

class NegativeValue(Exception):
    pass

class InvalidOption(Exception):
    pass

class ValueAbove(Exception):
    pass



def generate_cards():
    list_01 = random.sample(range(0, 8), 8)
    list_02 = random.sample(range(0, 8), 8)
    definite_board = []

    for i in range(0, 8):
        definite_board.append(list_01[i])
        definite_board.append(list_02[i])

    return definite_board



def show_board(board_cards_list, board_cards):
    for index, item in enumerate(board_cards_list):
        print(board_cards[item], end=(
            '\n' if (index + 1) % 4 == 0 else '\t'
        ))


def show_game(board_cards_list, board_cards, hits, user_position):
    for index, item in enumerate(board_cards_list):
        print(
            board_cards[item] if (item in hits or index in user_position ) else index,
            end=('\n' if (index + 1) % 4 == 0 else '\t')
        )




def score_lose(score):
    print("                          ")
    print(" Você errou! - Perdeu 50 pontos")
    score -= 50
    return score


def ranking_file(user_name, score):
    user_score_file = open("ranking.txt", "a")
    user_score_file.write(user_name + " ")
    user_score_file.write((str(f'{score} \n')))
    user_score_file.close()


def ranking():
    users_file = open("ranking.txt", "r")
    users_history = users_file.readlines()
    
    users_sorted = sorted(users_history, key=lambda user: int(user.split()[-1]), reverse=True)
    print("____________________________")
    print("                            ")
    print("          RANKING           ")
    print("____________________________")
    
    for i in users_sorted:
        
        print(f'{i.strip("")}')
        
    opt= int(input("⟳  Retornando ao menu digite 1:"))
    if opt == 1:
            main()
    else:
            exit()
        
    users_file.close()





def game_board():
    print("____________________________")
    print("                               ")
    user_name = input("Digite o seu nome: ")
    score = 1000
    board_cards = [ "🐵","🐺","🐶","🐱","🦁","😀","🤩","😴","😢","😡"]
    board_cards_list = generate_cards()
    hits = []
    
    
    print("____________________________")
    print("                            ")
    print("         TABULEIRO          ")
    print("____________________________")
    show_board(board_cards_list, board_cards)
    print("____________________________")

    try:
        print("                                    ")
        opt = int(input("Digite 1 para esconder as peças: "))
        print("____________________________")

        if opt == 1:
            
            

            while len(hits) != 8:
                print("____________________________")
                print("                            ")
                print("         TABULEIRO          ")
                print("____________________________")
                show_game(board_cards_list, board_cards, hits, user_position = [])
                print("____________________________")
                print("                            ")
                print("Jogador:", user_name)
                print("Seu score atual: ", score)
                print("____________________________")
                print("                            ")
                card_1 = int(input("Digite a primeira carta: "))
                if card_1 < 0:
                    raise NegativeValue
                if card_1 > 15:
                    raise ValueAbove

                
                print("____________________________")
                print("                            ")
                print("         TABULEIRO          ")
                print("____________________________")
                show_game(board_cards_list, board_cards, hits, user_position = [card_1])

                
                print("____________________________")
                print("                            ")
                card_2 = int(input("Digite a segunda carta: "))
                if card_2 < 0:
                    raise NegativeValue
                
                if card_2 > 15:
                    raise ValueAbove                
                
                print("____________________________")
                
                print("____________________________")
                print("                            ")
                print("         TABULEIRO          ")
                print("____________________________")
                
                show_game(board_cards_list, board_cards, hits, user_position = [card_1, card_2])

                print("____________________________")


                if board_cards[board_cards_list[card_1]] == board_cards[board_cards_list[card_2]]:
                    print("            ")
                    print("Você Acertou")
                    hits.append(board_cards_list[card_1])
                else:
                    score = score_lose(score)
                    if score == 0:
                        print("Fim de jogo! Você perdeu")
                        option = input("Deseja jogar novamente? y - sim | n - não: " )
                        if option == "y":
                            game_board()
                        else:
                            exit()

            print("Fim de jogo! Você ganhou")
            ranking_file(user_name, score)
            option = input("Deseja jogar novamente? y - sim | n - não: " )
            if option == "y":
                game_board()
            else:
                exit()


        else:
            raise InvalidOption
        
    except InvalidOption:
        print("")
        print("⨷ ERRO! Você digitou uma opção inválida")
        print("⟳Retornando ao menu...")

    except NegativeValue:
        print("")
        print("⨷ ERRO! Você digitou um número negativo ")
        print("⟳Retornando ao menu...")

    except ValueAbove:
        print("")
        print("⨷ ERRO! Você digitou um número acima de 15 ")
        print("⟳Retornando ao menu...")





def main():
    opt = 0


    while opt != 2:
        print("____________________________")
        print("                            ")
        print("      JOGO DA MEMÓRIA       ")
        print("____________________________")

        print("")
        print("1 - Jogar")
        print("2 - Ranking")
        print("3 - Sair")
        print("____________________________")
        
        try:
            print("            ")
            opt = int(input("Escolha uma opção? "))
            if opt < 0:
                raise NegativeValue
            
            if opt < 1 or opt > 3:
                raise InvalidOption
            
            elif opt == 1:
                game_board()
            
            elif opt == 2:
                ranking()

            elif opt == 3:
                exit()

        except NegativeValue:
            print("            ")
            print("⨷ ERRO! Você digitou um valor Valor negativo")

        except ValueError:
            print("            ")
            print("⨷ ERRO! O valor digitado precisa ser um número")

        except InvalidOption:
            print("            ")
            print("⨷ ERRO! Digite uma opção válida")



main()