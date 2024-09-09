package helper;

import java.util.Random;

public class RandomDiceRoll {

  public static int roll() {
    Random random = new Random();
    return random.nextInt(9 - 1) + 1;
  }
}