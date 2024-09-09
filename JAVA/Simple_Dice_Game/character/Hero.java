package character;

import helper.RandomDiceRoll;
import board.Field;
import board.FieldType;

public class Hero extends GameCharacter {

  private static final char HERO_INITIAL = 'H';
  private static final double BASE_HEALTH = 100.0;
  private static final double INSTANT_KILL = 1000.0;
  private static final double HARD_ATTACK = 10.0;
  private static final double MEDIUM_ATTACK = HARD_ATTACK * (60.0 / 100.0);
  private static final double WEAK_ATTACK = HARD_ATTACK * (30.0 / 100.0);

  public Hero(int level, int field) {
    super(BASE_HEALTH, HARD_ATTACK, new Position(level, field), HERO_INITIAL);
  }

  public void step(int field) {
    this.getPosition().setField(field);
  }

  public void changeLevel(int level) {
    this.getPosition().setLevel(level);
  }
  
  @Override
  public double attack() {
    int currentDiceRoll = RandomDiceRoll.roll();

    System.out.println(Hero.HERO_INITIAL + " rolled a(n) " + currentDiceRoll);

    double attackAmount = 0;

    if (currentDiceRoll == 1 || currentDiceRoll == 2) {
      attackAmount = Hero.INSTANT_KILL;
    } else if (currentDiceRoll == 3 || currentDiceRoll == 4) {
      attackAmount = Hero.HARD_ATTACK;
    } else if (currentDiceRoll == 5 || currentDiceRoll == 6) {
      attackAmount = Hero.MEDIUM_ATTACK;
    } else if (currentDiceRoll == 7 || currentDiceRoll == 8) {
      attackAmount = Hero.WEAK_ATTACK;
    }

    return attackAmount;
  }

  public boolean isReadyToFight(Field field) {
    return field.getFieldType() == FieldType.MONSTER || field.getFieldType() == FieldType.BOSS;
  }  
}