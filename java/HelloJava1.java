import javax.swing.*;

public class HelloJava1 
{
  public static void main(String[] args) {
    JFrame frm = new JFrame();
    JLabel lb = new JLabel("Hello, Java !", JLabel.CENTER);
    frm.getContentPane().add(lb);
    frm.setSize(300, 300);
    frm.setVisible(true);
  }
}