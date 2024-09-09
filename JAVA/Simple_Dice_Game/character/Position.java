package character;

public class Position {
  private int level;
  private int field;

  public Position(int level, int field) {
    this.level = level;
    this.field = field;
  }

  public int getLevel() {
    return this.level;
  }

  public int getField() {
    return this.field;
  }

  public void setLevel(int level) {
    this.level = level;
  }

  public void setField(int field) {
    this.field = field;
  }

  public String getPositionString() {
    return "[" + this.level + ", " + this.field + "]";
  }
}