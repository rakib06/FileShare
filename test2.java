package features;

import com.intuit.karate.Results;
import com.intuit.karate.Runner;
import net.masterthought.cucumber.Configuration;
import net.masterthought.cucumber.ReportBuilder;
import org.apache.commons.io.FileUtils;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class Demo {

//    @Karate.Test
//    Karate demo(){
////        Results results = Runner.path("classpath:features")
////                .outputCucumberJson(true)
////                .parallel(10);
////        generateReport(results.getReportDir());
////        assertEquals(0,results.getFailCount(), results.getErrorMessages());
//        slackPost();
//        return Karate.run().relativeTo(getClass());
//    }
//"classpath:com.demo.project"
    @Test
    public void testParallel() {
        Results results = Runner.path("classpath:features")
                .outputCucumberJson(true)
                .parallel(10);
        generateReport(results.getReportDir());
        assertEquals(0,results.getFailCount(), results.getErrorMessages());
        //assertTrue(results.getErrorMessages(), results.getFailCount() == 0);
    }

    public static void generateReport(String karateOutputPath) {
        Collection<File> jsonFiles = FileUtils.listFiles(new File(karateOutputPath), new String[] { "json" }, true);
        List<String> jsonPaths = new ArrayList<String>(jsonFiles.size());
        jsonFiles.forEach(file -> jsonPaths.add(file.getAbsolutePath()));
        Configuration config = new Configuration(new File("target"), "demo");
        ReportBuilder reportBuilder = new ReportBuilder(jsonPaths, config);
        reportBuilder.generateReports();
    }

    @AfterAll
    public static void slackPost() {
        System.out.println("Sending Slack API");
        // @Deprecated HttpClient httpClient = new DefaultHttpClient();
        HttpClient httpClient = HttpClientBuilder.create().build();
        try {
            HttpPost request = new HttpPost("https://slack.com/api/chat.postMessage");
            StringEntity params = new StringEntity("{\"channel\":\"C04H4GPBVE2\",\"text\":\"hello from java\"} ");
            request.addHeader("content-type", "application/json");
            request.addHeader("Authorization", "Bearer xoxb-2357231287538-4586831077141-kt8PseKeoNTzuiYrP3opWB24");
            request.setEntity(params);
            HttpResponse response = httpClient.execute(request);
            System.out.println(response.toString());
            System.out.println(response.getStatusLine());

        } catch (Exception ex) {
            System.out.println("Error");
        }
    }



}
