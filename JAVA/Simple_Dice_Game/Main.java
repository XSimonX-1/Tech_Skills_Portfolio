public class Main {
    private static final char[][] BOARD = {
        { 'M', 'M', 'P', 'P', 'M', 'P', 'M', 'P', 'P', 'B' },
        { 'P', 'M', 'P', 'M', 'M', 'P', 'P', 'M', 'P', 'B' },
        { 'M', 'P', 'P', 'M', 'M', 'M', 'P', 'P', 'P', 'B' }
    };
    private static final boolean IS_FIELD_TYPE_VISIBLE = false;
    
    public static void main(String[] args) {    
      new GameSetup(BOARD, IS_FIELD_TYPE_VISIBLE).start();
    }
}
