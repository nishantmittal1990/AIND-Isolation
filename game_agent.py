"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """ custom_score heuristic function idea is to implement aggressive heuristic function    
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = len(game.get_legal_moves(player))  # Calculate length of myPlayer moves
    length_opp_payer_moves = len(game.get_legal_moves(game.get_opponent(player)))  # Calculate length of opposite player moves same as custom score 2
    return float(length_my_player_moves - 1.5*length_opp_payer_moves)

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_2 heuristic function idea is to implement defensive heuristic function
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_moves = len(game.get_legal_moves(player)) # calculated length of available moves for my player
    length_moves_opponent_player = len(game.get_legal_moves(game.get_opponent(player))) #Calculated length of available moves for opponent player
    return float(1.5*length_my_moves - length_moves_opponent_player)

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_3 heuristic function aims at maximizing win chances of my agent
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = 1.0 * len(game.get_legal_moves(player))#Calculate length of available moves for myPlayer
    length_opp_payer_moves = len(game.get_legal_moves(game.get_opponent(player)))#Calculate length of available moves with oppositePlayer

    if length_my_player_moves == 0:
        return float("-inf")

    if length_opp_payer_moves == 0:
        return float("inf")

    return float(length_my_player_moves/length_opp_payer_moves)

def custom_score_4(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_4 heuristic function aims at minimizing loosing chances of myPlayer
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = len(game.get_legal_moves(player)) #Calculate length of available moves for myPlayer
    length_opp_payer_moves = 1.0 * len(game.get_legal_moves(game.get_opponent(player)))#Calculate length of available moves for the oppositePlayer

    if length_my_player_moves == 0:
        return float("-inf")

    if length_opp_payer_moves == 0:
        return float("inf")

    return float(-length_opp_payer_moves/length_my_player_moves)

def custom_score_5(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_5 heuristic function defines chances heuristics
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = len(game.get_legal_moves(player)) #Calculate length of available moves for myPlayer
    length_opp_payer_moves = len(game.get_legal_moves(game.get_opponent(player)))#Calculate length of available moves for the oppositePlayer
    return float(length_my_player_moves*length_my_player_moves - length_opp_payer_moves*length_opp_payer_moves)

def custom_score_6(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_6 heuristic function aims towards weighted chances heuristics
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = len(game.get_legal_moves(player)) #Calculate length of available moves for myPlayer
    length_opp_payer_moves = len(game.get_legal_moves(game.get_opponent(player)))#Calculate length of available moves for the oppositePlayer
    return float(length_my_player_moves*length_my_player_moves - 1.5*length_opp_payer_moves*length_opp_payer_moves)

def custom_score_7(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    """custom_score_7 heuristic function also aims towards weighted chances heuristics
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    length_my_player_moves = len(game.get_legal_moves(player)) #Calculate length of available moves for myPlayer
    length_opp_payer_moves = len(game.get_legal_moves(game.get_opponent(player)))#Calculate length of available moves for the oppositePlayer
    return float(1.5*length_my_player_moves*length_my_player_moves - length_opp_payer_moves*length_opp_payer_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        #Fetching legal moves for the active player at max level
        legal_moves = game.get_legal_moves()
        #Terminial condition - if there are no legal moves left will call the utility function
        if not legal_moves:
            return game.utility(self) #Returning utility function
        #Assigning default value to best move
        best_move = legal_moves[0]
        #Assigning default value to best score as -inf
        best_score = float('-inf')
        #for each future legal move of active player
        for move in legal_moves:
            #Fetching next state forecast moves
            next_state = game.forecast_move(move)
            #Calling min_value function for score - Return type of min_value function is score
            score = self.min_value(next_state, depth-1)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move #Return best_move

    def max_value(self, next_game_state, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth <= 0:
            return self.score(next_game_state, self)
        legal_moves = next_game_state.get_legal_moves()
        if not legal_moves:
            return next_game_state.utility(self)
        #Initialize best score as -inf for maximize function
        best_score = float('-inf')
        for move in legal_moves:
            next_state = next_game_state.forecast_move(move)
            #Calculating best score as maximum score out of best_score i.e. -inf and score returned from minimizing function
            best_score = max([best_score, self.min_value(next_state, depth - 1)])
        return best_score


    def min_value(self, next_game_state, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        #Return score if the defined depth==0
        if depth <= 0:
            return self.score(next_game_state, self)
        legal_moves = next_game_state.get_legal_moves()
        if not legal_moves:
            return next_game_state.utility(self)
        #Initialize best score to be 'inf' for minimize function
        #Only point of initializing best score as +inf as we have to take score which is less than +inf
        #for minizing function -- Basic requirement
        best_score = float('inf')
        for move in legal_moves:
            next_state = next_game_state.forecast_move(move)
            #Calculating best score as minimum score out of best_score i.e. +inf and score returned from maximizing function
            best_score = min([best_score, self.max_value(next_state, depth - 1)])

        return best_score


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left
        legal_moves = game.get_legal_moves()
        if not legal_moves:
            return (-1, -1)


        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_score = float("-inf")
        best_move = legal_moves[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            self.search_depth = 1
            while best_score is not float("inf"):
                best_move = self.alphabeta(game, self.search_depth, alpha=float("-inf"), beta=float("inf"))
                self.search_depth += 1
        except SearchTimeout:
            return best_move
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of <-- Nishant to take care of this one
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        #Get Legal moves for active player
        legal_moves = game.get_legal_moves()
        #if there are no remaining legal moves available - Terminal state return utility function
        if not legal_moves:
            return game.utility(self)
        #initialize best score as -inf - this needs to be used as alpha as well
        best_score = float("-inf")
        #Initialize best move as None
        best_move = None
        for move in legal_moves:
            next_state = game.forecast_move(move)
            #minimum value function called with input values as game state, depth, score and beta--> inf
            score = self.min_value(next_state, depth-1, best_score, beta)
            if score > best_score: #compare the returned score with best_score
                best_score = score #assign the score as a best score if score is greater than best_score
                best_move = move #assign same move as a best_move - for which score is the best_score
        return best_move #Return best move from alphabeta function

    def min_value(self, next_game_state, depth, alpha, beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth <= 0: #Calling score function in case depth ==0
            return self.score(next_game_state, self)
        legal_moves = next_game_state.get_legal_moves()
        if not legal_moves:
            return next_game_state.utility(self)
        score = float("inf") #default value of score is defined as +inf in case of minimizing function
        for move in legal_moves:
            next_state = next_game_state.forecast_move(move)
            score = min(score, self.max_value(next_state, depth-1, alpha, beta))
            if score <= alpha: #This condition is written in order to prune if possible
                return score
            beta = min(beta, score)#Assign beta as minimum value out of beta and score returned from maximizing function
        return score

    def max_value(self, next_game_state, depth, alpha, beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth <= 0:
            return self.score(next_game_state, self)
        legal_moves = next_game_state.get_legal_moves()
        if not legal_moves:
            return next_game_state.utility(self)
        score = float("-inf") #initialized default score as -inf in case of maximizing function
        for move in legal_moves:
            next_state = next_game_state.forecast_move(move)
            score = max(score, self.min_value(next_state, depth -1, alpha, beta))
            if score >= beta: #Prune if possible
                return score
            alpha = max(alpha, score) #assign alpha as max of alpha or score(max) returned from minimizing function
        return score