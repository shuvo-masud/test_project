import javax.swing.*;
import java.awt.*;
import java.util.Random;

public class CheckYourTomorrow {

    public static void main(String[] args) {

        JFrame frame = new JFrame("Check Your Tomorrow");
        frame.setSize(450, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.gridx = 0;

        //TITLE
        JLabel title = new JLabel("CHECK YOUR TOMORROW");
        title.setFont(new Font("Arial", Font.BOLD, 22));

        gbc.gridy = 0;
        panel.add(title, gbc);

        //INPUT LABEL
        JLabel inputLabel = new JLabel("Enter a 3-digit number:");
        gbc.gridy = 1;
        panel.add(inputLabel, gbc);

        //INPUT FIELD
        JTextField inputField = new JTextField(10);
        gbc.gridy = 2;
        panel.add(inputField, gbc);

        //BUTTONS
        JButton drawButton = new JButton("Go");
        JButton refreshButton = new JButton("↻");

        gbc.gridy = 3;
        panel.add(drawButton, gbc);

        gbc.gridy = 4;
        panel.add(refreshButton, gbc);

        //RESULT LABEL
        JLabel resultLabel = new JLabel("Result will appear here");
        resultLabel.setFont(new Font("Arial", Font.BOLD, 14));

        gbc.gridy = 5;
        panel.add(resultLabel, gbc);

        frame.add(panel);
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        // DRAW BUTTON LOGIC
        drawButton.addActionListener(e -> {

            String input = inputField.getText().trim();
            int userNumber;

            try {
                userNumber = Integer.parseInt(input);

                if (userNumber < 100 || userNumber > 999) {
                    resultLabel.setText("Enter a valid 3-digit number!");
                    return;
                }

            } catch (Exception ex) {
                resultLabel.setText("Invalid input!");
                return;
            }

            Random random = new Random();

            int[] numbers = new int[5];
            numbers[0] = userNumber;

            for (int i = 1; i < 5; i++) {
                numbers[i] = random.nextInt(900) + 100;
            }

            for (int i = numbers.length - 1; i > 0; i--) {
                int j = random.nextInt(i + 1);
                int temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }

            String message = "";

            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] == userNumber) {

                    switch (i + 1) {
                        case 1 -> message = "Horray! It can be a lucky day";
                        case 2 -> message = "Okay! Hardwork can Change It";
                        case 3 -> message = "A Casual day!";
                        case 4 -> message = "Be Careful on Your Next Step!";
                        case 5 -> message = "May God Help You!";
                    }
                    break;
                }
            }

            resultLabel.setText(message);
        });

     
        // REFRESH BUTTON LOGIC
        refreshButton.addActionListener(e -> {

            inputField.setText("");
            resultLabel.setText("Result will appear here");

        });
    }
}