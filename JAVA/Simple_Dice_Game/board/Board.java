package board;

import character.Position;

public class Board {
  private int numberOfLevels;
  private int numberOfFields;
  private Level[] board;
  private int currentLevel;

  public Board(char[][] boardSetup) {
    this.numberOfLevels = boardSetup.length;
    this.numberOfFields = boardSetup[0].length;
    this.currentLevel = 0;
    this.board = createBoardFromSetup(boardSetup);
  }

  public int getNumberOfLevels() {
    return this.numberOfLevels;
  }

  public void setNumberOfLevels(int numberOfLevels) {
    this.numberOfLevels = numberOfLevels;
  }

  public int getNumberOfFields() {
    return this.numberOfFields;
  }

  public void setNumberOfFields(int numberOfFields) {
    this.numberOfFields = numberOfFields;
  }

  public Level[] getBoard() {
    return this.board;
  }

  public void setBoard(Level[] board) {
    this.board = board;
  }

  public int getCurrentLevel() {
    return this.currentLevel;
  }

  public void setCurrentLevel(int currentLevel) {
    this.currentLevel = currentLevel;
  }

  private Level[] createBoardFromSetup(char[][] boardSetup) {
    Level[] levels = new Level[boardSetup.length];

    for (int i = 0; i < boardSetup.length; i++) {
      levels[i] = new Level(boardSetup[i]);
    }

    return levels;
  }

  public void printBoard(boolean isFieldTypeVisible) {
    for (int i = 0; i < numberOfLevels; i++) {
      this.board[i].printLevel(i + 1, new Position(-1, -1), isFieldTypeVisible);
    }
  }
}