package character;

import helper.TestDiceRolls;

public abstract class GameCharacter {
  private double healthPoint;
  private double attackPoint;
  private Position position;
  private char initial;

  public GameCharacter(double healthPoint, double attackPoint, Position position, char initial) {
    this.healthPoint = healthPoint;
    this.attackPoint = attackPoint;
    this.position = position;
    this.initial = initial;
  }

  public double getHealthPoint() {
    return this.healthPoint;
  }

  public void setHealthPoint(double healthPoint) {
    this.healthPoint = healthPoint;
  }

  public double getattackPoint() {
    return this.attackPoint;
  }

  public Position getPosition() {
    return this.position;
  }

  public char getInitial() {
    return this.initial;
  }

  public void printGameCharacter() {
    System.out.println(this.initial + " = " + "{ a: " + this.attackPoint + ", h: " + (this.healthPoint < 0 ? "0" : this.healthPoint) + ", p: " + this.position.getPositionString() + " }");
  }

  public void fight(GameCharacter GameCharacter) {
    double damage = this.attack();
    System.out.println(this.initial + " attack:  " + damage);
    double newHeroHealth = GameCharacter.getHealthPoint() - damage;
    GameCharacter.setHealthPoint(newHeroHealth);
    GameCharacter.printGameCharacter();
    if (GameCharacter.getHealthPoint() <= 0) {
      System.out.println("-----" + GameCharacter.getInitial() + " DEAD-----");
    }
  }

  public abstract double attack();
}