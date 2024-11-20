#include <iostream>
using namespace std;

// Function to display the game board
void displayBoard(char board[3][3]) {
    cout << "\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << board[i][j];
            if (j < 2) cout << " | ";
        }
        cout << "\n";
        if (i < 2) cout << "--|---|--\n";
    }
    cout << "\n";
}

// Function to check if there is a winner
char checkWinner(char board[3][3]) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) return board[i][0];
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) return board[0][i];
    }
    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) return board[0][2];
    return ' ';
}

// Function to check if the board is full (draw)
bool isBoardFull(char board[3][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ') return false;
    return true;
}

int main() {
    char board[3][3] = { {' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '} };
    char currentPlayer = 'X';
    char winner = ' ';
    int row, col;

    cout << "Welcome to Tic-Tac-Toe!\n";
    displayBoard(board);

    while (winner == ' ' && !isBoardFull(board)) {
        // Ask the current player for their move
        cout << "Player " << currentPlayer << ", enter your move (row and column, 1-3): ";
        cin >> row >> col;

        // Adjust for 0-based indexing
        row--; col--;

        // Check if the move is valid
        if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
            cout << "Invalid move! Try again.\n";
            continue;
        }

        // Make the move
        board[row][col] = currentPlayer;
        displayBoard(board);

        // Check for a winner
        winner = checkWinner(board);
        if (winner != ' ') break;

        // Switch player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    // Display the result
    if (winner != ' ')
        cout << "Congratulations! Player " << winner << " wins!\n";
    else
        cout << "It's a draw!\n";

    return 0;
}
