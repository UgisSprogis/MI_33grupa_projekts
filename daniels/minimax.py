# Kods izveidots ar ChatGPT
# Funkcija minimax, kas izmantojama, lai veiktu optimālu gājienu spēlē, izmantojot Minimax algoritmu.
def minimax(current_number, is_computer_turn):
    # Ja skaitlis ir mazāks vai vienāds ar 10, vai arī nedalās ur 2 vai 3, tad beidz darbību
    if current_number <= 10 or (current_number % 2 != 0 and current_number % 3 != 0):
        return 0, None

    if is_computer_turn:
        max_score = float('-inf')  # Sākumā maksimālā vērtība ir negatīvā bezgalība
        best_move = None  # Sākumā labākais gājiens nav zināms
        if current_number % 2 == 0:
            # Rekursīvi izsauc minimax funkciju ar samazinātu skaitli un norāda, ka nākamais gājiens būs cilvēkam
            score, next_move = minimax(current_number // 2, False)
            # Ja atrastais rezultāts ir lielāks par pašreizējo maksimālo, tad atjaunina vērtības
            if score > max_score:
                max_score = score
                best_move = 2
        if current_number % 3 == 0:
            # Līdzīgi kā iepriekš, bet ar dalīšanu ar 3
            score, next_move = minimax(current_number // 3, False)
            if score > max_score:
                max_score = score
                best_move = 3
        return max_score, best_move
    else:
        min_score = float('inf')  # Sākumā minimālā vērtība ir pozitīvā bezgalība
        if current_number % 2 == 0:
            # Rekursīvi izsauc minimax funkciju ar samazinātu skaitli un norāda, ka nākamais gājiens būs datoram
            score, next_move = minimax(current_number // 2, True)
            # Atjaunina minimālo vērtību, ja atrastais rezultāts ir mazāks
            min_score = min(min_score, score)
        if current_number % 3 == 0:
            # Līdzīgi kā iepriekš, bet ar dalīšanu ar 3
            score, next_move = minimax(current_number // 3, True)
            min_score = min(min_score, score)
        return min_score, None


# Funkcija, kas ļauj datoram izvēlēties dalītāju, izmantojot minimax algoritmu.
def computer_choose_number(current_number):
    next_move = None
    if current_number % 2 == 0:
        # Izvēlas labāko gājienu, izmantojot minimax algoritmu, kad datoram ir kārta iet
        score, next_move = minimax(current_number // 2, True)
    if current_number % 3 == 0  and not next_move:
        # Ja pirmais dalītājs nav piemērots, izmanto otro
        score, next_move = minimax(current_number // 3, True)
    return next_move

# Funkcija, kas atgriež datora gājienu.
def computer_turn(current_number):
    return computer_choose_number(current_number)

# Piemēra izmantošana
number_to_divide = 17946  # Piemēra skaitlis
chosen_divisor = computer_choose_number(number_to_divide)
print(chosen_divisor)  # Output: 3 vai 2
