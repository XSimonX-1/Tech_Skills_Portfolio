import character.Hero;
import character.MonsterArmy;
import board.Board;

public class GameSetup {

  private Board board;
  private Hero hero;
  private MonsterArmy monsterArmy;
  private GameLogic gameLogic;

  public static final int START_LEVEL = 0;
  public static final int START_FIELD = -1;

  public GameSetup(char[][] boardSetup, boolean isFieldTypeVisible) {
    this.board = new Board(boardSetup);
    this.monsterArmy = new MonsterArmy(board);
    this.hero = new Hero(START_LEVEL, START_FIELD);
    this.gameLogic = new GameLogic(START_LEVEL, START_FIELD, isFieldTypeVisible);
    this.board.printBoard(isFieldTypeVisible);
    if(isFieldTypeVisible) {
      this.monsterArmy.printMonsterArmy();
    }
  }

  public void start() {
    System.out.println("\tH - Hero");
    System.out.println("\tM - Monster");
    System.out.println("\tB - Boss Monster");
    System.out.println("\ta - attack point");
    System.out.println("\th - health point");
    System.out.println("\tp - position");
    this.gameLogic.run(this.board, this.hero, this.monsterArmy);
  }
}