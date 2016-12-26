"""

Write/Read parameters matrix protocol:

    Summery:
        The parameters matrix will be presented in Python's list syntax in predetermined .py file,
        under the global space-name PARAM_MATRIX.

        The conditions are python function (That return Boolean value),
        found in predetermined .py file (Default is conditions.py).
        The actions are Python functions, found in predetermined .py file (Default is actions.py).

    The matrix will address the following form:

        Explanation:
            Con_i / Ac_i should be interpreted as the i condition / action in the matrix;
            The conditions are predicate that gets Game and int represent the game-state and bot-index,
            analyze it and return True if the bot position in the board meets the requirements.
            The action can be combination of several basic operations from the bots's op interface.

         | Con_1 | Con_2 | Con_3 | ...
    -----+-------+-------+-------+-...
    Ac_1 | ...
    -----+-...
    Ac_2 | ...
    -----+-...
    Ac_3 | ...
    -----+-...
    ...

    The value in the I row and j column is the score for preforming the action Ac_i in case the Co_j is True.

    Why?
    This method seems easy to write, and even more easy to read by a python coded bot.

    How to build the matrix?
    This is the step that may combine some ML techniques which I'll describe samples in the next paragraph.
    Idea_1:
        Building an analyzer extension for generic bot;

        It added to the competing bot's do_turn function, and wrap the basic operations
        so it will be able to monitor it.

        In each turn he takes the True-conditions and
        increase the value in the row of every action that took place in the move.
        For the end it normalize the values in the matrix.

        Using that we can watch demo battles and fit matrix to each competing bot.

    Idea_2:
        Building evolutionary system that runs on the parameters matrix generated using #Idea_1,
        and by doing that finds MLE for building that best guided bot.
"""
