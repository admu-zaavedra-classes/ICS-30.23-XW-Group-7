from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def test(request):
    return render(request, 'startpage.html')

def puzzle(request):    
    Goal_State = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    Puzzle_Size = 3   

    goal_position = list_to_dictionary_converter(Goal_State, Puzzle_Size)

    chosen_position = None
    puzzle_configuration = None
    search_type = None
    search_algorithm = None
    current_f_h = None
    current_f_m = None 
    current_f_UCS = None 
    moves = None 
    error_message = None
    final_list = None

    if request.method == "POST":
        puzzle_configuration = request.POST.get("puzzle_configuration")
        heuristic = request.POST.get("Heuristic")
        search_algorithm = request.POST.get("Informed_search_algorithm")
            
        if puzzle_configuration and puzzle_configuration != 'data_value':
            try:
                puzzle_list = [int(x.strip()) for x in puzzle_configuration.split(',')]
                if len(puzzle_list) == Puzzle_Size ** 2:
                    chosen_position = list_to_dictionary_converter(puzzle_list, Puzzle_Size)
                else:
                    raise ValueError("Invalid puzzle configuration length")
            except ValueError as e:
                error_message = f"Error parsing puzzle configuration: {e}"

        search_type = request.POST.get("search_type")
        
        if search_type == "Informed":
            if search_algorithm == "A*":
                if heuristic == 'Hamming':
                    current_f_h, moves,  final_list = A_Star(chosen_position, goal_position, heuristic)
                elif heuristic == 'Manhattan':
                    current_f_m, moves, final_list = A_Star(chosen_position, goal_position, heuristic)
                else:
                    error_message = "Invalid heuristic chosen for A*"
            else:
                error_message = "Invalid algorithm for Informed search"
        elif search_type == "Uninformed":
            search_algorithm = request.POST.get("Uninformed_search_algorithm")
            if search_algorithm == 'UCS':
                current_f_UCS, moves, final_list = UCS(chosen_position, goal_position)
            else:
                error_message = "Invalid algorithm for Uninformed search"
        elif search_type == "All":
            current_f_h, moves, final_list = A_Star(chosen_position, goal_position, 'Hamming')
            current_f_m, moves, final_list = A_Star(chosen_position, goal_position, "Manhattan")
            current_f_UCS, moves, final_list = UCS(chosen_position, goal_position)
    
    print(final_list)
    
    context = {
        'goal': goal_position,
        'data': chosen_position,
        'num_of_move': moves,
        'puzzle_configuration': puzzle_configuration,
        'search_type': search_type,
        'search_algorithm': search_algorithm,
        'f_score_h': current_f_h,
        'f_score_m': current_f_m,
        'f_score_UCS': current_f_UCS,
        'error_message': error_message,
        'final_list': final_list, 
    }

    return render(request, 'Contents/8-puzzle.html', context)

def csv_file(request):
    return render(request, 'Contents/csv_file.html')
