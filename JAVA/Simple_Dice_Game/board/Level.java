package board;

import character.Position;

public class Level {
  private Field[] fields;

  public Level(char[] levelSetup) {
    this.fields = createLevelFromSetup(levelSetup);
  }

  public Field getField(int fieldNumber) {
    return this.fields[fieldNumber];
  }

  public Field[] getFields() {
    return this.fields;
  }

  private Field[] createLevelFromSetup(char[] levelSetup) {
    Field[] fields = new Field[levelSetup.length];

    for (int i = 0; i < levelSetup.length; i++) {
      char fieldChar = levelSetup[i];
      if (fieldChar == 'M') {
        fields[i] = new Field(FieldType.MONSTER);
      } else if(fieldChar == 'P') {
        fields[i] = new Field(FieldType.POTION);
      } else {
        fields[i] = new Field(FieldType.BOSS);
      }
    }

    return fields;
  }

  public void printLevel(int level, Position heroPosition, boolean isFieldTypeVisible) {
    System.out.print("Level " + level + " ");
    for (int i = 0; i < this.fields.length; i++) {
      if (heroPosition.getField() == i) {
        System.out.print("[H]");
      } else {
        fields[i].printField(isFieldTypeVisible);
      }
    }
    System.out.println();
  }
}