import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class HelloJava2
{
  public static void main(String[] args) {
    JFrame frm = new JFrame("Hello");
    frm.add(new HelloComponent2("Hello, Johny!"));
    frm.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frm.setSize(300, 300);
    frm.setVisible(true);
  }
}

class HelloComponent2 extends JComponent implements MouseMotionListener
{
  String theMessage;
  int messageX = 125;
  int messageY = 90;

  public HelloComponent2(String message) {
    theMessage = message;
    addMouseMotionListener(this);
  }

  public void paintComponent(Graphics g) {
    g.drawString(theMessage, messageX, messageY);
  }

  public void mouseDragged(MouseEvent e) {
    messageX = e.getX();
    messageY = e.getY();
    repaint();
  }

  public void mouseMoved(MouseEvent e) {}
}