import javax.swing.*;
import java.awt.*;

public class HelloJava1_1
{
  public static void main(String[] args) {
    JFrame frm = new JFrame();
    frm.add(new HelloComponent());
    frm.setSize(300, 300);
    frm.setVisible(true);
  }
}

class HelloComponent extends JComponent
{
  public void paintComponent(Graphics g) {
    g.drawString("Hello, Component !", 125, 95);
  }
}