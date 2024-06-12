import unittest
from enums import *
import chess_engine
import Piece
import ai_engine



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game_state = chess_engine.game_state()
        self.test_game_state.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]

    def test_1_get_valid_piece_takes(self):
        test_game_state_ = self.test_game_state
        white_knight = chess_engine.Knight('n', 4, 4, Player.PLAYER_1)
        test_game_state_.board[4][4] = white_knight
        expected_takes = []
        valid_takes = white_knight.get_valid_piece_takes(test_game_state_)
        self.assertEqual(expected_takes, valid_takes)

    def test_2_get_valid_piece_takes(self):
        test_game_state_ = self.test_game_state
        white_knight = chess_engine.Knight('n', 4, 4, Player.PLAYER_1)
        test_game_state_.board[3][4] = white_knight
        test_game_state_.board[6][3] = chess_engine.Pawn('p', 6, 3, Player.PLAYER_2)
        expected_takes = {(6, 3)}
        valid_takes = set(white_knight.get_valid_piece_takes(test_game_state_))
        self.assertEqual(expected_takes, valid_takes)

    def test_3_get_valid_piece_takes(self):
        test_game_state_ = self.test_game_state
        black_knight = chess_engine.Knight('n', 3, 4, Player.PLAYER_2)
        test_game_state_.board[3][4] = black_knight
        test_game_state_.board[2][6] = chess_engine.Pawn('p', 2, 6, Player.PLAYER_1)
        test_game_state_.board[5][3] = chess_engine.Pawn('p', 5, 3, Player.PLAYER_1)
        expected_takes = {(2, 6), (5, 3)}
        valid_takes = set(black_knight.get_valid_piece_takes(test_game_state_))
        self.assertEqual(expected_takes, valid_takes)

    def test_1_get_valid_peaceful_moves(self):
        test_game_state_ = self.test_game_state
        black_knight = chess_engine.Knight('n', 3, 4, Player.PLAYER_2)
        test_game_state_.board[3][4] = black_knight
        expected_moves = {(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)}
        valid_moves = set(black_knight.get_valid_peaceful_moves(test_game_state_))
        self.assertEqual(expected_moves, valid_moves)

    def test_2_get_valid_peaceful_moves(self):
        test_game_state_ = self.test_game_state
        black_knight = chess_engine.Knight('n', 3, 4, Player.PLAYER_2)
        test_game_state_.board[3][4] = black_knight
        test_game_state_.board[1][5] = chess_engine.Pawn('p', 1, 5, Player.PLAYER_2)
        test_game_state_.board[2][2] = chess_engine.Pawn('p', 2, 2, Player.PLAYER_2)
        expected_moves = {(1, 3), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)}
        valid_moves = set(black_knight.get_valid_peaceful_moves(test_game_state_))
        self.assertEqual(expected_moves, valid_moves)

    def test_3_get_valid_peaceful_moves(self):
        test_game_state_ = self.test_game_state
        black_knight = chess_engine.Knight('n', 3, 4, Player.PLAYER_2)
        test_game_state_.board[3][4] = black_knight
        test_game_state_.board[1][5] = chess_engine.Pawn('p', 1, 5, Player.PLAYER_1)
        test_game_state_.board[5][3] = chess_engine.Pawn('p', 5, 3, Player.PLAYER_2)
        expected_moves = {(1, 3), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5)}
        valid_moves = set(black_knight.get_valid_peaceful_moves(test_game_state_))
        self.assertEqual(expected_moves, valid_moves)

    def test_1_get_valid_piece_moves(self):
        test_game_state_ = self.test_game_state
        black_knight = chess_engine.Knight('n', 3, 4, Player.PLAYER_2)
        test_game_state_.board[3][4] = black_knight
        test_game_state_.board[1][5] = chess_engine.Pawn('p', 1, 5, Player.PLAYER_1)
        test_game_state_.board[5][3] = chess_engine.Pawn('p', 5, 3, Player.PLAYER_1)
        expected_moves = {(1, 3), (2, 2), (2, 6), (4, 2), (4, 6), (5, 5), (1, 5), (5, 3)}
        valid_moves = set(black_knight.get_valid_piece_moves(test_game_state_))
        self.assertEqual(expected_moves, valid_moves)


class EvaluateBoardTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game_state = chess_engine.game_state()
        self.test_game_state.board = [[Player.EMPTY for _ in range(8)] for _ in range(8)]
        self.ai = ai_engine.chess_ai()

    def test_empty_board(self):
        expected_score = 0
        evaluation_score = self.ai.evaluate_board(self.test_game_state, Player.PLAYER_1)
        self.assertEqual(expected_score, evaluation_score)

    def test_single_white_pawn(self):
        pawn = chess_engine.Pawn('p', 4, 4, Player.PLAYER_1)
        self.test_game_state.board[4][4] = pawn
        expected_score = -10  # PLAYER_1 pawn
        evaluation_score = self.ai.evaluate_board(self.test_game_state, Player.PLAYER_1)
        self.assertEqual(expected_score, evaluation_score)

    def test_single_black_pawn(self):
        pawn = chess_engine.Pawn('p', 4, 4, Player.PLAYER_2)
        self.test_game_state.board[4][4] = pawn
        expected_score = 10  # PLAYER_2 pawn
        evaluation_score = self.ai.evaluate_board(self.test_game_state, Player.PLAYER_1)
        self.assertEqual(expected_score, evaluation_score)

    def test_mixed_pieces(self):
        pieces = [
            chess_engine.King('k', 0, 0, Player.PLAYER_1),
            chess_engine.Queen('q', 1, 1, Player.PLAYER_1),
            chess_engine.Rook('r', 2, 2, Player.PLAYER_1),
            chess_engine.Bishop('b', 3, 3, Player.PLAYER_1),
            chess_engine.Knight('n', 4, 4, Player.PLAYER_1),
            chess_engine.Pawn('p', 5, 5, Player.PLAYER_1),
            chess_engine.King('k', 0, 1, Player.PLAYER_2),
            chess_engine.Queen('q', 1, 2, Player.PLAYER_2),
            chess_engine.Rook('r', 2, 3, Player.PLAYER_2),
            chess_engine.Bishop('b', 3, 4, Player.PLAYER_2),
            chess_engine.Knight('n', 4, 5, Player.PLAYER_2),
            chess_engine.Pawn('p', 5, 6, Player.PLAYER_2)
        ]

        positions = [
            (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)
        ]

        for piece, (row, col) in zip(pieces, positions):
            self.test_game_state.board[row][col] = piece

        expected_score = (
                -1000 - 100 - 50 - 30 - 30 - 10 +  # PLAYER_1 pieces
                1000 + 100 + 50 + 30 + 30 + 10  # PLAYER_2 pieces
        )

        evaluation_score = self.ai.evaluate_board(self.test_game_state, Player.PLAYER_1)
        self.assertEqual(expected_score, evaluation_score)

class system_tests(unittest.TestCase):
    def setUp(self):
        self.test_game_state = chess_engine.game_state()

    def test_game(self):
        test_game_state_ = self.test_game_state
        test_game_state_.move_piece((1, 2), (2, 2), False)
        test_game_state_.move_piece((6, 3), (4, 3), False)
        test_game_state_.move_piece((1, 1), (3, 1), False)
        test_game_state_.move_piece((7, 4), (3, 0), False)
        self.assertEqual(0, test_game_state_.checkmate_stalemate_checker())


if __name__ == '__main__':
    unittest.main()
