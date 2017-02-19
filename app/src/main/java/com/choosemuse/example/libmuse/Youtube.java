package com.choosemuse.example.libmuse; /**
 * Created by sean on 2/19/17.
 */

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import android.os.AsyncTask;
import java.io.InputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Youtube extends AsyncTask<String, Void, String> {
    private static final String TAG = "MyActivity";
    String server_response;


    protected String doInBackground(String... Strings) {
        URL url;

        HttpURLConnection urlConnection = null;

        try {
            url = new URL(Strings[0]);

            urlConnection = (HttpURLConnection) url.openConnection();
            int responseCode = urlConnection.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                server_response = readStream(urlConnection.getInputStream());
                //Log.v(TAG, response);
                return null;


            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();

        }
        return null;

    }

    protected void onPostExecute(String result){
        super.onPostExecute(result);

    }

    private String readStream(InputStream in) {
        BufferedReader reader = null;
        StringBuffer response = new StringBuffer();
        try {
            reader = new BufferedReader(new InputStreamReader(in));
            String line = "";
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        return response.toString();
    }



}