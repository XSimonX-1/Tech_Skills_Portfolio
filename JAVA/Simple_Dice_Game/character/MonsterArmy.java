package character;

import board.Board;
import board.Level;
import board.FieldType;
import java.util.ArrayList;

public class MonsterArmy {
  private ArrayList<GameCharacter> army;
  private Board board;

  public MonsterArmy(Board board) {
    this.board = board;
    this.army = createMonsters();
  }

  public ArrayList<GameCharacter> getArmy() {
    return this.army;
  }

  public void setArmy(ArrayList<GameCharacter> army) {
    this.army = army;
  }

  public Board getBoard() {
    return this.board;
  }

  public void setBoard(Board board) {
    this.board = board;
  }

  public Monster createMonster(int level, int field, char initial) {
    double attackPoint = Monster.BASE_MONSTER_ATTACK * (level + 1);
    double healthPoint = (Monster.BASE_MONSTER_HEALTH * (level + 1)) - Monster.BASE_MONSTER_ATTACK * level;
    return new Monster(healthPoint, attackPoint, new Position(level, field), initial);
  }

  public Monster createBoss(int level, int field, char initial) {
    double attackPoint = Monster.BASE_BOSS_ATTACK * (level + 1);
    double healthPoint = (Monster.BASE_BOSS_HEALTH * (level + 1)) - Monster.BASE_BOSS_ATTACK * level;
    return new Monster(healthPoint, attackPoint, new Position(level, field), initial);
  }

  public ArrayList<GameCharacter> createMonsters() {
    Level[] levels = this.board.getBoard();
    ArrayList<GameCharacter> monsters = new ArrayList<>();

    for (int i = 0; i < this.board.getNumberOfLevels(); i++) {
      for (int j = 0; j < this.board.getNumberOfFields(); j++) {

        FieldType fieldType = levels[i].getField(j).getFieldType();
        char initial = levels[i].getField(j).getInitial();

        if (fieldType == FieldType.MONSTER) {
          monsters.add(this.createMonster(i, j, initial));
        } else if (fieldType == FieldType.BOSS) {
          monsters.add(this.createBoss(i, j, initial));
        }
      }
    }

    return monsters;
  }

  public GameCharacter getMonster(int level, int field) {
    GameCharacter monster = null;

    for (int i = 0; i < this.army.size(); i++) {
      monster = this.army.get(i);
      if (monster.getPosition().getLevel() == level && monster.getPosition().getField() == field) {
        monster = this.army.remove(i);
        break;
      }
    }

    return monster;
  }

  public void printMonsterArmy() {
    for (int i = 0; i < this.army.size(); ++i) {
      this.army.get(i).printGameCharacter();
    }
  }
}