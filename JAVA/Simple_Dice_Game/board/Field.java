package board;

public class Field {

  private FieldType fieldType;

  public Field(FieldType fieldType) {
    this.fieldType = fieldType;
  }

  public FieldType getFieldType() {
    return this.fieldType;
  }

  public char getInitial() {
    return this.fieldType.name().charAt(0);
  }

  public void printField(boolean isFieldTypeVisible) {
    System.out.print("[" + (isFieldTypeVisible ? getInitial() : " ") + "]");
  }
}