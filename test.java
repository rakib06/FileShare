import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FileInputStream fstream = new FileInputStream("text.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(fstream));

        String strLine;

//Read File Line By Line
        while ((strLine = br.readLine()) != null)   {
            // Print the content on the console
            System.out.println (strLine);
        }

//Close the input stream
        fstream.close();
        System.out.println("Hello world!");
    }
}
