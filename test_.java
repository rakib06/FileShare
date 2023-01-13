import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        String dir = System.getProperty("user.dir");
        System.out.println(dir);
        String cmd = "cmd dir";
//        Process p = Runtime.getRuntime().exec(cmd);
//        System.out.println("END");
////        p.waitFor();
////        BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
////        String line ="";
////        while (r.readLine() !=null) {
////            System.out.println("While Loop");
////            line = r.readLine();
////            if (line == null) { break; }
////            System.out.println(line);
////        }
////        System.out.println("END");
//

        ProcessBuilder builder = new ProcessBuilder(
                "cmd  ");
        builder.redirectErrorStream(true);
        Process p = builder.command("allure.cmd ", "serve").start();
        p.waitFor();
        BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String line =r.readLine();
        while (line!=null) {
            System.out.println(line);
            System.out.println("While Loop");
            line = r.readLine();
            if (line == null) { break; }
            System.out.println(line);
        }
        System.out.println("END");

    }
}
