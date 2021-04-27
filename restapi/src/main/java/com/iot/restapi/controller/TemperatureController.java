package com.iot.restapi.controller;

import com.iot.restapi.entity.Temperature;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/temperature")
public class TemperatureController {

    Temperature currentTemp = new Temperature();

    @GetMapping
    public Temperature listTemperature(){
        return currentTemp;
    }

    @PutMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public @ResponseBody Temperature updateTemperature (@RequestBody String temperature) throws JSONException {   //Kriegt den Wert {temperatur:FLOAT} uebergeben
        //System.out.println(temperature); // Letzte Beispielausgabe: {temperature:42.2}
        JSONObject jo = new JSONObject(temperature);
        float temp = Float.valueOf(jo.get("temperature").toString());
        //System.out.println(temp);
        currentTemp.setTemperature(temp);
        System.out.println("Die Temperatur wurde geändert und beträgt nun: "+temperature);
        return currentTemp;
    }
}
