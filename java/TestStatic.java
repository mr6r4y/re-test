import java.awt.*;

public class TestStatic
{
  public static void main( String[] args ) {
    System.out.println(Color.red.green.blue);
    System.out.println(Color.red.green.blue.magenta);
    // TestStatic.java:8: error: value is not public in Color; cannot be accessed from outside package
    // System.out.printf("Magenta: %d\n", Color.red.green.blue.magenta.value);
  }
}
