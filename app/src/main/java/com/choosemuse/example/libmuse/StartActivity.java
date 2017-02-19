package com.choosemuse.example.libmuse;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.gson.Gson;

import org.json.JSONObject;

import okhttp3.OkHttpClient;

public class StartActivity extends Activity {

    public static final String API_KEY = "AIzaSyBZOU5n6IVdOn4_xdIq7OW240AQOBJZAdk";
    private String vid_id;
    public String url;
    private OkHttpClient client;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_start);
        final Button searchButton = (Button) findViewById(R.id.searchButton);
        final EditText videoSearch = (EditText) findViewById(R.id.videoSearch);
        searchButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View view){
                try {
                    String text_input = videoSearch.getText().toString();
                    String keywords = text_input.replace(" ", "-");
                    url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q=" + keywords + "&type=video&key=AIzaSyBZOU5n6IVdOn4_xdIq7OW240AQOBJZAdk";
                    String response = new Youtube().execute(url).get();

                    Gson gson = new Gson();
                    JSONObject json = gson.fromJson(response, JSONObject.class);
                    vid_id = json.getJSONObject("items").getString("id").toString();

                    // youTubePlayerView.initialize(API_KEY, getMyself());

                    //player.cueVideo(vid_id);
                    //text.setText(vid_id);


                } catch (Exception e) {
                    e.printStackTrace();

                }
            }
        });
    }

}
